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
#             GPL-3.0 License            #
#                                        #
##########################################

from setuptools import setup, find_packages

setup(
    name='phoneintel',
    version='1.1.1',
    description='A tool for processing phone numbers with OSINT capabilities.',
    author='PhoneIntel',
    author_email='phoneintel@proton.me',
    license='GPL-3.0',
    url='https://github.com/phoneintel/phoneintel',
    packages=find_packages(include=['phoneintel', 'phoneintel.src', 'phoneintel.src.utils']),
    include_package_data=True,
    project_urls={
    'Bug Tracker': 'https://github.com/phoneintel/phoneintel/issues',
    'Documentation': 'https://phoneintel.github.io/',
    'Source Code': 'https://github.com/phoneintel/phoneintel',
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'colorama==0.4.6',
        'phonenumbers==8.13.42',
        'requests==2.32.3',
        'beautifulsoup4==4.12.3',
    ],
    entry_points={
        'console_scripts': [
            'phoneintel=phoneintel.main:main',
        ],
    },
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Programming Language :: Python :: 3.11',
    ],
)
