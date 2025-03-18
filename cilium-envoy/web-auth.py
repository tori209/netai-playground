from typing import Union, Annotated
from fastapi import FastAPI, Header, status

import logging

app = FastAPI()

@app.get("/")
def read_root():
        return {"Hello": "World"}

@app.get("/ext-authz", status_code=200)
def auth(x_ext_authz: Annotated[str | None, Header()] = None):
        logging.info(x_ext_authz)
        print(x_ext_authz)
        return "OK"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
        return {"item_id": item_id, "q": q}