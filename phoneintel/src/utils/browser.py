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
from phoneintel.src.utils.const import USER_AGENTS, browser_search, SUB_KEY_STYLE, VALUE_STYLE, separator
from phoneintel.src.utils.internet import is_connected
import random
from colorama import Fore


class PhoneIntelBrowser:
    def __init__(self, phonenumber:str):
        self.user_agents_file = USER_AGENTS
        self.user_agent = self._load_random_user_agent()
        self.headers = {
            "User-Agent": self.user_agent
        }
        if is_connected():
            self.get_links(phonenumber)
        else:
            separator()
            print(f"{Fore.RED}[!] NO INTERNET CONNECTION TO RUN BROWSER SEARCH")
    
    def _load_random_user_agent(self):
        try:
            with open(self.user_agents_file, 'r') as file:
                user_agents = file.readlines()
            user_agents = [ua.strip() for ua in user_agents if ua.strip()]
            if user_agents:
                return random.choice(user_agents)
            else:
                raise ValueError("The User-Agents file is empty.")
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.user_agents_file}")
        except Exception as e:
            raise RuntimeError(f"Error loading User-Agents: {e}")

    def get_links(self, phone_number):
        urls = []
        try:
            phone_number = phone_number.split("+")[1]
            response = requests.get(f'https://duckduckgo.com/html/?q={phone_number}', headers=self.headers)
            response.raise_for_status()  # Check if the request was successful
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all("a", class_="result__url", href=True)
            
            for link in links:
                href = link['href']
                if href:
                    urls.append(href)
                else:
                    urls.append("No URL")
        except:
            pass
        
        
        browser_search()
        print(f"{SUB_KEY_STYLE}[-] USER AGENT: {VALUE_STYLE}{self.user_agent}")
        separator()

        for url in urls:

            print(f"{SUB_KEY_STYLE}[!] {VALUE_STYLE} {url}")
