from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
#from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Pankaj": "Welcome to My API!"}

class StringInput(BaseModel):
    input_string: str

class StringStats(BaseModel):
    input_string: str
    token_count: int
    character_count: int

@app.post("/analyze_string", response_model=StringStats)
async def analyze_string(string_input: StringInput):
    input_string = string_input.input_string
    token_count = len(input_string.split())
    character_count = len(input_string)
    return {"input_string": input_string, "token_count": token_count, "character_count": character_count}


# class StringInput(BaseModel):
#     input_string: str

# class StringStats(BaseModel):
#     token_count: int
#     character_count: int

# @app.post("/analyze_string", response_model=StringStats)
# async def analyze_string(string_input: StringInput):
#     input_string = string_input.input_string
#     token_count = len(input_string.split())
#     character_count = len(input_string)
#     return {"token_count": token_count, "character_count": character_count}
