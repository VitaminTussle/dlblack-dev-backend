from random import random
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from random import randrange
from models import Nonogram, NonogramUpdate

router = APIRouter()

@router.post("/create-nonogram", response_description="Create a new Nonogram puzzle entry", status_code=status.HTTP_201_CREATED, response_model=Nonogram)
def createNonogram(request: Request, nonogram: NonogramUpdate = Body(...)):
    nonogram = jsonable_encoder(nonogram)
    newNonogram = request.app.database["nonograms"].insert_one(nonogram)
    createdNonogram = request.app.database["nonograms"].find_one(
        {"_id": newNonogram.inserted_id}
    )
    return createdNonogram

@router.get("/get-nonogram", response_description="Get a random Nonogram puzzle", response_model=Nonogram)
def getNonogram(request: Request):
    nonograms = list(request.app.database["nonograms"].find())
    randInd = int(randrange(len(nonograms)))
    chosenNonogram = nonograms[randInd]
    return chosenNonogram