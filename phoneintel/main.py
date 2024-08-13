
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

from phoneintel.src.utils import *
from time import sleep
from colorama import init, Fore, Style
import argparse
import sys
import subprocess

def open_map_info()->None:
        print(Fore.CYAN+"[!] Opening Map...\n")
        

# Constants
DORKS_TYPES = [
    "social_networks", "forums", "classifieds", "ecommerce",
    "news", "blogs", "job_sites", "pastes", "reputation", "phone_directories", "people_search",  "all"
]
init(autoreset=True)

def run_phoneintel(phone, map_true: bool = False):
    try:
        banner()
        separator()
        init = PhoneIntel(phone)

        if map_true:
            if is_connected():
                separator()
                open_map_info()
                PhoneIntelMap(init.country, init.area)
            else:
                print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

def run_phoneintel_browser(phone, map_true: bool = False):
    try:
        banner()
        separator()
        init = PhoneIntel(phone)
        PhoneIntelBrowser(init.phone_number)
        if map_true:
            if is_connected():
                separator()
                open_map_info()
                PhoneIntelMap(init.country, init.area)
            else:
                print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")


def run_phoneintel_browser_neutrino(phone, map_true: bool = False):
    try:
        banner()
        separator()
        init = PhoneIntel(phone, api=True, api_name='neutrino')
        PhoneIntelBrowser(init.phone_number)
        if map_true:
            if is_connected():
                separator()
                open_map_info()
                PhoneIntelMap(init.country, init.area)
            else:
                print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")



def run_phoneinteltext_path(input_path, map_true: bool = False):
    try:
        banner()
        numbers = PhoneIntelText(input_path).get_phone_numbers()
        for number in numbers:
            try:
                separator()
                init = PhoneIntel(number)  

                if map_true:
                    if is_connected():
                        separator()
                        open_map_info()
                        PhoneIntelMap(init.country, init.area)
                        sleep(0.5)
                    else:
                        print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
            except Exception as e:
                print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")


def run_phoneinteltext_path_neutrino(input_path, map_true: bool = False):
    try:
        banner()
        numbers = PhoneIntelText(input_path).get_phone_numbers()
        for number in numbers:
            try:
                separator()
                init = PhoneIntel(number, api=True, api_name='neutrino')  

                if map_true:
                    if is_connected():
                        separator()
                        open_map_info()
                        PhoneIntelMap(init.country, init.area)
                        sleep(0.5)
                    else:
                        print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
            except Exception as e:
                print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")



def run_phoneinteltext_string(string, map_true: bool = False):
    try:
        banner()
        numbers = PhoneIntelText(string, False).get_phone_numbers()

        for number in numbers:
            try:
                separator()
                init = PhoneIntel(number) 

                if map_true:
                    if is_connected():
                        separator()
                        open_map_info()
                        PhoneIntelMap(init.country, init.area)
                        sleep(0.3)
                    else:
                        print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
                        exit()
            except Exception as e:
                print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")



def run_phoneinteltext_string_neutrino(string, map_true: bool = False):
    try:
        banner()
        numbers = PhoneIntelText(string, False).get_phone_numbers()

        for number in numbers:
            try:
                separator()
                init = PhoneIntel(number, api=True, api_name='neutrino') 

                if map_true:
                    if is_connected():
                        separator()
                        open_map_info()
                        PhoneIntelMap(init.country, init.area)
                        sleep(0.3)
                    else:
                        print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
                        exit()
            except Exception as e:
                print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

def run_phoneinteldorking(phone, type, map_true: bool = False):
    try:
        banner()
        separator()
        init = PhoneIntel(phone)

        phone_ = init.phone_number
        dorks_banner()
        print("\n")
        dorks = PhoneIntelDorking(phone_, type)

        if map_true:
            if is_connected():
                separator()
                open_map_info()
                PhoneIntelMap(init.country, init.area)
            else:
                print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")

        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")



def run_phoneinteldorking_neutrino(phone, type, map_true: bool = False):
    try:
        banner()
        separator()
        init = PhoneIntel(phone, api=True, api_name='neutrino')

        phone_ = init.phone_number
        dorks_banner()
        print("\n")
        dorks = PhoneIntelDorking(phone_, type)

        if map_true:
            if is_connected():
                separator()
                open_map_info()
                PhoneIntelMap(init.country, init.area)
            else:
                print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")

        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")



def run_phonintelneutrino(phone, map_true):

    try:
        banner()
        separator()
        init = PhoneIntel(phone, api=True, api_name='neutrino')

        
        if map_true:
            if is_connected():
                separator()
                open_map_info()
                PhoneIntelMap(init.country, init.area, init.lat, init.lon)
            else:
                print(f"{Fore.RED}[!] NO INTERNET CONNECTION, MAP NOT AVAILABLE")
        separator()

    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
        







def install_dependencies():

    dependencies = {
        "colorama": "0.4.6",
        "phonenumbers": "8.13.42",
        "requests": "2.32.3",
        "beautifulsoup4": "4.12.3"
    }


    print("Required Dependencies:")
    for k, v in dependencies.items():
        print(k)
        
    user_input = input("Do you want to install the required dependencies? (yes/no): ").strip().lower()

    if user_input not in ['yes', 'y']:
        print("Installation of dependencies aborted by user.")
        return False

    # Comando base de pip
    pip_command = [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
    
    print(f"Updating pip...")
    try:
        subprocess.check_call(pip_command)
    except subprocess.CalledProcessError as e:
        print(f"Error updating pip: {e}")
        sys.exit(1)


    pip_command = [sys.executable, "-m", "pip", "install"]
    
    print(f"Installing pip packages...")
    for package, version in dependencies.items():
        try:

            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:

            install_command = pip_command + [f"{package}=={version}"]
            try:
                print(f"Installing {package}...")
                subprocess.check_call(install_command)
                print(f"{package} installed successfully.")
            except subprocess.CalledProcessError as e:
                print(f"Error installing {package}: {e}")
                sys.exit(1)

    print("All dependencies have been installed successfully.")
    return True



class CustomHelp:
    """Custom help formatter to create a more detailed and aesthetic help menu."""
    def __init__(self) -> None:
        print(self.format_help())
    def format_help(self):
        # Header
        help_text = "\nPhoneIntel: OSINT Tool\n"
        help_text += "=======================\n\n"
        help_text += "Description:\n"
        help_text += "  This tool processes phone numbers to perform various actions including fetching information, searching, and generating dorks.\n\n"

        # Usage
        help_text += "Usage:\n\n"
        help_text += "  phoneintel <command> [options]\n\n"

        # Commands
        help_text += "Commands:\n\n"
        help_text += "  --info    Execute info command\n"
        help_text += "  --search  Execute search command\n"
        help_text += "  --dorks   Execute dorks command\n"
        help_text += "  --browser   Execute browser command\n"
        help_text += "  --neutrino   Execute Neutrino API command\n\n"
        help_text += "  --credits   Show the credits\n\n"
        help_text += "  --disclaimer   Show the Enduser and information disclaimer\n\n"

        # Detailed Command Help
        help_text += "Detailed Command Help:\n\n"
        help_text += "  info:\n\n"
        help_text += "    phoneintel --info <phone> [--map]\n\n"
        help_text += "    Arguments:\n\n"
        help_text += "      <phone>  Phone number to be processed\n"
        help_text += "      --map    Execute map function (optional)\n\n"

        help_text += "  search:\n\n"
        help_text += "    phoneintel --search [<phone>] [--input FILE | --string TEXT] [--neutrino-api] [--map]\n\n"
        help_text += "    Arguments:\n\n"
        help_text += "      <phone>   Phone number to be processed (optional)\n"
        help_text += "      --input   Input file for search (optional)\n"
        help_text += "      --string  Search string (optional)"
        help_text += "      --map     Execute map function (optional)\n\n"
        help_text += "      --neutrino-api     Return Neutrino API information (optional)\n\n"

        help_text += "  dorks:\n\n"
        help_text += "    phoneintel --dorks <phone> --type TYPE [--neutrino-api] [--map]\n\n"
        help_text += "    Arguments:\n"
        help_text += "      <phone>  Phone number to be processed\n"
        help_text += "      --type   Type of dorks (required)\n"
        help_text += "               Valid types: {}\n".format(", ".join(DORKS_TYPES))
        help_text += "      --map    Execute map function (optional)\n\n"
        help_text += "      --neutrino-api     Return Neutrino API information (optional)\n\n"

        help_text += "  browser:\n\n"
        help_text += "    phoneintel --browser <phone> [--neutrino-api] [--map]\n\n"
        help_text += "    Arguments:\n"
        help_text += "      <phone>  Phone number to be processed\n\n"
        help_text += "      --neutrino-api     Return Neutrino API information (optional)\n\n"


        help_text += "  neutrino:\n\n"
        help_text += "    phoneintel --neutrino [<phone> | --login --id <api-id> --key <api-key> | --show]  [--map]\n\n"
        help_text += "    Arguments:\n"
        help_text += "      <phone>  Phone number to be processed\n"
        help_text += "      --login  Login in the Neutrino API\n\n"
        help_text += "          --id    API ID\n"
        help_text += "          --key   API KEY\n\n"
        help_text += "      --show   Show Neutrino API Credentials\n\n"
        help_text += "      --map    Execute map function (optional)\n\n"


        return help_text



def main():
    
    try:
        __import__("requests")
        __import__("phonenumbers")
        __import__("bs4")
        __import__("colorama")

    except Exception as e:
        print(f"[Error] {e}")
        if install_dependencies():
            
            main()

    
    parser = argparse.ArgumentParser(
        description="PhoneIntel Argument Processor",
        add_help=False
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--info', action='store_true', help='Execute info command')
    group.add_argument('--search', action='store_true', help='Execute search')
    group.add_argument('--dorks', action='store_true', help='Execute dorks command')
    group.add_argument('-h', '--help', action='store_true', help='Show help message and exit')
    group.add_argument('--neutrino', action='store_true', help='Execute Neutrino Options')
    group.add_argument('--browser', action='store_true', help='Execute Browser Search')
    group.add_argument('--credits', action='store_true', help='Show the credits')
    group.add_argument('--disclaimer', action='store_true', help='Show the disclaimer')
    

    parser.add_argument('phone', nargs='?', type=str, help='Phone number to be processed')

    search_group = parser.add_argument_group('search_group', 'Arguments for search')
    search_group.add_argument('--input', type=str, help='Input file for search')
    search_group.add_argument('--string', type=str, help='Search string')


    dorks_group = parser.add_argument_group('dorks_group', 'Arguments for dorks')
    dorks_group.add_argument('--type', type=str, help='Type of dorks')



    neutrino_group = parser.add_argument_group('neutrino_group', 'Arguments for neutrino')
    neutrino_group.add_argument('--login', action='store_true', help='Enable login mode for Neutrino')
    neutrino_group.add_argument('--show', action='store_true', help='Show Neutrino Actual Credentials')
    neutrino_group.add_argument('--id', type=str, help='Neutrino ID')
    neutrino_group.add_argument('--key', type=str, help='Neutrino Key')

    parser.add_argument('--neutrino-api', action='store_true', help='Allow Neutrino Information')
    parser.add_argument('--map', action='store_true', help='Execute map function')

    args = parser.parse_args()
    
    
        
    if args.help:
        CustomHelp()
        return


    if args.search and not (args.input or args.string or args.phone):
        parser.error('--search requires --input, --string, or phone number')
    if args.dorks and not args.type:
        parser.error('--dorks requires --type')
    if args.dorks and args.type.strip().lower() not in DORKS_TYPES:
        parser.error(f'Invalid dork type: {args.type}. Valid types are: {", ".join(DORKS_TYPES)}')

    phone_number = args.phone
    
    if args.phone:
        phone_number = str(phone_number).strip()
        if not phone_number.startswith("+"):
            separator()
            print(Fore.YELLOW+Style.BRIGHT+"[!] Not an associated country number, adding +1")
            phone_number = f"+1{phone_number}"
    

    if args.credits:

        print_credits()


    if args.disclaimer:

        display_disclaimer()


    if args.browser:
        if phone_number is None:
            parser.error('--info requires a phone')
        else:
            if args.neutrino_api:
                if check_api_list():
                    if args.map:
                        run_phoneintel_browser_neutrino(phone_number, args.map)
                    else:
                        run_phoneintel_browser_neutrino(phone_number)
                else:
                    exit()
            else:
                if args.map:
                    run_phoneintel_browser(phone_number, args.map)
                else:
                    run_phoneintel_browser(phone_number)
            
    
    if args.info:
        if phone_number is None:
            parser.error('--info requires a phone')
        else:
            if args.map:
                run_phoneintel(phone_number, args.map)
            else:
                run_phoneintel(phone_number)
    elif args.search:
        if phone_number is None and not (args.input or args.string):

            parser.error('--search requires --input or --string')
        if args.input:

            if args.neutrino_api:
                if check_api_list():
                    if args.map:
                        run_phoneinteltext_path_neutrino(args.input, args.map)
                    else:
                        run_phoneinteltext_path_neutrino(args.input)
                else:
                    exit()


            else:

                if args.map:
                    run_phoneinteltext_path(args.input, args.map)
                else:
                    run_phoneinteltext_path(args.input)
        elif args.string:


            if args.neutrino_api:
                if check_api_list():
                    if args.map:
                        run_phoneinteltext_string_neutrino(args.string, args.map)
                    else:
                        run_phoneinteltext_string_neutrino(args.string)
                exit()
            else:

                if args.map:
                    run_phoneinteltext_string(args.string, args.map)
                else:
                    run_phoneinteltext_string(args.string)

        else:
            parser.error('--search requires --input or --string')









    elif args.dorks:
        if phone_number is None:
            parser.error('--dorks requires --phone')
        else:

            if args.neutrino_api:
                if check_api_list():
                    if args.map:
                        run_phoneinteldorking_neutrino(phone_number, args.type, args.map)
                    else:
                        
                        run_phoneinteldorking_neutrino(phone_number, args.type)
                else:
                    exit()
            
            else:
                if args.map:
                    run_phoneinteldorking(phone_number, args.type, args.map)
                else:
                    
                    run_phoneinteldorking(phone_number, args.type)
        




    elif args.neutrino:


        if is_connected():
                


            if check_api_list():

                if not args.phone and not args.login and not args.show:
                    parser.error('--neutrino requires either --login (with --id and --key), --show or a phone number')

                if args.login and args.id and args.key:
                        id_ = str(args.id)

                        key_ = str(args.key)

                        NeutrinoLogin('neutrino_id', id_)
                        NeutrinoLogin('neutrino_key', key_)
                        print(f"{KEY_STYLE}[!] NEUTRINO API ID SET TO: {VALUE_STYLE}{id_}")
                        print(f"{KEY_STYLE}[!] NEUTRINO API KEY SET TO: {VALUE_STYLE}{key_}")
                elif  args.login and args.id:
                    
                        id_ = str(args.id)

                        NeutrinoLogin('neutrino_id', id_)
                        print(f"{KEY_STYLE}[!] NEUTRINO API ID SET TO: {VALUE_STYLE}{id_}")

                elif  args.login and args.key:
                    
                        key_ = str(args.key)

                        NeutrinoLogin('neutrino_key', key_)
                        print(f"{KEY_STYLE}[!] NEUTRINO API KEY SET TO: {VALUE_STYLE}{key_}")

                if args.phone and not args.login and not args.show:

                    if args.map:
                        run_phonintelneutrino(phone_number, map_true=True)

                    else:
                        run_phonintelneutrino(phone_number, map_true=False)


                if args.show and not args.login and not args.phone:

                    api_cred_show('neutrino')



            else:

                exit()
            
        else:
            print(f"{Fore.RED}[ERROR] NO INTERNET CONNECTION, USE --info FOR OFFLINE SEARCHS")

    
    
    
if __name__ == "__main__":
  
    main()
    
