from fastapi import FastAPI
from database.mysql import get_preapproved_limit, get_interest_rate


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend running successfully!"}

@app.get("/test_mongo")
def test_mongo():
    return {"message": "MongoDB connection OK"}
@app.get("/test_mysql")
def test_mysql(phone: str):
    data = get_preapproved_limit(phone)
    return {"result": data}
