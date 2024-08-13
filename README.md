<p align="center">
  <img src="/imgs/phoneintel.png" alt="Descripción de la imagen">
</p>

# PhoneIntel - Transforming Phone Number Intelligence

[![PyPI version](https://img.shields.io/pypi/v/phoneintel.svg)](https://pypi.org/project/phoneintel/)
[![GitHub issues](https://img.shields.io/github/issues/phoneintel/phoneintel.svg)](https://GitHub.com/phoneintel/phoneintel/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/phoneintel/phoneintel.svg)](https://GitHub.com/phoneintel/phoneintel/pull/)
[![GitHub forks](https://img.shields.io/github/forks/phoneintel/phoneintel.svg?style=social)](https://github.com/phoneintel/phoneintel/network/)
[![GitHub license](https://img.shields.io/github/license/phoneintel/phoneintel.svg)](https://github.com/phoneintel/phoneintel/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/phoneintel/phoneintel.svg)](https://GitHub.com/phoneintel/phoneintel/graphs/contributors/)
[![GitHub stars](https://img.shields.io/github/stars/phoneintel/phoneintel.svg?style=social)](https://GitHub.com/phoneintel/phoneintel/stargazers/)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)

### Introduction

Welcome to **PhoneIntel**, your ultimate open-source solution for harnessing the power of phone number intelligence. Designed for OSINT enthusiasts and professionals, PhoneIntel is an advanced tool that enables you to search and analyze comprehensive information about phone numbers, empowering you with insights at your fingertips.

With PhoneIntel, uncover essential details about phone numbers, including country, area or state, carrier information, and more. Seamlessly handle multiple phone numbers, generate precise Google dorks for social media, forums, classified ads sites, and map locations directly on OpenStreetMap.

### Key Features

- **In-Depth Phone Number Analysis**: Gain detailed insights such as country, area or state, and carrier information.
- **Batch Processing**: Effortlessly analyze multiple phone numbers from a text file.
- **Google Dork Generation**: Create URL-encoded Google dorks tailored to specific categories.
- **Location Mapping**: Visualize phone number locations on OpenStreetMap with the `--map` option.
- **Tellows Integration**: Access additional data from [Tellows](https://www.tellows.com), including URL, score, and call type.
- **SpamCalls Integration**: Extract spam risk, last activity, and the latest report of phone numbers from [SpamCalls.net](https://spamcalls.net).
- **Neutrino API Integration**: Authenticate, search, and map phone number information using the [Neutrino API](https://www.neutrinoapi.com).

### Installation

1. Run the following command.

    ```bash
    pip install phoneintel
    ```

### For Kali Linux Users

Remember to add the Directory to PATH:

```bash
export PATH=$PATH:/home/<username>/.local/bin
```

### Getting Started

#### Single Phone Number Lookup
Discover detailed information about a specific phone number:
```bash
phoneintel --info +34613814500
```

#### Multiple Phone Numbers from a String
Analyze multiple phone numbers embedded within a text string:
```bash
phoneintel --search --string "My number is +16148077641 but you can call me at +34613814500"
```

#### Batch Analysis from a Text File
Process multiple phone numbers listed in a text file:
```bash
phoneintel --search --input ./example.txt
```

#### OpenStreetMap Location Mapping
View the location of a phone number on OpenStreetMap:
```bash
phoneintel --info "+34613814500" --map
```

#### Generate Google Dorks
Create targeted Google dorks for various categories:
```bash
phoneintel "+34613814500" --dorks --type social_networks
```

### Neutrino API Usage

#### Authenticate with Neutrino API
To use the Neutrino API, you first need to log in with your API credentials:
```bash
phoneintel --neutrino --login --id <api-id> --key <api-key>
```

#### Show Neutrino API Credentials
To display your current Neutrino API credentials:
```bash
phoneintel --neutrino --show
```

#### Lookup Phone Number with Neutrino API
Search for phone number information using the Neutrino API:
```bash
phoneintel --neutrino +34613814500
```

#### Lookup and Map Phone Number with Neutrino API
Search for and map phone number information using the Neutrino API:
```bash
phoneintel --neutrino +34613814500 --map
```

### Help and Usage Guide

PhoneIntel includes a custom help formatter to provide detailed and aesthetic command line assistance.

#### Command Format
```bash
phoneintel <command> [options]
```

#### Available Commands

- `--info`: Execute info command
- `--search`: Execute search command
- `--dorks`: Execute dorks command
- `--browser`: Execute browser command
- `--neutrino`: Execute Neutrino API command
- `--credits`: Show the credits
- `--disclaimer`: Show the Enduser and information disclaimer

#### Detailed Command Help

##### Info
```bash
phoneintel --info <phone> [--map]
```
- **Arguments:**
  - `<phone>`: Phone number to be processed
  - `--map`: Execute map function (optional)

##### Search
```bash
phoneintel --search [<phone>] [--input FILE | --string TEXT] [--neutrino-api] [--map]
```
- **Arguments:**
  - `<phone>`: Phone number to be processed (optional)
  - `--input`: Input file for search (optional)
  - `--string`: Search string (optional)
  - `--neutrino-api`: Return Neutrino API information (optional)
  - `--map`: Execute map function (optional)

##### Dorks
```bash
phoneintel --dorks <phone> --type TYPE [--neutrino-api] [--map]
```
- **Arguments:**
  - `<phone>`: Phone number to be processed
  - `--type`: Type of dorks (required)
    - Valid types: 
        - social_networks 
        - forums
        - classifieds 
        - ecommerce
        - news 
        - blogs 
        - job_sites 
        - pastes 
        - reputation 
        - phone_directories
        - people_search
        - all
        
  - `--neutrino-api`: Return Neutrino API information (optional)
  - `--map`: Execute map function (optional)

##### Browser
```bash
phoneintel --browser <phone> [--neutrino-api] [--map]
```
- **Arguments:**
  - `<phone>`: Phone number to be processed
  - `--neutrino-api`: Return Neutrino API information (optional)
  - `--map`: Execute map function (optional)

##### Neutrino
```bash
phoneintel --neutrino [<phone> | --login --id <api-id> --key <api-key> | --show] [--map]
```
- **Arguments:**
  - `<phone>`: Phone number to be processed
  - `--login`: Login in the Neutrino API
    - `--id`: API ID
    - `--key`: API KEY
  - `--show`: Show Neutrino API Credentials
  - `--map`: Execute map function (optional)

### Examples

#### Basic Information Search
```bash
phoneintel --info "+34613814500"
```

#### Batch Search from File
```bash
phoneintel --search --input ./numbers.txt
```

#### Generate Dorks for Social Networks
```bash
phoneintel --dorks "+34613814500" --type social_networks
```

#### Browser Command Usage
```bash
phoneintel --browser "+34613814500" --map
```

### Disclaimer

PhoneIntel is intended for educational and research purposes only. It is designed to perform basic scans and provide initial insights into phone numbers. Always ensure you have proper authorization before using any tool for security assessments. Misuse of this tool for unauthorized or illegal activities is strictly prohibited. Use responsibly and within the bounds of applicable laws and regulations.

### Comprehensive Documentation

Dive into the full capabilities of PhoneIntel through our detailed documentation: [PhoneIntel Documentation](https://phoneintel.github.io)

### Attribution

PhoneIntel uses data from the following sources:

- [Tellows](https://www.tellows.com): Provides phone number ratings, reports, and other related information.
- [Neutrino API](https://www.neutrinoapi.com): Offers services for validating and analyzing phone numbers.
- [SpamCalls.net](https://spamcalls.net): Provides spam risk assessment, last activity, and user reports for phone numbers.

### Contributing

We welcome contributions! To propose major changes, please open an issue first to discuss your ideas. Ensure all relevant tests are updated accordingly.

### License

PhoneIntel is licensed under the Apache 2.0 License. For more details, see the [LICENSE](https://github.com/phoneintel/phoneintel/blob/main/LICENSE) file.

---

Elevate your phone number intelligence capabilities with PhoneIntel – the tool that brings OSINT to your fingertips.

