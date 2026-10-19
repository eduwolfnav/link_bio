import asyncio

async def hello() -> str:
    await asyncio.sleep(4)
    return "Mensaje cargado con exito..."
