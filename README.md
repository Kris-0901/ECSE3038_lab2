# FastAPI POST & GET Requests

## Summary 
This application allows persons' name, occupation and address to be stored in a list called data (which simulates a datbase) using Rest API POST requests. The POST request is submitted in JSON format to http://localhost:8000/person. The user may also retrieve all the persons' data using Rest API GET request on port 8000. The code implements error handling in the case of empty values in the defined keys. the app will return an error message if key is missing the required values.

### Anticipated Results 

**Input:** `POST /person`

**Output:**

```
{
    "success": true,
    "result": {
        "name": "Kristof",
        "occupation": "biomedical engineer",
        "address": "Kingston"
    }
}
```
**Input Invalid:** `POST /person`

**Output:**

```
{
    "success": false,
    "result": {
        "error_message": "invalid request"
    }
}
```

**Input**`GET/person`

**Output:**

```
[
    {
        "name": "Remy",
        "occupation": "Dealer",
        "address": "Kingston"
    },
    {
        "name": "Jim",
        "occupation": "Real Estate Agent",
        "address": "Kingston"
    },
    {
        "name": "Bob",
        "occupation": "Construction Worker",
        "address": "Kingston"
    },
    {
        "name": "Kristof",
        "occupation": "biomedical engineer",
        "address": "Kingston"
    }
]

```

**Input (list empty)**`GET/person`

**Output:**

```
{
    "status": "this database is empty. send a rest api post request to 'http://localhost:8000/person' in the following json format",
    "json format": {
        "name": "John",
        "occupation": "Boxer",
        "address": "21 First Street"
    }
}
```

## Purpose

This code was written to fulfill the course requirements of 'ECSE3038 Engineering Internet of Things Systems' and to learn the Python programming language.

## Favourite Pokemon

**Blaziken** 
Blaziken is a strong and valuable Pokémon. It has a high attack stat, impressive speed, and a versatile move pool. Blaziken's unique Fire/Fighting typing also gives it an advantage against certain types of Pokémon.

Also just looks cool ¯\_(ツ)_/¯