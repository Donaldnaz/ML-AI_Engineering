# FAST AP MODIFICATION FOR VERTEX AI ENDPOINTS

@app.get("/", response_model=HealthResponse)
async def root():
    """Root endpoint for basic health check - required by Vertex AI"""
    return HealthResponse(
        status="healthy" if models_loaded else "unhealthy",
        models_loaded=models_loaded,
        device=device,
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    )

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Detailed health check endpoint for Vertex AI readiness/liveness probes"""
    health_status = "healthy"
    
    # Check if models are loaded
    if not models_loaded:
        health_status = "unhealthy"
    
    # Check if CUDA is available when expected
    if device == "cuda" and not torch.cuda.is_available():
        health_status = "degraded"
    
    # Check disk space in /tmp
    try:
        stat = os.statvfs('/tmp')
        free_space_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
        if free_space_gb < 1.0:  # Less than 1GB free
            health_status = "degraded"
    except Exception:
        pass
    
    response = HealthResponse(
        status=health_status,
        models_loaded=models_loaded,
        device=device,
        timestamp=time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    )
    
    # Return appropriate HTTP status code
    if health_status == "healthy":
        return JSONResponse(status_code=200, content=response.dict())
    elif health_status == "degraded":
        return JSONResponse(status_code=200, content=response.dict())  # Still serving
    else:
        return JSONResponse(status_code=503, content=response.dict())  # Service unavailable

@app.get("/readiness")
async def readiness_check():
    """Kubernetes/Vertex AI readiness probe"""
    if models_loaded:
        return JSONResponse(status_code=200, content={"status": "ready"})
    else:
        return JSONResponse(status_code=503, content={
            "status": "not ready", 
            "error": model_load_error or "Models not loaded"
        })

@app.get("/liveness") 
async def liveness_check():
    """Kubernetes/Vertex AI liveness probe"""
    return JSONResponse(status_code=200, content={"status": "alive"})

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    """
    Main Vertex AI prediction endpoint.
    Expects instances with audio preprocessing parameters.
    """
    if not models_loaded:
        raise HTTPException(
            status_code=503, 
            detail=f"Models not loaded: {model_load_error or 'Unknown error'}"
        )
    
    predictions = []
    
    try:
        for instance in request.instances:
            # Convert instance to AudioPreprocessingRequest
            try:
                audio_request = AudioPreprocessingRequest(**instance)
            except Exception as e:
                predictions.append({
                    "error": f"Invalid request format: {str(e)}",
                    "status": "failed"
                })
                continue
            
            # Process the audio/video
            try:
                result = await process_task(audio_request.dict())
                predictions.append({
                    "status": "success",
                    "file_name": audio_request.file_name,
                    "processing_result": result,
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
                })
            except Exception as e:
                logging.error(f"Prediction failed for {audio_request.file_name}: {str(e)}")
                predictions.append({
                    "status": "failed", 
                    "file_name": audio_request.file_name,
                    "error": str(e),
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
                })
        
        return PredictionResponse(predictions=predictions)
        
    except Exception as e:
        logging.error(f"Prediction endpoint error: {str(e)}")
        logging.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
