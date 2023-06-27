import requests
from bs4 import BeautifulSoup

class BotText:
    def __init__(self) -> None:
        pass
    def text_welcome(self):
        with open("~/text_bot/text_welcome.tex", "r") as f:
            self.start_text = f.read()
        return self.start_text

class Connect:
    def __init__(self, url: str):
        self.url = url
        
    def req(self):
        try:
            self.r = requests.get(self.url)
            return self.r.content
        except requests.ConnectionError as e:
            print(e)

# bot = BotText()
# print(bot.text_welcome())

# Здесь будет парсер