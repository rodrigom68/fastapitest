from    fastapi import fastapi

app = fastapi()

@app.get("/")
async def root():
    return {"message": "Jeferson Caminhoes"}