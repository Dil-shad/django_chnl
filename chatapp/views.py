from django.shortcuts import render
import threading
# Create your views here.
from channels.layers import get_channel_layer

async def index(request):
    print(threading.get_native_id())
    channel_layer = get_channel_layer()
    await channel_layer.group_send("chat_a1", {
                    'type': 'chat_message',
                    'message': "index-notification",
                    })
    return render(request, 'index.html')


def room(request, room_name):
    return render(request, 'room.html', { 'room_name': room_name})
