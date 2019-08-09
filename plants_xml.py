from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import re


url = 'https://www.w3schools.com/xml/plant_catalog.xml'
response = get(url, verify=False)

soup = BeautifulSoup(response.content, 'xml')

names = []
botanical_names = []
zones = []
lights = []
prices = []
availabilities = []

plants = soup.find_all('PLANT')

for plant in plants:

    names.append(plant.COMMON.text)
    botanical_names.append(plant.BOTANICAL.text)
    zones.append(plant.ZONE.text)
    lights.append(plant.LIGHT.text)
    prices.append(float(re.findall("\d+\.\d+", plant.PRICE.text)[0]))
    availabilities.append(int(plant.AVAILABILITY.text))
    

test_df = pd.DataFrame({
    'Name': names,
    'Botanical Name': botanical_names,
    'Zone': zones,
    'Price': prices,
    'Light Required': lights,
    'In-Stock': availabilities
})

print(test_df)







