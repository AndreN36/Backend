from fastapi import FastAPI
import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

@app.get("/")
def root():
    logging.info("Root endpoint accessed")
    return {"message": "FastAPI running"}