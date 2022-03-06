from random import randint
from fastapi import FastAPI
import json

f = open("dicts.json", "r")
data = json.load(f)
app = FastAPI()
last_five = []


def return_random_word():
    if len(last_five) == 5:
        last_five.pop(0)

    a = data[randint(0, len(data))]
    if a in last_five:
        return return_random_word()
    else:
        last_five.append(a)
        return a


@app.get("/get_word")
async def return_a_word():
    value = return_random_word()

    return {"word": value["word"], "definition": value["definition"]}


@app.get("/")
async def root():
    return {"message": "Welcome to dictionary API"}


@app.get("/word/{word}")
async def get_word(word):
    g = 0
    not_found = False
    for i in data:
        g = g + 1
        if i["word"] == word.upper():
            return {"word": i["word"], "definition": i["definition"]}
        if g == len(data):
            not_found = True
        if not_found:
            return {"word": "Word not found", "definition": "Word not found"}
