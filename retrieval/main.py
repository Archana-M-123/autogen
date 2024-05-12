from fastapi import FastAPI
from process import process_user_request

app = FastAPI()

@app.get("/process_user_input/")
async def process_user_input(user_request: str):
    result = process_user_request(user_request)
    return {"result": result}
