from fastapi import FastAPI
from api.routes import router
from api.websocket import websocket_router

app = FastAPI()

app.include_router(router)
app.include_router(websocket_router)