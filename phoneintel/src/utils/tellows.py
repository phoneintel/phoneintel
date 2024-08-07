import requests
from bs4 import BeautifulSoup
import urllib.parse
from colorama import Fore, Style
from phoneintel.src.utils.const import *

class TellowsScraper:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.base_url = 'https://www.tellows.com/num/'
        self.soup = None
        self.score = None
        self.type_of_call = None

    def fetch_data(self):
        url = self.base_url + urllib.parse.quote(self.phone_number)
        print(f"{SUB_KEY_STYLE}    - Tellows URL: {VALUE_STYLE}{url}")
        
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def extract_score(self):
        try:
            score_image = self.soup.find('div', {'id': 'tellowsscore'}).find('img')
            self.score = score_image['alt'].split(': Score ')[1].strip() if score_image else 'N/A'
        except:
            self.score = 'N/A'

    def extract_type_of_call(self):
        try:
            self.type_of_call = self.soup.find('b', text='Types of call:').find_next_sibling(text=True).strip()
        except:
            self.type_of_call = 'N/A'

    def get_info(self):
        try:
            self.fetch_data()
            self.extract_score()
            self.extract_type_of_call()
            return {
                'phone_number': self.phone_number,
                'score': self.score,
                'type_of_call': self.type_of_call
            }
        except:
            return {
                'phone_number': self.phone_number,
                'score': "Unknow",
                'type_of_call': "Unknow"
            }

    def set_phone_number(self, new_number):
        self.phone_number = new_number

