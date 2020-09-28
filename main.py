from bs4 import BeautifulSoup
from requests import get

URL = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/?search%5Bfilter_enum_furniture%5D%5B0%5D=yes&search%5Bfilter_enum_rooms%5D%5B0%5D=one'

def parse_price(price):
  return float(price.replace(' ', '').replace('zł', '').replace(',', '.'))

page = get(URL)
bs = BeautifulSoup(page.content, 'html.parser')

for offer in bs.find_all('div', class_='offer-wrapper'):
  footer = offer.find('td', class_='bottom-cell')
  location = footer.find('small', class_='breadcrumb').get_text().strip().split(',')[0]
  title = offer.find('strong').get_text().strip()
  price = parse_price(offer.find('p', class_="price").get_text().strip())
  link = offer.find('a')
  print(location, title, price)
  break