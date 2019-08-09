# scraping.py

from bs4 import BeautifulSoup
import requests
import unicodedata


def scrape():
    l = []
    
    base_url = 'https://www.amazon.com/Best-Sellers/zgbs'

    # Request URL and Beautiful Parser
    r = requests.get(base_url)
    soup = BeautifulSoup(r.text, "html.parser")
    all_product = soup.find_all('div', class_="zg_item zg_homeWidgetItem")

    for item in all_product:
        d = {}

        # image
        product_image = item.find("img", {"class":"a-dynamic-image p13n-sc-dynamic-image"})
                                          
        # image = image.text.replace('\n', "").strip()
        product_image2 = product_image['src']
        d['product_image'] = product_image2

        # name & link
        product_name = product_image['alt']
        product_link = 'https://www.amazon.com' + str(item.find("a", {"class":"a-link-normal"}).get('href'))
        product_name = str(unicodedata.normalize('NFKD', str(product_name)).encode('ascii','ignore'))
        d['product_link'] = product_link
        d['product_name'] = product_name

        # rank
        product_rank = item.find("div", {"class":"zg_rank"})
        product_rank = '#' + str(''.join(filter(str.isdigit, product_rank.text)))
        d['product_review'] = str(product_rank)

        # category
        product_category
        # insert result into list
        l.append(d)
    # return list
    return l


if __name__ == "__main__":
    print(scrape())