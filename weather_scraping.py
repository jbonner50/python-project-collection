
import requests, bs4
import pandas as pd


page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = bs4.BeautifulSoup(page.content, 'html.parser')
another_page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
another_soup = bs4.BeautifulSoup(another_page.content, 'html.parser')
weather_page = requests.get("https://forecast.weather.gov/MapClick.php?lat=39.1071&lon=-84.5041")
weather_soup = bs4.BeautifulSoup(weather_page.content, 'html.parser')
#print(page)
#print(page.status_code)
#print(page.content)



'''
# organizes html
print(soup.prettify())
print(anothersoup.prettify())
# grabs all the children of soup & prints type
print(list(soup.children))
print([type(item) for item in list(soup.children)])
# sets html equal to html element of soup.children
html = list(soup.children)[2]
print(list(html.children))
# sets body equal to body tag of html tag of soup.children
body = list(html.children)[3]
print(list(body.children))
# sets p equal to paragraph of body of html of soup.children
p = list(body.children)[1]
# grabs text from tag
print(p.get_text())
'''

'''
#Finding instances of tags

# finds all occurences of p tag
print(soup.find_all('p')[0].get_text()) 
# finds first instance of tag
print(soup.find('p')) 
'''

'''
#Searching for tags by class & ID

# search for any p tag that has the class outer-text
print(another_soup.find_all('p', class_='outer-text'))
# search for elements by id:
print(another_soup.find_all(id="first"))
'''

'''
#CSS Selectors
# p a — finds all a tags inside of a p tag.
# body p a — finds all a tags inside of a p tag inside of a body tag.
# html body — finds all body tags inside of an html tag.
# p.outer-text — finds all p tags with a class of outer-text.
# p#first — finds all p tags with an id of first.
# body p.outer-text — finds any p tags with a class of outer-text inside of a body tag.
print(another_soup.prettify())
print(another_soup.select('div p'))
#select method above returns a list of BeautifulSoup objects, just like find_all.
'''


#Downloading weather data
#grabs seven day forcase element
seven_day = weather_soup.find(id="seven-day-forecast")
#sets forecast_items to a list of all the day containers
forecast_items = seven_day.find_all(class_="tombstone-container")
#sets today to the first element
today = forecast_items[0]
print(today.prettify())

'''
#Extracting information from the page
# The name of the forecast item — period-name
# The description of the conditions — title property of img.
# A short description of the conditions — short-desc.
# The temperature low — temp.
period = today.find(class_="period-name").get_text()
short_desc = today.find(class_="short-desc").get_text()
short_desc = ''.join(' ' + char if char.isupper() else char.strip() for char in short_desc).strip()
temp = today.find(class_="temp").get_text()
img = today.find("img")
desc = img['title']
print(period)
print(short_desc)
print(temp)
print(desc)
'''

#Extracting all the information from the page
#Select all items with the class period-name inside an item with the class tombstone-container in seven_day.
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)
#Use a list comprehension to call the get_text method on each BeautifulSoup object.
short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
print(short_descs)
print(temps)
print(descs)

#Combining our data into a Pandas Dataframe
#pass in each list of items that we have as part of a dictionary
#Each dictionary key will become a column in the DataFrame
#each list will become the values in the column:

print(len(periods))
print(len(short_descs))
print(len(temps))
print(len(descs))
""" weather = pd.DataFrame({
"period": periods,
"short_desc": short_descs,
"temp": temps,
"desc":descs
})
print(weather) """

""" temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)
print(weather["temp_num"].mean())

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(weather[is_night]) """