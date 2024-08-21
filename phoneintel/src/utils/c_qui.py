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
#     THIS NOTICE MUST REMAIN INTACT     #
#   FOR CODE REDISTRIBUTION UNDER THE    #
#           APACHE 2.0 LICENSE           #
#                                        #
##########################################

import requests
from bs4 import BeautifulSoup
import urllib.parse
from colorama import Fore, Style
from phoneintel.src.utils.const import *

class C_QuiScraper:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.base_url = 'https://www.c-qui.fr/'
        self.soup = None
        self.explanation = None
        self.spam_risk = None
        self.last_activity = None
        self.latest_report = None

    def fetch_data(self, url_:bool=True):
        url = self.base_url + urllib.parse.quote(self.phone_number)

        if url_:
            print(f"{SUB_KEY_STYLE}    - c-qui.fr URL: {VALUE_STYLE}{url}")

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except:
            pass

    def extract_info(self):
        try:
            main_div = self.soup.find('div', class_='entete-normale spemob').get_text(strip=True)
            if "l'opérateur" in main_div:
                
                self.carrier = main_div.split("l'opérateur")[1].split("Ce")[0].strip()
                self.requests = main_div.split("demandé")[1].split("foissur")[0].strip()
            
        except:
            self.requests = None
            self.carrier = None


    def get_info(self):
        try:
            self.fetch_data()
            self.extract_info()


            return {
                
                "carrier" : self.carrier,
                "requests" : self.requests
                
            }
        except Exception as e:

            return {
                
                "carrier" : None,
                "requests" : None
                
            }
        
