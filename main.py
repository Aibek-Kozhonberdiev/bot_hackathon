import requests
from bs4 import BeautifulSoup
class Requests:
    def __init__(self, url: str):
        self.url = url
        
    def req(self):
        try:
            self.r = requests.get(self.url)
            return self.r.content
        except requests.ConnectionError as e:
            print(e)
# Здесь будет парсер