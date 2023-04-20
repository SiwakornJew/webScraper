from fastapi import FastAPI
from getTemple import getT
import requests
import re
app = FastAPI()


@app.get("/")
def getTemple():
    li_match = getT()
    return {"temple": li_match}
