import asyncio
import json
from typing import AsyncGenerator

import redis.asyncio as redis
from django.http import StreamingHttpResponse
from django.utils.decorators import classonlymethod
from django_components import component

r = redis.from_url("redis://localhost")


def sse_message(event_id: int, event: str, data: str) -> str:
    data = data.replace("\n", "")
    return f"id: {event_id}\n" f"event: {event}\n" f"data: {data.strip()}\n\n"


class NotificationComponent(component.Component):

    @classonlymethod
    def as_live_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    template = """
    <div style="color: {{color}};" role="alert">
        <span style="font-weight: bold;">{{ title }}</span> {{ message }} 
    </div>
    """

    async def streaming_response(self, *args, **kwargs) -> AsyncGenerator[str, None]:
        async with r.pubsub() as pubsub:
            await pubsub.subscribe("notifications_channel")
            try:
                while True:
                    message = await pubsub.get_message(
                        ignore_subscribe_messages=True, timeout=1
                    )
                    if message is not None:
                        notification_data = json.loads(message["data"].decode())
                        sse_message_rendered = sse_message(
                            notification_data["id"],
                            "notification",
                            self.render(
                                {
                                    "title": notification_data["title"],
                                    "message": notification_data["message"],
                                    "color": notification_data["color"],
                                }
                            ),
                        )
                        yield sse_message_rendered
                    await asyncio.sleep(0.1)
            finally:
                await r.aclose()

    async def get(self, request, *args, **kwargs):
        return StreamingHttpResponse(
            streaming_content=self.streaming_response(),
            content_type="text/event-stream",
        )
