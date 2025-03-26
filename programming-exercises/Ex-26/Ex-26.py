"""Za pomocą webscrappera pobrać wszystkie oferty domów z podanego 
linku(https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing), 
każda oferta ma być obiektem klasy Home, który posiada atrybuty takie jak header_name, price, price_for_m2. 
Wszystkie obiekty zapisać do słownika oraz do pliku home.csv."""

import requests
from bs4 import BeautifulSoup
import csv

class Home:
    def __init__(self, header_name, price, price_for_m2):
        self.header_name = header_name
        self.price = price
        self.price_for_m2 = price_for_m2

def get_page_content(url):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    } #Potrzebny aby uzyskać dostęp do strony
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Failed to fetch page content, status code: {response.status_code}")

def extract_data(soup):
    homes = []
    for offer in soup.find_all('article', {'data-cy': 'listing-item'}): 
        header_name = offer.find('p', {'data-cy': 'listing-item-title'}).text.strip()
        price = offer.find('span',class_='css-2bt9f1 evk7nst0').text.strip()
        dl = offer.find('dl',class_='css-9q2yy4 e1nke57n1')  # Znajdź wszystkie <dl> na stronie
        dds = dl.find_all('dd')
        if len(dds) > 2:
            price_for_m2 = dds[2].text.strip()  # Wybierz drugi <dl>
        else:
            price_for_m2 = "Brak informacji"
        homes.append(Home(header_name, price, price_for_m2))
    return homes

def save_to_csv(homes, filename):
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile: #utf-8-sig to kodowanie UTF-8, ale z dodanym BOM, który pomaga Excelowi rozpoznać kodowanie i poprawnie wyświetlać polskie znaki.
        writer = csv.writer(csvfile,delimiter=";") #Ustawienie aby robiło przerwy za pomocą średników, ponieważ w excel polski nie oddziela domyślnie za pomocą ',' tylko ';'
        writer.writerow(['Header Name', 'Price', 'Price per m2'])
        for home in homes:
            writer.writerow([home.header_name, home.price, home.price_for_m2])

def save_to_dict(homes):
    return {i: vars(home) for i, home in enumerate(homes)}

def main():
    url = "https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing"
    try:
        soup = get_page_content(url)
        homes = extract_data(soup)
        save_to_csv(homes, 'H:\ISI\programming-exercises\Ex-26\home.csv')
        homes_dict = save_to_dict(homes)
        print("Dane zapisane do home.csv oraz do słownika:")
        print(homes_dict)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()