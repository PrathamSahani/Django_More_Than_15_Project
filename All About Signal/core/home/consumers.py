from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync



class Test(WebsocketConsumer):
    
    def connect(self):
        self.room_name = "test_consumer"
        self.group_name = "test_cosnumer_group" 
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.room_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status': "connected"}))
        
        
        
    
    def receive(self):
        pass
    
    def disconnect(self):
        pass
    
    
    