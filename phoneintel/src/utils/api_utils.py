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

from os import path
from phoneintel.src.utils.const import USER_API_KEYS, KEY_STYLE, VALUE_STYLE
from json import dump, load
from colorama import Fore
api_list_params = {

    "neutrino_id" : "",
    "neutrino_key": ""


}

def check_api_list()->bool:
    try:
        if path.exists(USER_API_KEYS):

            return True
        
        else:

            try:
                with open(USER_API_KEYS, 'w', encoding='utf-8') as file:
                    dump(api_list_params, file, indent=4)
                    
                return True
            
            except:
                print(f"{Fore.RED}[ERROR] Can't create api_list.json in {USER_API_KEYS}")
                return False
    except:

        print(f"{Fore.RED}[ERROR] Error reading api_list.json")
        return False




def api_cred_show(api_name:str):
        
    try:
        try:
            with open(USER_API_KEYS, 'r', encoding='utf-8') as file:
                data = load(file)
        except:
            print(f"{Fore.RED}[ERROR] Users API File connot be opened")
            print(f"{Fore.RED}[!] Delete the file {USER_API_KEYS} and reinstall phoneintel")
            print(f"{Fore.RED}  [!] pip uninstall phoneintel")
            print(f"{Fore.RED}  [!] pip install phoneintel")
        for k,v in data.items():

            if str(k).startswith(api_name):

                print(f"{KEY_STYLE}[!] {str(k).upper()}: {VALUE_STYLE}{str(v)}")

    except:

        print(f"{Fore.RED}[ERROR] The credentials cannot be displayed")
