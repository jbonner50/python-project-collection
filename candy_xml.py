
from bs4 import BeautifulSoup
import pandas as pd
import lxml

f = open("candy-data.xml")      # simplified for the example (no urllib)
soup = BeautifulSoup(f, 'lxml')
f.close()

names = []
chocolates = []
fruitys = []
caramels = []
peanutyalmondys = []
nougats = []
crispedricewafers = []
hards = []
bars = []
sugarpercents = []
pricepercents = []
winpercents = []

candies = soup.find_all('candy')

for candy in candies:

    names.append(candy.competitorname.text)
    chocolates.append(int(candy.chocolate.text))
    fruitys.append(int(candy.fruity.text))
    caramels.append(int(candy.caramel.text))
    peanutyalmondys.append(int(candy.peanutyalmondy.text))
    nougats.append(int(candy.nougat.text))
    crispedricewafers.append(int(candy.crispedricewafer.text))
    hards.append(int(candy.hard.text))
    bars.append(int(candy.bar.text))
    sugarpercents.append(float(candy.sugarpercent.text))
    pricepercents.append(float(candy.pricepercent.text))
    winpercents.append(float(candy.winpercent.text))


candy_data = pd.DataFrame({
    'name': names,
    'chocolate': chocolates,
    'fruity': fruitys,
    'caramel': caramels,
    'peanutyalmondy': peanutyalmondys,
    'nougat': nougats,
    'wafer': crispedricewafers,
    'hard': hards,
    'bar': bars,
    'sugarpercent': sugarpercents,
    'pricepercent': pricepercents,
    'winpercent': winpercents  
})

print(candy_data)
