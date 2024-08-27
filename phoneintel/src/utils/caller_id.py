#!/usr/bin/env python3
##########################################
#                                        #
#      CREATED BY THE PHONEINTEL TEAM    #
#                                        #
##########################################
# ALL INFORMATION IS SOURCED EXCLUSIVELY #
#    THROUGH RAPIDAPI, A REPUTABLE API   #
# AGGREGATOR. WHILE RAPIDAPI, IS TRUSTLY #
#  WE DO NOT HAVE KNOWLEDGE OF OR CONTROL#
#  OVER THE METHODS USED BY THE API      #
#  PROVIDERS TO OBTAIN THE DATA.         #
#                                        #
#  THIS SOFTWARE SIMPLY AUTOMATES API    #
#  REQUESTS. WE ARE NOT RESPONSIBLE FOR  #
#  HOW THE USER UTILIZES THIS SOFTWARE,  #
#  NOR FOR ANY ACTIONS OR CONSEQUENCES   #
#  ARISING FROM ITS USE.                 #
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
from phoneintel.src.utils.const import *
from phoneintel.src.utils.api_utils import check_api_list
from phoneintel.src.utils.const import USER_API_KEYS
from json import load

class CallerIDAPI:
    def __init__(self, national_number:str=None, country_code:str=None) -> None:
    
        check_api_list()
        with open(USER_API_KEYS, 'r') as file:

            caller_id_api = load(file)

        self.__api_key = caller_id_api['caller_id_key']
        self.url = "https://caller-id4.p.rapidapi.com/search-mobile"
        self.querystring = {"q": f"{national_number}", "countryCode": f"{country_code}", "type": "4", "encoding": "json"}

        self.headers = {
            'x-rapidapi-key': self.__api_key,
            'x-rapidapi-host': "caller-id4.p.rapidapi.com"
        }

        self.info = None
        self.name = None
        self.gender = None
    
    def make_req(self):
            
            response = requests.get(url=self.url, headers=self.headers, params=self.querystring).json()
            if "message" in response:
                
                self.name = f"{ERROR_STYLE}Unknown"
                self.info = f"{ERROR_STYLE}Unknown"
            
            else:
                
                self.name = response["data"][0]["name"] if response["data"][0]["name"] else f"{ERROR_STYLE}Unknown"
                
                self.info = response["data"][0]["internetAddresses"][0]["id"] if response["data"][0]["internetAddresses"][0]["id"] else f"{ERROR_STYLE}Unknown"

    def detect_gender(self):
        
        if " " in str(self.name):
            print("cool")
            if len(str(self.name).split(" ")) > 1:
                
                name = str(self.name).split(" ")[0]
                
            else:
                
                pass
        
        
        else:
            pass
        
        try:
            url = f"https://api.genderize.io?name={name}"
            response = requests.get(url=url).json()

            self.gender = str(f"{response["gender"]} in {int(response["probability"])*100}%").capitalize()
        except:
            pass
        
        
        
        
    def run(self):
        try:
            self.make_req()
            if self.name != f"{ERROR_STYLE}Unknown":
                try:
                    self.detect_gender()
                    return {
                        
                        "name":self.name,
                        "info":str(self.info),
                        "gender":str(self.gender)
                        
                    }
                except:
                    return {
                        
                        "name":self.name,
                        "info":str(self.info),
                        "gender": f"{ERROR_STYLE}Unknown"
                        
                    }
            else:
                return {
                        
                        "name":self.name,
                        "info":str(self.info),
                        "gender": f"{ERROR_STYLE}Unknown"
                        
                    }
        except:
            return None
            
