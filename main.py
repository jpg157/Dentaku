from fbchat import log, Client
import os
import commands
from fbchat import MessageReaction


# Subclass fbchat.Client and override required methods
class dentaku_bot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        command = str(message_object.text).replace("!", "").split(" ")
        parameters = {
            "user": command[1:],
            "author_id": author_id,
            "message_object": message_object,
            "thread_id": thread_id,
            "thread_type": thread_type
        }
        command = command[0]
        try:
            module = __import__(command)
            my_class = getattr(module, command)
            instance = my_class(parameters)
        except:

            print("Command not found.")


client = dentaku_bot(os.getenv('EMAIL'), os.getenv('PASSWORD'))
client.listen()
