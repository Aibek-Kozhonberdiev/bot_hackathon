import asyncio
from bardapi import Bard
from config import TOKEN

class BardСhat:
    def __init__(self, message: str):
        self.message = message

    async def chat(self):
        bard = Bard(token=TOKEN)
        response = await asyncio.to_thread(bard.get_answer, self.message)
        return response['content']

async def bard_chat(message) -> str:
    creator = BardСhat(message)
    response = await creator.chat()
    return response