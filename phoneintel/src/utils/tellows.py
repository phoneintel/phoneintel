#!/usr/bin/env python3
##########################################
#                                        #
#      CREATED BY THE PHONEINTEL TEAM    #
#                                        #
##########################################
#                                        #
# ALL INFORMATION IS SOURCED EXCLUSIVELY #
#      FROM OPEN SOURCE AND PUBLIC       #
#               RESOURCES                #
#                                        #
#   THIS SOFTWARE IS PROVIDED "AS IS",   #
#   WITHOUT WARRANTY OF ANY KIND,        #
#   EXPRESS OR IMPLIED, INCLUDING BUT    #
#   NOT LIMITED TO THE WARRANTIES OF     #
#   MERCHANTABILITY, FITNESS FOR A       #
#   PARTICULAR PURPOSE AND               #
#   NONINFRINGEMENT.                     #
#                                        #
#   IN NO EVENT SHALL THE AUTHORS OR     #
#   COPYRIGHT HOLDERS BE LIABLE FOR ANY  #
#   CLAIM, DAMAGES OR OTHER LIABILITY,   #
#   WHETHER IN AN ACTION OF CONTRACT,    #
#   TORT OR OTHERWISE, ARISING FROM,     #
#   OUT OF OR IN CONNECTION WITH THE     #
#   SOFTWARE OR THE USE OR OTHER         #
#   DEALINGS IN THE SOFTWARE.            #
#                                        #
#     THIS NOTICE MUST REMAIN INTACT     #
#   FOR CODE REDISTRIBUTION UNDER THE    #
#           GPL-3.0 license              #
#                                        #
##########################################

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

    def fetch_data(self, url_:bool=True):

        url = self.base_url + urllib.parse.quote(self.phone_number)

        if url_:
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


    def get_info_australia(self):
        try:
            self.fetch_data(url_=False)
            result = self.extract_australian_country()
            return result
        except Exception as e:
            return e

    def extract_australian_country(self):

        try:
            country = str(self.soup.find('div', class_='col-lg-9').find('h1'))

            

            if 'from' in country:
                country = country.split('from')[1]

            if 'of' in country:
                country = country.split('of')[1]
            
            if '</h1>' in country:
                country = country.replace("</h1>", "")

            if country.strip().startswith('<h1>'):

                country = 'Unknown'

            return country.strip()
            
        except Exception as e:

            return 'Unknown'
