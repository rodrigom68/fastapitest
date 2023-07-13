from typing import Union

from FastApi import FastApi  

app = FastApi()

@app.get("/")
async def root():
    return {"message": "Jeferson Caminhoes"}

@pp.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None)
    return {"item_id":item_id, "q":q}

