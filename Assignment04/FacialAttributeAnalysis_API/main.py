from time import time
# from typing import Optional
from fastapi import FastAPI, HTTPException, status, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import cv2
import numpy as np
from process import main_process


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

@app.middleware("http")
async def log_middleware(request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["Process-Time"] = f'Request {request.url} processed in {process_time} seconds.'
    return response

@app.get("/")
async def root():
    return {"description": "Welcome to Facial Attribute Analyzer API!\nThis API uses Deepface project as the main process for getting information from images and FastAPI to establish API."}

@app.post("/facial_attribute_analyzer")
async def facial_attribute_analyzer(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail="Unsupported media type")
    
    contents = await input_file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    image_rgb = cv2.imdecode(np_array, cv2.IMREAD_UNCHANGED)
    data = main_process(image_rgb)
    return {"data": data}
    

