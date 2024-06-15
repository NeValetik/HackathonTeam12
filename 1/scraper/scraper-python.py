import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    if soup.select('.comments-moodle.d-flex'):
        elements = soup.select('.comments-moodle.d-flex')
        for element in elements:
            print("Review:", element.text.strip())
    elif soup.select('.reviews'):
        elements = soup.select('.reviews')
        for element in elements:
            print("Review:", element.text.strip())
    elif soup.select('.oneProd-reviewsList.cleanList'):
        elements = soup.select('.oneProd-reviewsList.cleanList')
        for element in elements:
            print("Review:", element.text.strip())

    else:
        print("No specific element found for reviews.")

    if soup.select('.price-num'):
        price = soup.select('.price-num')
        for element in price:
            print("Price:", element.text.strip())
    else:
        print("No price found")

if __name__ == '__main__':

    url = input()
    scrape(url)
