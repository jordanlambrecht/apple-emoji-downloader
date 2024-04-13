import xml.etree.ElementTree as ET
import requests
import os
import json

def parse_and_download_sitemap(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Namespace handling
    namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Extract URLs from the sitemap
    urls = []
    for url in root.findall('ns:url', namespaces):
        loc = url.find('ns:loc', namespaces).text
        lastmod = url.find('ns:lastmod', namespaces)
        lastmod = lastmod.text if lastmod is not None else "Not provided"
        urls.append({
            'url': loc,
            'last_modified': lastmod
        })

        # Download each URL content and save it locally
        response = requests.get(loc)
        if response.status_code == 200:
            file_name = loc.split('/')[-1] or "index.html"
            file_path = os.path.join('downloaded_content', file_name)
            os.makedirs('downloaded_content', exist_ok=True)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded and saved content from {loc} to {file_path}")
        else:
            print(f"Failed to download content from {loc}")

    # Optionally, save to JSON
    with open('sitemap_urls.json', 'w') as json_file:
        json.dump(urls, json_file, indent=4)

    print(f"Extracted and downloaded content for {len(urls)} URLs from the sitemap.")

# Replace 'sitemap.xml' with the path to your downloaded XML file
parse_and_download_sitemap('sitemap.xml')
