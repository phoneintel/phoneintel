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

from colorama import Fore, Style
from os import path
from time import sleep

BANNER = f'''{Fore.BLUE}
-------------------------------------------

        ╔═╗╦ ╦╔═╗╔╗╔╔═╗╦╔╗╔╔╦╗╔═╗╦  
        ╠═╝╠═╣║ ║║║║║╣ ║║║║ ║ ║╣ ║  
        ╩  ╩ ╩╚═╝╝╚╝╚═╝╩╝╚╝ ╩ ╚═╝╩═╝
        
-------------------------------------------'''
BANNER_2 = f'''{Fore.BLUE}
-------------------------------------------
            ╔╦╗╔═╗╦═╗╦╔═╔═╗
             ║║║ ║╠╦╝╠╩╗╚═╗
            ═╩╝╚═╝╩╚═╩ ╩╚═╝
-------------------------------------------'''
BANNER_3 = f''' {Fore.BLUE}
-------------------------------------------
          ╔╗ ╦═╗╔═╗╦ ╦╔═╗╔═╗╦═╗
          ╠╩╗╠╦╝║ ║║║║╚═╗║╣ ╠╦╝
          ╚═╝╩╚═╚═╝╚╩╝╚═╝╚═╝╩╚═
-------------------------------------------'''
SUB_KEY_STYLE = Fore.YELLOW + Style.BRIGHT
KEY_STYLE = Fore.YELLOW + Style.BRIGHT
VALUE_STYLE = Fore.GREEN + Style.NORMAL
ERROR_STYLE = Fore.RED + Style.BRIGHT
MAIN_PATH = path.normpath(__file__+"/../..")
MAIN_PATH_2 = path.normpath(__file__+"/../../..")
COUNTRY_INFO_CSV = path.join(MAIN_PATH, "resources", "countries", "countries.csv")
USER_AGENTS = path.join(MAIN_PATH, "resources", "user_agents", "agents.txt")
DORKS_JSON = path.join(MAIN_PATH, "resources", "dorks", "dorks.json")
COUNTRY_COORDINATES_JSON = path.join(MAIN_PATH, "resources", "countries", "country_coordinates.json")
COUNTRY_LANGS_JSON = path.join(MAIN_PATH, "resources", "countries", "countries_langs.json")
USER_API_KEYS = path.join(MAIN_PATH, "resources", "user", "api_list.json")
DISCLAIMER = path.join(MAIN_PATH_2, "DISCLAIMER.txt")
def separator()->None:
    
    print(Fore.BLUE+"-------------------------------------------")
    
def banner()->None:
        print(BANNER)
        sleep(0.3)
        print(Fore.RESET+"[!] VERSION 1.1.0\n")
        sleep(0.3)
        print("[!] GITHUB https://github.com/phoneintel/phoneintel\n")
        sleep(0.3)
        print("[!] LICENSED UNDER Apache-2.0 license")
        sleep(0.3)
        
def dorks_banner()->None:
        print(BANNER_2)
        sleep(0.3)


def invalid_path()->None:
        print(Fore.RED+"[!] Invalid Path...\n")



def browser_search()->None:
        print(BANNER_3)
        sleep(0.3)
        print(Fore.YELLOW+f"[-]{Fore.CYAN} SEARCHING IN DUCKDUCKGO")

