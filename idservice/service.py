from typing import AsyncGenerator
import uuid
import math
import time
import asyncio
import secrets
from idservice.config import config


async def snowflake_generator(machine_id: int):
    seq = 0
    last_t = -1
    while True:
        t = int(time.time() * 1000)
        if t != last_t:
            last_t = t
            seq = 0
        else:
            seq += 1
            if seq >= 4096:
                await asyncio.sleep(0.001)
                continue
        yield (seq | machine_id << 12 | t << 22)


def anext(x: AsyncGenerator):
    return x.__anext__()


_sf_instance = snowflake_generator(config.ID_SERVICE_SNOWFLAKE_MACHINE_ID)


async def generate_snowflake():
    v = await anext(_sf_instance)
    return {"id": v, "id_str": str(v), "id_hex": f"{v:016X}"}


async def generate_uuid():
    v = uuid.uuid4()
    return {
        "id_str": str(v),
        "id_hex": v.hex,
        "id": v.int,
    }


async def generate_random(bits):
    v = secrets.randbits(bits)
    hl = math.floor(bits // 4)
    return {"id": v, "id_str": str(v), "id_hex": format(v, f"0{hl}X")}
