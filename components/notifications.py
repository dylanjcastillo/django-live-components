import asyncio
import json
from typing import AsyncGenerator
import redis.asyncio as redis
from django.http import StreamingHttpResponse
from django_components import component


@component.register("notification")
class NotificationComponent(component.Component):
    template = """
    <div style="text-color: {{color}};" role="alert">
        <span style="font-weight: bold;">{{ title }}</span> {{ message }} 
    </div>
    """


notification_component = NotificationComponent(
    registered_name="notification",
)


def sse_message(event_id: int, event: str, data: str) -> str:
    data = data.replace("\n", "")
    return f"id: {event_id}\n" f"event: {event}\n" f"data: {data.strip()}\n\n"


r = redis.from_url("redis://localhost")


async def get_component_updates(*args, **kwargs) -> AsyncGenerator[str, None]:
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
                        notification_component.render(
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


async def stream_component(request):
    return StreamingHttpResponse(
        streaming_content=get_component_updates(),
        content_type="text/event-stream",
    )
