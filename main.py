from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "ODOC"}

fake_items_db = {"yoonsik": "apple","seri": "banana","kenny": "orange"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {fake_items_db[item_id]}


@app.get("/add/{var1}/{var2}")
async def add(var1,var2):
    return {'add':int(var1)+int(var2)}

@app.get("/mul/{var1}/{var2}")
async def mul(var1,var2):
    return {'mul':int(var1)*int(var2)}

@app.get("/div/{var1}/{var2}")
async def div(var1,var2):
    return {'div':int(var1)/int(var2)}

@app.get("/sub/{var1}/{var2}")
async def sub(var1,var2):
    return {'sub':abs(int(var1)-int(var2))}

