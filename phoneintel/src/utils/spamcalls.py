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
#           APACHE 2.0 LICENSE           #
#           GPL-3.0 license              #
#                                        #
##########################################

import requests
from bs4 import BeautifulSoup
import urllib.parse
from colorama import Fore, Style
from phoneintel.src.utils.const import *

class SpamCallsNetScraper:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.base_url = 'https://spamcalls.net/en/number/'
        self.soup = None
        self.explanation = None
        self.spam_risk = None
        self.last_activity = None
        self.latest_report = None

    def fetch_data(self, url_:bool=True):
        url = self.base_url + urllib.parse.quote(self.phone_number)

        if url_:
            print(f"{SUB_KEY_STYLE}    - spamcalls.net URL: {VALUE_STYLE}{url}")

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except:
            pass

    def extract_explanation(self):
        try:
            main_div = self.soup.find('div', class_='well zusammenfassung-v2 row').get_text(strip=True)
            self.explanation = main_div.split('explanation')[1].split(':')[0].strip()
        except:
            self.explanation = 'N/A'

    def extract_spam_risk(self):
        try:
            main_div = self.soup.find('div', class_='well zusammenfassung-v2 row').get_text(strip=True)
            spam_risk = main_div.split('Spam-Risk')[1].split('Country')[0].replace('(', ' (')
            self.spam_risk = spam_risk.strip()
        except:
            self.spam_risk = 'N/A'

    def extract_last_activity(self):
        try:
            main_div = self.soup.find('div', class_='well zusammenfassung-v2 row').get_text(strip=True)
            self.last_activity = main_div.split('days')[1].split('phone')[0].strip()
        except:
            self.last_activity = 'N/A'

    def extract_latest_report(self):
        try:
            main_div = self.soup.find('div', class_='well zusammenfassung-v2 row').get_text(strip=True)
            self.latest_report = main_div.split('Latest User Report')[1].split('people')[0].strip()
        except:
            self.latest_report = 'N/A'

    def get_info(self):
        try:
            self.fetch_data()
            self.extract_explanation()
            self.extract_spam_risk()
            self.extract_last_activity()
            self.extract_latest_report()

            return {
                'phone_number': self.phone_number,
                'explanation': self.explanation,
                'spam_risk': self.spam_risk,
                'last_activity': self.last_activity,
                'latest_report': self.latest_report
            }
        except Exception as e:
            print(f"{Fore.RED}Error while fetching data: {e}{Style.RESET_ALL}")
            return {
                'phone_number': self.phone_number,
                'explanation': "Unknown",
                'spam_risk': "Unknown",
                'last_activity': "Unknown",
                'latest_report': "Unknown"
            }

    def set_phone_number(self, new_number):
        self.phone_number = new_number
