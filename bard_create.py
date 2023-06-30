# Libraries Imported
from bot_create import token

class Bard_create: 
    def __init__(self, message: str): # The Bard_create class is an instance of the Bard language model. It has a constructor (__init__) that takes a message parameter.
        self.message = message
    def chat(self): # The chat() method is used to interact with the Bard model and retrieve its response based on the provided message. It utilizes the Bard class from the bardapi module.
        from bardapi import Bard
        Bard = Bard(token=token)
        return Bard.get_answer(f"{self.message}")['content']