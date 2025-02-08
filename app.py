"""ID# 620138053"""

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

#Structure / object to define Data format
class Data(BaseModel):
    name: str
    occupation: str
    address: str

#create instance of FastAPI class
app = FastAPI()

#list to store persons data
data = []

