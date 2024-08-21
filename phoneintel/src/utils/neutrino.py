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


from json import load, dump
from phoneintel.src.utils.const import USER_API_KEYS
from colorama import Fore
import requests


class NeutrinoAPI:

    def __init__(self, phonenumber:str, country_code:str) -> None:


                
        with open(USER_API_KEYS, 'r') as file:

            neutrino_api = load(file)

        self.__api_id = neutrino_api['neutrino_id']
        self.__api_key = neutrino_api['neutrino_key']

        if self.__api_key == '':
            print(f"{Fore.RED}[ERROR] Please set the Neutrino API KEY {Fore.CYAN} ( phoneintel --neutrino --login --id <id> --key <api-key> )")
            print(f"{Fore.YELLOW}[!] Or Create an account at: {Fore.CYAN} https://www.neutrinoapi.com/signup/")
            exit()

        elif self.__api_id == '':
            print(f"{Fore.RED}[ERROR] Please set the Neutrino API ID {Fore.CYAN} ( phoneintel --neutrino --login --id <id> --key <api-key> )")
            print(f"{Fore.YELLOW}[!] Or Create an account at: {Fore.CYAN} https://www.neutrinoapi.com/signup/")
            exit()

        else:
            
            self.phonenumber = phonenumber
            self.country_code = country_code
            self.url = 'https://neutrinoapi.net/hlr-lookup'
            self.headers = {

                'User-ID': str(self.__api_id),
                'API-Key': str(self.__api_key)
            }
            self.data = {

                'number': self.phonenumber,
                'country-code': self.country_code

            }


    def neutrino_req(self):

        try:
            self.api_request = requests.post(self.url, headers=self.headers, data=self.data)
            self.response = self.api_request.json()

            if 'api-error' in self.response:
                if str(self.response['api-error-msg']).strip().lower() == "ACCESS DENIED. USER ID OR API KEY INVALID".strip():
                    print(f"{Fore.RED}[NEUTRINO API ERROR] {self.response['api-error-msg']}")
                    print(f"{Fore.YELLOW}[!] Please set again the Neutrino API KEY or API ID {Fore.CYAN} ( phoneintel --neutrino --login --id <id> --key <api-key> )")
                    print(f"{Fore.YELLOW}[!] Or Create an account at: {Fore.CYAN} https://www.neutrinoapi.com/signup/")
                elif str(self.response['api-error-msg']).strip().upper() == "FREE PLAN LIMIT EXCEEDED".strip():

                    print(f"{Fore.RED}[NEUTRINO API ERROR] {self.response['api-error-msg']}")
                    print(f"{Fore.YELLOW}[!] Please wait 24hs or Buy a plan at {Fore.CYAN} ( https://www.neutrinoapi.com/plans/ )")
                elif str(self.response['api-error-msg']).strip().upper() == "ACCOUNT OR IP BANNED".strip():

                    print(f"{Fore.RED}[NEUTRINO API ERROR] {self.response['api-error-msg']}")
                    print(f"{Fore.YELLOW}[!] Please contact to support {Fore.CYAN} ( https://www.neutrinoapi.com/contact-us/ )")
            
            else:
                return self.response
            
            
        except:
            if not self.response['api-error-msg'].strip().upper() == "ACCESS DENIED. USER ID OR API KEY INVALID".strip().lower():
                print(f"{Fore.RED}[ERROR] Fail in API Request")



class NeutrinoMap:
    def __init__(self, city:str, county:str='', state:str='') -> None:


        with open(USER_API_KEYS, 'r') as file:

            neutrino_api = load(file)

        self.__api_id = neutrino_api['neutrino_id']
        self.__api_key = neutrino_api['neutrino_key']

        if self.__api_key == '':
            print(f"{Fore.RED}[ERROR] Please set the Neutrino API KEY {Fore.CYAN} ( phoneintel --neutrino --login --id <id> --key <api-key> )")
            print(f"{Fore.YELLOW}[!] Or Create an account at: {Fore.CYAN} https://www.neutrinoapi.com/signup/")
            exit()

        elif self.__api_id == '':
            print(f"{Fore.RED}[ERROR] Please set the Neutrino API ID {Fore.CYAN} ( phoneintel --neutrino --login --id <id> --key <api-key> )")
            print(f"{Fore.YELLOW}[!] Or Create an account at: {Fore.CYAN} https://www.neutrinoapi.com/signup/")
            exit()

        else:
            
            self.city = city if city != '' else ''
            self.state = state if state != '' else ''
            self.county = county if county != '' else ''
            self.url = 'https://neutrinoapi.net/geocode-address'
            self.headers = {

                'User-ID': str(self.__api_id),
                'API-Key': str(self.__api_key)
            }
            self.data = {
                
                'city': str(self.city),
                'county': str(self.county),
                'state': str(self.state),
                'language-code' : 'en',
            }


    def neutrino_req(self):

        try:
            self.api_request = requests.post(self.url, headers=self.headers, data=self.data)
            self.response = self.api_request.json()
            if 'api-error' in self.response:
                print(f"{Fore.RED}[NEUTRINO API ERROR] {self.response['api-error-msg']}")
                exit()
            return self.response
        except:
            if not self.response['api-error-msg'].strip().lower() == "ACCESS DENIED. USER ID OR API KEY INVALID".strip().lower():
                print(f"{Fore.RED}[ERROR] Fail in API Request")



class NeutrinoLogin:

    def __init__(self, key, value) -> None:
        
        self.key = key
        self.value = value
        self.change_value()

    def change_value(self):

        try:

            with open(USER_API_KEYS, 'r', encoding='utf-8') as file:

                self.data = load(file)

            if self.key in self.data:

                self.data[self.key] = self.value

            

            with open(USER_API_KEYS, 'w', encoding='utf-8') as file:
                dump(self.data, file, indent=4)

        
        except FileExistsError:

            print(f"[!] api_list.json not found")

        except:
            print(f"[!] Neutrino Login Fail")



