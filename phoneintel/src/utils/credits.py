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

from colorama import Fore,Style
from phoneintel.src.utils.const import DISCLAIMER, separator



def print_credits()->None:


    print(f'''{Fore.BLUE}
-------------------------------------------

        ╔═╗╦ ╦╔═╗╔╗╔╔═╗╦╔╗╔╔╦╗╔═╗╦  
        ╠═╝╠═╣║ ║║║║║╣ ║║║║ ║ ║╣ ║  
        ╩  ╩ ╩╚═╝╝╚╝╚═╝╩╝╚╝ ╩ ╚═╝╩═╝
        
-------------------------------------------   {Fore.YELLOW}{Style.BRIGHT}
PhoneIntel{Style.NORMAL} is a tool that processes phone 
numbers to perform various actions, including 
fetching information, searching, and generating dorks.

{Fore.YELLOW}[*] {Fore.CYAN}{Style.BRIGHT}PhoneIntel{Style.NORMAL} use information obtained from:

    {Fore.BLUE}[!] {Fore.GREEN}{Style.BRIGHT}spamcalls.net {Style.NORMAL}{Fore.CYAN}( https://spamcalls.net )

    {Fore.BLUE}[!] {Fore.GREEN}{Style.BRIGHT}tellows.com {Style.NORMAL}{Fore.CYAN}( https://tellows.com )

{Fore.YELLOW}[*] {Fore.CYAN}{Style.BRIGHT}PhoneIntel{Style.NORMAL} allow to use the API of Neutrino API:

    {Fore.BLUE}[!] {Fore.GREEN}{Style.BRIGHT}NEUTRINO API {Style.NORMAL}{Fore.CYAN}( https://www.neutrinoapi.com )
{Fore.YELLOW}
ALL INFORMATION PROVIDED BY tellows, spamcalls
AND Neutrino API IS ENTIRELY OWNED BY THEM
PhoneIntel ONLY SHOW THE INFORMATION OBTAINED
FROM PUBLIC CONTENT AND APIs
{Fore.RED}
-------------------------------------------
{Fore.RED}{Style.BRIGHT}                DISCLAIMER{Style.NORMAL}
-------------------------------------------
THE DEVELOPERS AND CONTRIBUTORS OF PHONEINTEL
ASSUME NO RESPONSIBILITY OR LIABILITY FOR ANY
ACTIONS OR RESULTS ARISING FROM USE OR MISUSE
OF THIS TOOL. USERS ARE SOLELY RESPONSIBLE FOR
ANY AND ALL ILLEGAL AND NO ETHICAL CONSEQUENCES
RESULTING FROM THEIR ACTIONS WHILE USING PHONEINTEL

{Style.BRIGHT}[!]{Style.NORMAL} RESPECT PRIVACY
{Style.BRIGHT}[!]{Style.NORMAL} NOT USE FOR ANY ILLEGAL ACTIVITY
{Style.BRIGHT}[!]{Style.NORMAL} PHONEINTEL IS MADE FROM PUBLIC INFORMATION
-------------------------------------------
{Fore.YELLOW}[*] {Style.NORMAL}LICENSED UNDER Apache-2.0 license{Fore.BLUE}
-------------------------------------------
{Fore.RESET}''')
    



def display_disclaimer()->None:

    with open(DISCLAIMER, 'r', encoding="utf-8") as file:
        separator()
        for line in file:
            print(line)
        separator()
