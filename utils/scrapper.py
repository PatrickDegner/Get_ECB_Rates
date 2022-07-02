import requests
from bs4 import BeautifulSoup


url = 'https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html'
response = requests.get(url)
simple_soup = BeautifulSoup(response.text, 'html.parser')

date = simple_soup.find('h3').string
country = simple_soup.find_all('td', {'class':'currency'})
country_content = [e.string for e in country]
currency = simple_soup.find_all('span', {'class':'rate'})
currency_contents = [e.string for e in currency]
stats = dict(zip(country_content,currency_contents))