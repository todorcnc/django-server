# This file is related to websockets
import json

from channels.generic.websocket import AsyncWebsocketConsumer

class WebsocketConsumer(AsyncWebsocketConsumer):
   
    async def connect(self):
        username = self.scope["query_string"].decode("utf-8").split("=")[1]
        print(f"Username attempting to connect: {username}")
        print(f"Connection ID (Channel Name): {self.channel_name}")
        await self.accept()
        await self.channel_layer.group_add("notifications", self.channel_name)
    
    async def disconnect(self, close_code):
        print(f"Connection ID (Channel Name) closing: {self.channel_name}")
        await self.channel_layer.group_discard("notifications", self.channel_name)
    
    async def send_notification(self, event):

        await self.send(text_data=json.dumps(event))

    # This function will handle messages received from the WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('content', None)
        if message:
            print(f"Received message: {message}")
        else:
            print("Received a message, but no content field found.")