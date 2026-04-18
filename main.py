from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from graph import get_concept, get_domain

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "running"}


@app.get("/concept")
def concept(q: str = Query(...)):
    return get_concept(q)


@app.get("/domain")
def domain(q: str = Query(...)):
    return get_domain(q)