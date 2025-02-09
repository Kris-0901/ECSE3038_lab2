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

#function to add new person of type/class Data
async def create_new_person(new_person:Data):
   
    # iterate through all keys in new_person  and chjeck for None/ "" (empty string) and return success or faliure message
    for any_key in new_person:
        if  new_person.name == "" or new_person.address == "" or new_person.occupation== "":
            return {"success": False,"result": {"error_message": "invalid request"}}
        else:
            data.append(new_person)

            #convert dictionary/ class new_person to JSON format
            person_json = jsonable_encoder(new_person)
            return {"success": True,"result": person_json}


#decorator to define or create path
@app.get("/person") 

#function to return the entire lists of person using Rest API GET request. If list is empty it returns the expected input
async def get_persons_list():
    if not data :
        return {"status":"this database is empty. send a rest api post request to 'http://localhost:8000/person' in the following json format",
                "json format": {"name": "John","occupation": "Boxer","address":"21 First Street"}}
    return data

