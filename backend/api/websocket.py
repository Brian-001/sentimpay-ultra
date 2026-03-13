from fastapi import APIRouter, WebSocket
from core.websocket_manager import manager

websocket_router = APIRouter()


@websocket_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:

            data = await websocket.receive_text()

            await manager.broadcast({
                "type": "heartbeat",
                "message": data
            })

    except Exception:
        manager.connections.remove(websocket)