# Emoji Data Fetcher

## Description

This project is designed to parse a sitemap from a specified URL, download the content of each linked page, and save this content locally for further processing. It is particularly useful for keeping a local, up-to-date copy of emoji data from online repositories.

**THIS PROJECT IS A WORK-IN-PROGRESS AND NOT FULLY OPERATIONAL**

## TO-DO Links

- <https://emojipedia.org/sitemap.xml>
- <https://api.prod-deploy.zedge.net/emojipedia-content-discovery/sitemap/en/emoji>
- <https://api.prod-deploy.zedge.net/emojipedia-content-discovery/sitemap/en/static-content>
- <https://api.prod-deploy.zedge.net/emojipedia-content-discovery/sitemap/en/unicode>
- <https://api.prod-deploy.zedge.net/emojipedia-content-discovery/sitemap/en/vendor/apple/ios-17.4/0>
- <https://unicode.org/Public/emoji/15.1/emoji-test.txt>
- <https://unicode.org/Public/emoji/15.1/emoji-sequences.txt>
- <https://www.unicode.org/Public/UCD/latest/ucd/emoji/emoji-data.txt>

## Features

Parses XML sitemaps to extract URLs.
Downloads content from each URL.
Saves each file locally for offline access.

## To-Do

Current abilities are:

1. It reads from the emoji-test.txt file and parses all of the emoji data into json
2. It's currently able to idenfiy if something is a variant right now
3. Has logging output

Up next:

1. Have it compare emoji metadata to info in the sitemap
2. Download the emojis based off of URL pattern matching
3. Add prompts for users to select categories along with skin color variants (if any)
4. Investigate how flag variants work
5. Create config files

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setting Up a Virtual Environment

### MacOS/Linux

Open a terminal.
Navigate to the project directory.
Run the following command to create a virtual environment:
`python3 -m venv venv`

Activate the virtual environment:
`source venv/bin/activate`

Once the virtual environment is activated, install the required packages:
`pip install -r requirements.txt`

### Windows

Open Command Prompt or PowerShell.
Navigate to the project directory.
Run the following command to create a virtual environment:
`python -m venv venv`

Activate the virtual environment:
`.\venv\Scripts\activate`

Once the virtual environment is activated, install the required packages:
`pip install -r requirements.txt`

### Usage

To run the script, ensure that the virtual environment is activated, and execute:
`python emojidownloader.py`

## Contributing

Idk wtf I'm doing so any help is great. If you would like to contribute, please fork the repository and issue a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
