import os
import re
import phonenumbers
from phoneintel.src.utils.const import invalid_path, separator
class PhoneIntelText:
    
    def __init__(self, text_or_path: str, path: bool = True) -> None:
        if not isinstance(text_or_path, str):
            raise ValueError("Invalid input, must be a string")
        
        self.__target = text_or_path
        self.__phone_numbers = []
        if path:
            if os.path.exists(path):
                self.__path = os.path.realpath(self.__target)
                if os.path.isdir(self.__path):
                    self.__process_directory(self.__path)
                elif os.path.isfile(self.__path):
                    self.__process_file(self.__path)
            else:
                invalid_path()
                return
                
        else:
            self.__process_text(self.__target)

    def __process_directory(self, directory_path: str) -> None:
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.lower().endswith('.txt'):
                    file_path = os.path.join(root, file)
                    self.__process_file(file_path)

    def __process_file(self, file_path: str) -> None:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content:
                    self.__extract_phone_numbers(content)
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")

    def __process_text(self, text: str) -> None:
        if text:
            self.__extract_phone_numbers(text)

    def __extract_phone_numbers(self, content: str) -> None:
        lines = content.splitlines()

        phone_pattern = re.compile(r'\+?\d[\d\s\-()]{7,}\d')

        for line in lines:
            potential_numbers = phone_pattern.findall(line)
 
            for number in potential_numbers:
                try:

                    cleaned_number = re.sub(r'[^\d\+]', '', number)
                    parsed_number = phonenumbers.parse(cleaned_number, None)
                    number = f"+{parsed_number.country_code}{parsed_number.national_number}"
                    self.__phone_numbers.append(number)
                except phonenumbers.NumberParseException:
                    continue

    def get_phone_numbers(self) -> list:
        return self.__phone_numbers

