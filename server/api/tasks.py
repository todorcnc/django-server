# This file is related to celery
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def add(x, y):
    for i in range(100):
        # Send Progress 
        # This how you end messages over the websocket with django channels
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": f"{i}"
            }
        )
    return x + y