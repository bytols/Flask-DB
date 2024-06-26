import asyncio
import websockets
import random
# create handler for each connection

async def handler(websocket, path):
    async for message in websocket:
        # message poderia ser o nome da ação
        print(f"Data received as:  {message}!")
        # retornar o valor da ação
        reply = f"{random.randint(1,100)}"
        await websocket.send(reply)

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()