from fastapi import FastAPI
from idservice.service import generate_uuid, generate_snowflake, generate_random

app = FastAPI()


@app.get("/api/version")
async def get_version():
    return {"version": "1.0"}


@app.get("/api/uuid")
async def gen_uuid():
    return await generate_uuid()


@app.get("/api/snowflake")
async def gen_snowflake():
    return await generate_snowflake()


@app.get("/api/random/{bits}")
async def gen_random(bits: int):
    return await generate_random(bits)
