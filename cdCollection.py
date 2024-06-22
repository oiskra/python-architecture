import requests
import xml.etree.ElementTree as ET

URL = "https://www.w3schools.com/xml/cd_catalog.xml"

if __name__ == "__main__":
    results = []
    response = requests.get(URL)
    root = ET.fromstring(response.content)    
    
    for i in root.findall("CD"):
        title = i.find("TITLE").text
        artist = i.find("ARTIST").text
        results.append((artist, title))
        
    print(results)
        
        
# <CD>
#     <TITLE>Empire Burlesque</TITLE>
#     <ARTIST>Bob Dylan</ARTIST>
#     <COUNTRY>USA</COUNTRY>
#     <COMPANY>Columbia</COMPANY>
#     <PRICE>10.90</PRICE>
#     <YEAR>1985</YEAR>
# </CD>