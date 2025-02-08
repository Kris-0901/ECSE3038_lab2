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

#decorator to define or create path
@app.post("/person")

async def create_new_person(request_person:Data):
    data.append(request_person)

    person_json = jsonable_encoder(request_person)

    return person_json


@app.get("/person") #decorator

async def get_persons_list():
    return data

