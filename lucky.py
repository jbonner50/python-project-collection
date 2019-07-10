#! python3
# opens first several google search results

import requests, sys, webbrowser, bs4

print('Googling...')
res = requests.get('https://google.com/search?q=fun')# + '+'.join(sys.argv[1:]), verify=False)
res.raise_for_status()

#retrive search result page
soup = bs4.BeautifulSoup(res.text)

#retrieve links
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('https://google.com' + linkElems[i].get('href'))