
#!/usr/bin/env python3
from phoneintel.src.utils import *
from time import sleep
from colorama import init, Fore, Style
import argparse
import sys
import subprocess


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

        if map_true and "Unknown" not in init.area:
            separator()
            open_map()
            PhoneIntelMap(init.country, init.area)
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
                init = PhoneIntel(number)  # Cambiado de phone a number

                if map_true and "Unknown" not in init.area:
                    separator()
                    open_map()
                    PhoneIntelMap(init.country, init.area)
                    sleep(0.5)
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
                init = PhoneIntel(number)  # Cambiado de phone a number

                if map_true and "Unknown" not in init.area:
                    separator()
                    open_map()
                    PhoneIntelMap(init.country, init.area)
                    sleep(0.3)
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

        if map_true and "Unknown" not in init.area:
            separator()
            open_map()
            PhoneIntelMap(init.country, init.area)

        separator()
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")

def install_dependencies():
    # Lista de dependencias
    dependencies = {
        "colorama": "0.4.6",
        "phonenumbers": "8.13.42",
        "requests": "2.32.3",
        "beautifulsoup4": "4.12.3"
    }

    # Preguntar al usuario si quiere instalar las dependencias
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

    # Comando para instalar paquetes
    pip_command = [sys.executable, "-m", "pip", "install"]
    
    print(f"Installing pip packages...")
    for package, version in dependencies.items():
        try:
            # Intentar importar el paquete
            __import__(package)
            print(f"{package} is already installed.")
        except ImportError:
            # Si el paquete no está instalado, instalarlo
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
        help_text += "  info    Execute info command\n"
        help_text += "  search  Execute search command\n"
        help_text += "  dorks   Execute dorks command\n\n"

        # Detailed Command Help
        help_text += "Detailed Command Help:\n\n"
        help_text += "  info:\n\n"
        help_text += "    phoneintel info <phone> [--map]\n\n"
        help_text += "    Arguments:\n\n"
        help_text += "      <phone>  Phone number to be processed\n"
        help_text += "      --map    Execute map function (optional)\n\n"

        help_text += "  search:\n\n"
        help_text += "    phoneintel search [<phone>] [--input FILE | --string TEXT] [--map]\n\n"
        help_text += "    Arguments:\n\n"
        help_text += "      <phone>   Phone number to be processed (optional)\n"
        help_text += "      --input   Input file for search (optional)\n"
        help_text += "      --string  Search string (optional)\n"
        help_text += "      --map     Execute map function (optional)\n\n"

        help_text += "  dorks:\n\n"
        help_text += "    phoneintel dorks <phone> --type TYPE [--map]\n\n"
        help_text += "    Arguments:\n"
        help_text += "      <phone>  Phone number to be processed\n"
        help_text += "      --type   Type of dorks (required)\n"
        help_text += "               Valid types: {}\n".format(", ".join(DORKS_TYPES))
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
    # Grupo de argumentos mutuamente excluyentes
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--info', action='store_true', help='Execute info command')
    group.add_argument('--search', action='store_true', help='Execute search')
    group.add_argument('--dorks', action='store_true', help='Execute dorks command')
    group.add_argument('-h', '--help', action='store_true', help='Show help message and exit')
    # Argumento posicional opcional para el número de teléfono
    parser.add_argument('phone', nargs='?', type=str, help='Phone number to be processed')
    # Argumentos adicionales para --search
    search_group = parser.add_argument_group('search_group', 'Arguments for search')
    search_group.add_argument('--input', type=str, help='Input file for search')
    search_group.add_argument('--string', type=str, help='Search string')
    # Argumentos adicionales para --dorks
    dorks_group = parser.add_argument_group('dorks_group', 'Arguments for dorks')
    dorks_group.add_argument('--type', type=str, help='Type of dorks')
    # Añadir el argumento --map
    parser.add_argument('--map', action='store_true', help='Execute map function')
    # Parsear los argumentos
    args = parser.parse_args()
    
    
    if args.help:
        CustomHelp()
        return
    # Validación de argumentos
    if args.search and not (args.input or args.string or args.phone):
        parser.error('--search requires --input, --string, or phone number')
    if args.dorks and not args.type:
        parser.error('--dorks requires --type')
    if args.dorks and args.type.strip().lower() not in DORKS_TYPES:
        parser.error(f'Invalid dork type: {args.type}. Valid types are: {", ".join(DORKS_TYPES)}')
    # Procesar los argumentos
    phone_number = args.phone
    
    if not args.search:
        phone_number = str(phone_number).strip()
        if not phone_number.startswith("+"):
            separator()
            print(Fore.YELLOW+Style.BRIGHT+"[!] Not an associated country number, adding +1")
            phone_number = f"+1{phone_number}"
        
    
    
    if args.info:
        if phone_number is None:
            parser.error('--info requires a phone')
        else:
            if args.map:
                print("alo")
                run_phoneintel(phone_number, args.map)
            else:
                run_phoneintel(phone_number)
    elif args.search:
        if phone_number is None and not (args.input or args.string):
            parser.error('--search requires --phone or (--input or --string)')
        if args.input:
            if args.map:
                run_phoneinteltext_path(args.input, args.map)
            else:
                run_phoneinteltext_path(args.input)
        elif args.string:
            if args.map:
                run_phoneinteltext_string(args.string, args.map)
            else:
                run_phoneinteltext_string(args.string)
    elif args.dorks:
        if phone_number is None:
            parser.error('--dorks requires --phone')
        else:
            if args.map:
                run_phoneinteldorking(phone_number, args.type, args.map)
            else:
                
                run_phoneinteldorking(phone_number, args.type)
    
    
    
    
    
    
if __name__ == "__main__":
    main()
