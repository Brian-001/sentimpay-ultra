from fastapi import WebSocket

class WSManager:

    def __init__(self):
        self.connections = []

    async def connect(self, websocket: WebSocket):

        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, message):

        for ws in self.connections:
            await ws.send_json(message)

manager = WSManager()