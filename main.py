
from fastapi import FastAPI
from getTemple import getTem

app = FastAPI()


@app.get("/temple/{provide_name}")
async def getTemple(provide_name):
    li_match = getTem(provide_name)

    return li_match
