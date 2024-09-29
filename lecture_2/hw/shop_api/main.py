from fastapi import FastAPI

app = FastAPI(title="Shop API")

@app.get("/")
async def root():
    return {"message": "Hello World"}