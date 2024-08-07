import phonenumbers
import csv
from phonenumbers import geocoder, carrier, NumberParseException
from colorama import Fore, Style
from phoneintel.src.utils.internet import is_connected
from phoneintel.src.utils.const import *
from phoneintel.src.utils.tellows import TellowsScraper
if is_connected():
    import requests
    from urllib.parse import quote


class PhoneIntel:
    
    def __init__(self, phone_number: str, lang: str = "en") -> None:
        self.phone_number = phone_number
        self.lang = lang
        self.parsed_number = None
        self.country_code = None
        self.national_number = None
        self.area = None
        self.country = None
        self.carrier_name = None
        
        self.__parse_number()
        self.__get_geolocation()
        self.__get_carrier()
        self.__print_info()
    
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
    
    def __print_country_details(self) -> None:
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
                print(f"{SUB_KEY_STYLE}    - Time Zone in Capital: {VALUE_STYLE}{time_zone}")
                print(f"{SUB_KEY_STYLE}    - Currency: {VALUE_STYLE}{country_details['Currency']}")
                
                
                if is_connected():
                
                    import requests
                    try:
                        self.__req_coordinates()
                        self.__make_req()
                        print(f"{SUB_KEY_STYLE}    - Latitude: {VALUE_STYLE}{self.__lat}")
                        print(f"{SUB_KEY_STYLE}    - Longitude: {VALUE_STYLE}{self.__lon}")
                    except:
                        pass
                    # Obtener datos de todos los países
                    try:
                        response = requests.get('https://restcountries.com/v3.1/all', timeout=5)
                        countries = response.json()

                        # Ejemplo para Argentina
                        for country in countries:
                            if country['cca2'] == str(country_details['Top Level Domain']).upper():  # 'AR' es el código ISO del país (Argentina)
                                languages = country.get('languages', {})
                                print(f"{SUB_KEY_STYLE}    - Languages: {VALUE_STYLE}")
                                for code, name in languages.items():
                                    print(f"{VALUE_STYLE}               - {name}")
                    except:
                        pass
                    
                    try:
                        
                        print(f"{SUB_KEY_STYLE}[-] TELLOWS DETAILS:")
                        init_tellows = TellowsScraper(f"+{self.country_code}{self.national_number}").get_info()
                        print(f"{SUB_KEY_STYLE}    - Tellows Score: {VALUE_STYLE}{init_tellows["score"]}")
                        type_of_call = init_tellows["type_of_call"]
                        if type_of_call != "N/A":
                            print(f"{SUB_KEY_STYLE}    - Type of Call: {VALUE_STYLE}{init_tellows["type_of_call"]}")
                        else:
                            print(f"{SUB_KEY_STYLE}    - Type of Call: {ERROR_STYLE}{'Unknown'}")
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

        import requests
        if self.__state:
            self.__api = f"https://nominatim.openstreetmap.org/search?q={quote(self.__state)},{quote(self.__country)}&format=json"
        else:
            self.__api = f"https://nominatim.openstreetmap.org/search?q={quote(self.__country)}&format=json"
    
    def __make_req(self):

        import requests
        if not self.__api:
            raise ValueError("API URL is not set. Call req_coordinates() first.")
        try:
            response = requests.get(self.__api, timeout=5)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            separator()
            print(f"[!] Error in map request")
        except requests.exceptions.RequestException as e:
            separator()
            print(f"[!] Error in map request")
        
        if response.status_code == 200:
            response_data = response.json()
            if response_data:
                self.__lon = response_data[0]["lon"]
                self.__lat = response_data[0]["lat"]
            else:
                raise ValueError("No coordinates found for the provided location.")
        else:
            separator()
            print(f"[!] Error in map request")