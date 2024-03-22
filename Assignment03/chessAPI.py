from time import time
import json
# from pydantic import BaseModel
from enum import Enum
from typing import Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


app = FastAPI()

with open('assets/data.json') as f:
    data = json.load(f)

class ChessPiecesNames(str, Enum):
    Pawn = "Pawn"
    Bishop = "Bishop"
    Knight = "Knight"
    Rook = "Rook"
    Queen = "Queen"
    King = "King"

# class ChessPieces(BaseModel):
#     name: Optional[ChessPiecesNames] = None

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
async def intro():
    result = {"description": data['description']}
    return FileResponse(f"{data['image_path']['all']}", headers=result)

@app.get("/pieces")
async def pieces(piece_name: Optional[ChessPiecesNames] = None, piece_image: Optional[ChessPiecesNames] = None):
    if piece_name is None and piece_image is None:
        return data["pieces"]
    elif piece_image is None:
        return data["pieces"][piece_name]
    elif piece_name is None:
        return FileResponse(f"{data['image_path'][piece_image]}")
    else:
        result = {"piece_info": f"{data['pieces'][piece_name]}"}
        return FileResponse(f"{data['image_path'][piece_image]}", headers=result)

@app.get("/rules")
async def rules():
    return data["rules"]

@app.get("/about_creator")
async def about_creator():
    return data["about_me"]

@app.get("/reference")
async def reference():
    return data["reference"]

