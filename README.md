
# PhoneIntel - Transforming Phone Number Intelligence

[![PyPI version](https://img.shields.io/pypi/v/phoneintel.svg)](https://pypi.org/project/phoneintel/)
[![GitHub issues](https://img.shields.io/github/issues/phoneintel/phoneintel.svg)](https://GitHub.com/phoneintel/phoneintel/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/phoneintel/phoneintel.svg)](https://GitHub.com/phoneintel/phoneintel/pull/)
[![GitHub forks](https://img.shields.io/github/forks/phoneintel/phoneintel.svg?style=social)](https://github.com/phoneintel/phoneintel/network/)
[![GitHub license](https://img.shields.io/github/license/phoneintel/phoneintel.svg)](https://github.com/phoneintel/phoneintel/blob/main/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/phoneintel/phoneintel.svg)](https://GitHub.com/phoneintel/phoneintel/graphs/contributors/)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)

### Introduction

Welcome to **PhoneIntel**, your ultimate open-source solution for harnessing the power of phone number intelligence. Designed for OSINT enthusiasts and professionals, PhoneIntel is an advanced tool that enables you to search and analyze comprehensive information about phone numbers, empowering you with insights at your fingertips.

With PhoneIntel, uncover essential details about phone numbers, including country, area or state, carrier information, and more. Seamlessly handle multiple phone numbers, generate precise Google dorks for social media, forums, classified ads sites, and map locations directly on OpenStreetMap.

### Key Features

- **In-Depth Phone Number Analysis**: Gain detailed insights such as country, area or state, and carrier information.
- **Batch Processing**: Effortlessly analyze multiple phone numbers from a text file.
- **Google Dork Generation**: Create URL-encoded Google dorks tailored to specific categories.
- **Location Mapping**: Visualize phone number locations on OpenStreetMap with the `--map` option.
- **Tellows Integration**: Access additional data from Tellows, including URL, score, and call type.

### Installation

1. Run the following command.

```bash
pip install phoneintel
```

### For Kali Linux Users

Remember Add the Directory to PATH:

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

### Examples

#### Basic Information Search
```bash
phoneintel --info "+34613814500"
```

### Disclaimer

PhoneIntel is intended for educational and research purposes only. It is designed to perform basic scans and provide initial insights into phone numbers. Always ensure you have proper authorization before using any tool for security assessments. Misuse of this tool for unauthorized or illegal activities is strictly prohibited. Use responsibly and within the bounds of applicable laws and regulations.

### Comprehensive Documentation

Dive into the full capabilities of PhoneIntel through our detailed documentation: [PhoneIntel Documentation](https://phoneintel.github.io)

### Contributing

We welcome contributions! To propose major changes, please open an issue first to discuss your ideas. Ensure all relevant tests are updated accordingly.

### License

PhoneIntel is licensed under the Apache 2.0 License. For more details, see the [LICENSE](https://github.com/phoneintel/phoneintel/blob/main/LICENSE) file.

---

Elevate your phone number intelligence capabilities with PhoneIntel – the tool that brings OSINT to your fingertips.
