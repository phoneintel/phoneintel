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

import phonenumbers
import csv
from phonenumbers import geocoder, carrier, NumberParseException
from colorama import Fore, Style
from json import load, JSONDecodeError
from phoneintel.src.utils.const import *
from phoneintel.src.utils.internet import is_connected
from phoneintel.src.utils.tellows import TellowsScraper
from phoneintel.src.utils.neutrino import NeutrinoAPI, NeutrinoMap
from phoneintel.src.utils.spamcalls import SpamCallsNetScraper
import requests
from urllib.parse import quote

class PhoneIntel:
    
    def __init__(self, phone_number: str, lang: str = "en", api:bool=False, api_name:str="name") -> None:
        self.phone_number = phone_number
        self.lang = lang
        self.parsed_number = None
        self.country_code = None
        self.national_number = None
        self.coordinates_json_path = COUNTRY_COORDINATES_JSON 
        self.area = None
        self.__lat = None
        self.__lon = None
        self.country = None
        self.carrier_name = None
        self.api_name = api_name.strip().lower()
        self.__parse_number()
        if not api:
            
            self.__get_geolocation()
            if not self.carrier_name:
                self.__get_carrier()
            self.__print_info()
        
        else:

            if self.api_name.strip().lower() == 'neutrino':

                self.__print_api_content()


            else:

                print(f"{Fore.RED}[ERROR] Invalid API name.")




        
    
    def __parse_number(self) -> None:
        try:
            self.parsed_number = phonenumbers.parse(self.phone_number)
            self.country_code = self.parsed_number.country_code
            self.national_number = self.parsed_number.national_number
        except NumberParseException as e:
            print(f"{Fore.RED}[ERROR] Failed to parse phone number: {e}")
            self.parsed_number = None
    
    def __get_geolocation(self) -> None:
        if self.parsed_number:
            try:
                if str(self.parsed_number.country_code).strip() == '61':
                    self.country = "Australia"
                    
                    
                    if is_connected():
                        
                        try:
                            carrier_area = TellowsScraper(self.phone_number).get_info_australia()

                            if str(self.parsed_number.national_number).strip().startswith("4") or str(self.parsed_number.national_number).strip().startswith("04"):

                                self.carrier_name = carrier_area
                                self.area = f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                            else:

                                self.area = carrier_area


                        except:
                            self.area = f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                        


                    else:
                        self.area = f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"


                else:

                    self.area = geocoder.description_for_number(self.parsed_number, self.lang) or f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                    self.country = geocoder.country_name_for_number(self.parsed_number, self.lang) or f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
            except Exception as e:
                print(f"{Fore.RED}[ERROR] Failed to get geolocation information: {e}")
                self.area = f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                self.country = f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"

    def __get_carrier(self) -> None:
        if self.parsed_number:
            try:
                self.carrier_name = carrier.name_for_number(self.parsed_number, self.lang) or f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
            except Exception as e:
                print(f"{Fore.RED}[ERROR] Failed to get carrier information: {e}")
                self.carrier_name = f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
    
    def __print_info(self) -> None:
        if self.parsed_number:
            print(f"{KEY_STYLE}[-] TARGET PHONE: {VALUE_STYLE}{self.phone_number}")
            print(f"{KEY_STYLE}[-] COUNTRY: {VALUE_STYLE}{self.country}")
            print(f"{KEY_STYLE}[-] AREA/STATE: {VALUE_STYLE}{self.area}")
            print(f"{KEY_STYLE}[-] CARRIER: {VALUE_STYLE}{self.carrier_name}")
            self.__print_country_details()
            
        else:
            print(f"{Fore.RED}[ERROR] Cannot display info, parsing failed.")
    
    def __print_country_details(self, api:bool=False, api_name:str="") -> None:
        if self.country:


                country_details = self.__get_country_details_from_csv(self.country)
                if country_details:
                    
                    time_zone = country_details['Time Zone in Capital']
                    if "_" in time_zone:
                        time_zone = time_zone.replace("_", " ")
                            
                    print(f"{SUB_KEY_STYLE}[-] COUNTRY DETAILS:")
                    print(f"{SUB_KEY_STYLE}    - Top Level Domain: {VALUE_STYLE}{country_details['Top Level Domain']}")
                    print(f"{SUB_KEY_STYLE}    - Continent: {VALUE_STYLE}{country_details['Continent']}")
                    print(f"{SUB_KEY_STYLE}    - Capital: {VALUE_STYLE}{country_details['Capital']}")
                    print(f"{SUB_KEY_STYLE}    - Time Zone: {VALUE_STYLE}{time_zone}")
                    print(f"{SUB_KEY_STYLE}    - Currency: {VALUE_STYLE}{country_details['Currency']}")
                    
                    
                    with open(COUNTRY_LANGS_JSON, 'r', encoding='utf-8') as langs:
                        countries = load(langs)

                    try:
                            for country in countries:
                                if country['cca2'] == str(country_details['Top Level Domain']).upper():
                                    languages = country.get('languages', {})
                                    print(f"{SUB_KEY_STYLE}    - Languages: {VALUE_STYLE}")
                                    for code, name in languages.items():
                                        print(f"{VALUE_STYLE}               - {name}")
                    except:
                            pass
                    if not api:
                        try:

                            self.__req_coordinates()

                            print(f"{SUB_KEY_STYLE}    - Latitude: {VALUE_STYLE}{self.__lat}")
                            print(f"{SUB_KEY_STYLE}    - Longitude: {VALUE_STYLE}{self.__lon}")

                        except:
                            pass
                    else:

                        if ',' in self.area:
                            
                            self.city = self.area.split(',')[0]
                            self.county = self.area.split(',')[1] if len(self.area.split(',')) > 1 else ''
                            self.state = self.area.split(',')[-1]

                        else:
                            self.city = self.area
                            self.county = ''
                            self.state = ''





                        data = NeutrinoMap(self.city, self.county, self.state).neutrino_req()


                        if 'locations' in data:
                                
                                if int(data['found']) != 0:
                                    try:
                                        data = data['locations']
                                        self.__lat = data[0]['latitude']
                                        self.__lon = data[0]['longitude']
                                        self.lat = self.__lat
                                        self.lon = self.__lon

                                        print(f"{SUB_KEY_STYLE}    - Latitude: {VALUE_STYLE}{self.__lat}")
                                        print(f"{SUB_KEY_STYLE}    - Longitude: {VALUE_STYLE}{self.__lon}")
                                    
                                    except:

                                        self.__req_coordinates()

                                        print(f"{SUB_KEY_STYLE}    - Latitude: {VALUE_STYLE}{self.__lat}")
                                        print(f"{SUB_KEY_STYLE}    - Longitude: {VALUE_STYLE}{self.__lon}")

                                else:
                                    self.__req_coordinates()

                                    print(f"{SUB_KEY_STYLE}    - Latitude: {VALUE_STYLE}{self.__lat}")
                                    print(f"{SUB_KEY_STYLE}    - Longitude: {VALUE_STYLE}{self.__lon}")


                        else:

                            try:

                                self.__req_coordinates()

                                print(f"{SUB_KEY_STYLE}    - Latitude: {VALUE_STYLE}{self.__lat}")
                                print(f"{SUB_KEY_STYLE}    - Longitude: {VALUE_STYLE}{self.__lon}")

                            except:
                                pass
                    

                    try:
                        separator()
                        print(f"{SUB_KEY_STYLE}[-]{Fore.BLUE} TELLOWS DETAILS:")
                        init_tellows = TellowsScraper(f"+{self.country_code}{self.national_number}").get_info()
                        print(f"{SUB_KEY_STYLE}    - Tellows Score: {VALUE_STYLE}{init_tellows['score']}")
                        type_of_call = init_tellows["type_of_call"]
                        if type_of_call != "N/A":
                            print(f"{SUB_KEY_STYLE}    - Type of Call: {VALUE_STYLE}{init_tellows['type_of_call']}")
                        else:
                            print(f"{SUB_KEY_STYLE}    - Type of Call: {ERROR_STYLE}{'Unknown'}")
                        print(f"{SUB_KEY_STYLE}[!]{Fore.CYAN} FOR REPORT A NUMBER PLEASE USE ( https://www.tellows.com/ )")
                        separator()
                    except:

                        pass

                    
                    try:

                        print(f"{SUB_KEY_STYLE}[-]{Fore.BLUE} SPAMCALLS.NET DETAILS:")
                        init_spamcalls = SpamCallsNetScraper(f"+{self.country_code}{self.national_number}").get_info()
                        if init_spamcalls['explanation'].strip() != 'Unknown' and str(init_spamcalls['explanation']).strip() != 'N/A':


                            print(f"{SUB_KEY_STYLE}    - Call Explanation: {VALUE_STYLE}{init_spamcalls['explanation']}")

                        else:

                            print(f"{SUB_KEY_STYLE}    - Call Explanation: {ERROR_STYLE}{'Unknown'}")

                        if init_spamcalls['spam_risk'] != 'Unknown' and init_spamcalls['spam_risk'].strip()  != 'N/A':

                            print(f"{SUB_KEY_STYLE}    - Spam Risk: {VALUE_STYLE}{init_spamcalls['spam_risk']}")

                        else:

                            print(f"{SUB_KEY_STYLE}    - Spam Risk: {ERROR_STYLE}{'Unknown'}")
                        

                        if init_spamcalls['last_activity'] != 'Unknown' and init_spamcalls['last_activity'].strip()  != 'N/A':

                            print(f"{SUB_KEY_STYLE}    - Last Activity: {VALUE_STYLE}{init_spamcalls['last_activity']}")

                        else:

                            print(f"{SUB_KEY_STYLE}    - Last Activity: {ERROR_STYLE}{'Unknown'}")


                        if init_spamcalls['latest_report'] != 'Unknown' and init_spamcalls['latest_report'].strip() != 'N/A':

                            print(f"{SUB_KEY_STYLE}    - Latest Report: {VALUE_STYLE}{init_spamcalls['latest_report']} UTC")

                        else:

                            print(f"{SUB_KEY_STYLE}    - Latest Report: {ERROR_STYLE}{'Unknown'}")

                        print(f"{SUB_KEY_STYLE}[!]{Fore.CYAN} FOR REPORT A NUMBER PLEASE USE ( https://spamcalls.net/en/page/report-spam-calls )")



                    except:

                        pass
                    
                    
                else:
                    print(f"{Fore.RED}[ERROR] No country details found for {self.country}")

    
    def __get_country_details_from_csv(self, country_name: str) -> dict:
        try:
            with open(COUNTRY_INFO_CSV, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    if row['Country Name'].lower() == country_name.lower():
                        return row
        except FileNotFoundError as e:
            print(f"{Fore.RED}[ERROR] CSV file not found: {e}")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Error reading CSV file: {e}")
        return None

    def __req_coordinates(self):
        if not 'Unknown' in self.area:
            
            try:
                self.__api = f"https://api.bigdatacloud.net/data/reverse-geocode-client?localityLanguage=en&locality={quote(self.area)}&countryName={quote(self.country)}"
                self.__make_req()
            except:
                self.__load_coordinates_from_json()
        else:
            self.__load_coordinates_from_json()
                    
    def __load_coordinates_from_json(self):
        try:
            with open(self.coordinates_json_path, 'r') as f:
                data = load(f)
                for entry in data["country_info"]:
                    if entry["country"].lower() == self.country.lower():
                        self.__lat = str(entry["latitude"])
                        self.__lon = str(entry["longitude"])
                        self.lon = self.__lon
                        self.lat = self.__lat
                        break
                if self.__lat is None or self.__lon is None:
                    raise ValueError(f"No coordinates found for country: {self.__country}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Coordinates JSON file not found at {self.coordinates_json_path}")
        except JSONDecodeError:
            raise ValueError("Error decoding the JSON file")
    
    def __make_req(self):
        if not self.__api and (self.__lat is None or self.__lon is None):
            raise ValueError("API URL is not set and coordinates are not found in the JSON. Call req_coordinates() first.")

        if self.__api:
            try:
                response = requests.get(self.__api, timeout=5)
                response.raise_for_status()
            except:
                pass

            if response.status_code == 200:
                response_data = response.json()
                if 'latitude' in response_data and 'longitude' in response_data:
                    self.__lon = response_data['longitude']
                    self.__lat = response_data['latitude']
                    self.lon = self.__lon
                    self.lat = self.__lat
                else:
                    raise ValueError("No coordinates found for the provided location.")
            else:
                separator()
                print(f"[!] Error in map request")

    def __print_api_content(self):

        if self.api_name == 'neutrino':
        
            try:
                
                data = NeutrinoAPI(f'+{self.parsed_number.country_code}{self.parsed_number.national_number}', str(self.parsed_number.country_code)).neutrino_req()

                if 'api-error' in data:
                    exit()


                print(f"{Fore.CYAN}[-] INFORMATION PROVIDED BY NEUTRINO API {VALUE_STYLE}https://www.neutrinoapi.com/")
                
                print(f"{KEY_STYLE}[-] TARGET PHONE: {VALUE_STYLE}{self.phone_number}")

                if 'country' in data:
                    self.country = data['country'] if data['country'] != '' else f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                    print(f"{KEY_STYLE}[-] COUNTRY: {VALUE_STYLE}{self.country}")

                if 'location' in data:
                    self.area = data['location'] if data['location'] != '' else f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                    print(f"{KEY_STYLE}[-] AREA/STATE: {VALUE_STYLE}{self.area}")

                if 'origin-network' in data:
                    self.carrier_name = data['origin-network'] if data['origin-network'] != '' else f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                    print(f"{KEY_STYLE}[-] ORIGIN CARRIER: {VALUE_STYLE}{self.carrier_name}")

                if 'current-network' in data:
                    self.carrier_name = data['current-network'] if data['current-network'] != '' else f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                    print(f"{KEY_STYLE}[-] CURRENT CARRIER: {VALUE_STYLE}{self.carrier_name}")

                if 'local-number' in data:
                    self.local_number = data['local-number'] if data['local-number'] != '' else f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                    print(f"{KEY_STYLE}[-] LOCAL NUMBER: {VALUE_STYLE}{self.local_number}")
                

                if 'number-type' in data:
                    self.number_type = data['number-type'] if data['number-type'] != '' else f"{ERROR_STYLE}Unknown{Style.RESET_ALL}"
                    print(f"{KEY_STYLE}[-] NUMBER TYPE: {VALUE_STYLE}{self.number_type}")

                
                
                try:
                    self.__print_country_details(api=True, api_name='neutrino')
                except Exception as e:
                    print(e)



            except:

                pass
