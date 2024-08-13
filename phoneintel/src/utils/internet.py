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

import requests

def is_connected(url='https://www.google.com', proxies=None, timeout=3):
    try:
        response = requests.get(url, proxies=proxies, timeout=timeout)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False
