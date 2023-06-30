from bot_create import token

class Bard_create:
    def __init__(self, message: str):
        self.message = message
    def chat(self):
        from bardapi import Bard
        Bard = Bard(token=token)
        return Bard.get_answer(f"{self.message}")['content']