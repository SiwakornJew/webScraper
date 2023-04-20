
from fastapi import FastAPI
from getTemple import getTem
from fastapi.responses import FileResponse
app = FastAPI()


@app.get("/temple/{provide_name}")
async def getTemple(provide_name):
    li_match = getTem(provide_name)
    return li_match


@app.get("/temple/list_of_temple-csv")
async def download_csv():
    file_path = "list_temple.csv"
    return FileResponse(file_path, media_type="text/csv", filename="list_temple.csv")
