# views.py
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import StreamingHttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


async def stream_components(request):
    return StreamingHttpResponse(
        streaming_content=stream_messages(),
        content_type="text/event-stream",
    )
