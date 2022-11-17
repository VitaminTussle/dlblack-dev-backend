from pymongo import MongoClient
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from dotenv import dotenv_values
from routes import router as nonogramRouter

config = dotenv_values(".env")
app = FastAPI(debug=True)

@app.on_event("startup")
def startup():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("connected to mongodb")

@app.on_event("shutdown")
def shutdown():
    app.mongodb_client.close()

@app.exception_handler(RequestValidationError)
async def validationExceptionHandler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

@app.exception_handler(StarletteHTTPException)
async def validationExceptionHandler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)

app.include_router(nonogramRouter, tags=["nonograms"], prefix="/nonogram")