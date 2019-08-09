#! python3
# opens first several google search results

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('https://google.com/search?q=fun', verify=False) #+ str(sys.argv[1]))
res.raise_for_status()

#retrive search result page
soup = bs4.BeautifulSoup(res.content, 'html.parser')

#retrieve links
links = soup.find_all('cite', class_ = "iUh30")

print(links)
numOpen = min(5, len(links))

for i in range(numOpen):
    webbrowser.open(links[i].get('href'))