import json
from django.utils import timezone
from .models import Message, User, Channel
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

def show_attr(cls):
    print([i for i in cls.__dict__.keys() if i[:1] != '_'])

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        id = self.scope['url_route']['kwargs']['id']
        channel = Channel.objects.get(id=id)
        channel_messages = Message.objects.filter(channel_id=channel)
        for message in channel_messages:
            if message.owner_id != self.scope['user']:
                message.received = True
                message.save()
        self.room_group_name = "channel" + str(id)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_owner = self.scope['user']
        owner = User.objects.get(username=message_owner)
        owner_id = owner.id
        channel = Channel.objects.get(id=self.scope['url_route']['kwargs']['id'])
        created = str(timezone.now())

        message_id = Message.objects.create(owner_id=owner, channel_id=channel, value=message).id
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'created': created,
                'message_owner': str(message_owner),
                'message_id': message_id,
                'owner_id': owner_id,
            }
        )

    def disconnect(self, close_code):
        print('disconnected')
    
    def chat_message(self, event):
        message = event['message']
        created = event['created']
        message_owner = event['message_owner']
        message_id = event['message_id']
        received = False
        if str(self.scope['user']) != str(message_owner):
            msg = Message.objects.get(id=message_id)
            msg.received = True
            msg.save()
            received = True

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message,
            'created': created,
            'message_owner': message_owner,
            'received': received,
        }))
