from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint


url = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=num_votes,desc&start=1&ref_=adv_nxt'
response = get(url, verify=False)

html_soup = BeautifulSoup(response.text, 'html.parser')

#grabbing all movie containers
movie_containers = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
#print(type(movie_containers))
#print(len(movie_containers))

#lists to store scraped data
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

#multiple pages
pages = [str(i) for i in range(1,100,50)]
years_url = [str(i) for i in range(2000,2018)]

#extract data from each container
for container in movie_containers:
    
    #continue if container has metascore
    if container.find('div', class_ = 'ratings-metascore') is not None:
        #name
        name = container.h3.a.text
        names.append(name)

        #year
        year = container.h3.find('span', class_ = 'lister-item-year').text
        years.append(year)

        #imdb rating
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        #metascore
        m_score = container.find('span', class_ = 'metascore').text
        metascores.append(int(m_score))

        #votes
        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))

test_df = pd.DataFrame({
    'name': names,
    'year': years,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes
})

print(test_df.info())
print(test_df)


'''
# assigns first movie for testing
first_movie = movie_containers[0]

#name of the movie
#attribute notation for accessing <a> tag instide <h3> tag
#Dot notation will only access the first element
first_name=first_movie.h3.a.text
print(first_name)

#year of the movie
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
print(first_year)

#imbd rating
first_rating = float(first_movie.strong.text)
print(first_rating)

#metascore
#Attribute notation clearly isn’t a solution
#There are many <span> tags before that.
first_mscore = first_movie.find('span', class_ ='metascore')
first_mscore = float(first_mscore.text)
print(first_mscore)

#number of votes
#The name attribute is different from the class attribute. 
#Using BeautifulSoup we can access elements by any attribute. 
#The find() and find_all() functions have a parameter named attrs. 
#To this we can pass in the attributes and values we are searching for as a dictionary:
first_votes = first_movie.find('span', attrs = {'name':'nv'})
#We could use .text notation to access the <span> tag’s content.
# It would be better though if we accessed the value of the data-value attribute
# This way we can convert the extracted datapoint to an int without having to strip a comma.
#You can treat a Tag object just like a dictionary. 
# The HTML attributes are the dictionary’s keys. 
# The values of the HTML attributes are the values of the dictionary’s keys. 
# This is how we can access the value of the data-value attribute:
first_votes = int(first_votes['data-value'])
print(first_votes)
'''