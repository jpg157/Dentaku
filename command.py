from fbchat import Client
class Command:

    def __init__(self, parameters, client:Client):
        self.user_params = parameters['user']
        self.author_id = parameters['author_id']
        self.message_object = parameters['message_object']
        self.thread_id = parameters['thread_id']
        self.thread_type = parameters['thread_type']
        self.client = client
        self.author = self.client.fetchUserInfo(self.author_id)[self.author_id]

        self.markAsDelivered(self.thread_id, self.message_object.uid)
        self.markAsRead(self.thread_id)

        self.run()

    def run(self):
        print("Running abstract command...")
        return
