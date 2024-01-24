# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class TweetConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Add connected user to group
        await self.channel_layer.group_add("tweet_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove user from group when they disconnect
        await self.channel_layer.group_discard("tweet_updates", self.channel_name)

    async def receive(self, text_data):
        # Handle incoming messages (if necessary)
        pass

    async def tweet(self, event):
        # Send a message to WebSocket
        await self.send(text_data=event["html"])
