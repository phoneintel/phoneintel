import urllib.parse
from phonenumbers import parse, geocoder
from colorama import Fore, init
from json import load, JSONDecodeError
from phoneintel.src.utils.const import DORKS_JSON

init(autoreset=True)

class PhoneIntelDorking:
    
    def __init__(self, target: str, dork_type: str = "social_networks") -> None:
        self.__target = target
        self.__type = dork_type.lower().strip()
        phonenumbers_init = parse(self.__target)
        self.__country_code = phonenumbers_init.country_code
        self.__national_number = phonenumbers_init.national_number
        self.__country = geocoder.country_name_for_number(phonenumbers_init, "en")
        self.__dorks_base = self.__json_to_dict(DORKS_JSON)
        self.__dorks_ready = []
        self.__process_dorks()
        self.__print_dorks()
        
    def __process_dorks(self) -> None:
        dork_categories = ["social_networks", "forums", "classifieds", "ecommerce", "news", "blogs", "job_sites", "pastes", "reputation", "phone_directories", "people_search"]

        if self.__type in dork_categories:
            self.__replace_placeholders(self.__dorks_base[self.__type])
        elif self.__type == "all":
            for category in dork_categories:
                self.__replace_placeholders(self.__dorks_base[category])
                
    def __replace_placeholders(self, dork_list: list) -> None:
        for dork in dork_list:
            dork = dork.replace('{phone}', str(self.__target))
            dork = dork.replace('{national_phone}', str(self.__national_number))
            dork = dork.replace('{country}', str(self.__country))
            dork = dork.replace('{country_code}', str(self.__country_code))
            self.__dorks_ready.append(dork)
    
    def __json_to_dict(self, json_path: str) -> dict:
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                return load(file)
        except FileNotFoundError:
            print(f"Error: El archivo {json_path} no se encontró.")
        except JSONDecodeError:
            print(f"Error: El archivo {json_path} no es un JSON válido.")
        return {}

    def __print_dorks(self) -> None:
        base_url = "https://www.google.com/search?q="
        type = self.__type
        if "_" in type:
            type = type.replace("_", " ")
        type = type.capitalize()
        for counter, dork in enumerate(self.__dorks_ready, start=1):
            encoded_dork = urllib.parse.quote(dork)
            full_url = f"{base_url}{encoded_dork}"
            print(Fore.YELLOW + f"{type} Dork {counter}: " + Fore.CYAN + full_url)
            print("\n")
