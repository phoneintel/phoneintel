import requests
import webbrowser
from urllib.parse import quote
from phoneintel.src.utils.const import separator

class PhoneIntelMap:
    
    def __init__(self, country: str, state: str = None, only_coordinates:bool=False) -> None:
        self.__country = country
        self.__state = state
        self.__api = None
        self.__lon = None
        self.__lat = None
        if only_coordinates:
            self.__req_coordinates()
            try:
                self.__req_coordinates()
                try:
                    self.__make_req()
                    
                    coordinates = [self.__lat, self.__lon]
                    return coordinates

                except Exception as e:
                    coordinates = ["Unknown", "Unknown"]
                    return coordinates
            except:
                coordinates = ["Unknown", "Unknown"]
                return coordinates

        else:
            try:
                self.__req_coordinates()
                try:
                    self.__make_req()
                    if self.__lon:
                        self.open_map()
                except Exception as e:
                    print(f"An error occurred: {e}")
            except:
                print(f"An error occurred: {e}")
        
        
    def __req_coordinates(self):
        if self.__state:
            self.__api = f"https://nominatim.openstreetmap.org/search?q={quote(self.__state)},{quote(self.__country)}&format=json"
        else:
            self.__api = f"https://nominatim.openstreetmap.org/search?q={quote(self.__country)}&format=json"
    
    def __make_req(self):
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
            
    def open_map(self):
        if self.__lon and self.__lat:
            map_url = f"https://www.openstreetmap.org/?mlat={self.__lat}&mlon={self.__lon}#map=12/{self.__lat}/{self.__lon}"
            webbrowser.open(map_url)
        else:
            raise ValueError("Coordinates are not set. Ensure the API request was successful.")
