# -*- coding: UTF-8 -*-
import wikipedia
from fbchat import log, Client
from fbchat.models import *

class Raven(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        demand = message_object.text
        reply = wikipedia.summary(demand, sentences = 1)
        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        

        if author_id != self.uid:
           self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
           


client = Raven("username", "password")
client.listen()

