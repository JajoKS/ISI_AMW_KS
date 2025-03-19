"""Za pomocą pakietu do web-scrappingu, np.beautifulsoup lub jsoup, zapisać do tablicy wszystkie hiperłącza 
występujące na wybranej przez siebie stronie."""

import requests
from bs4 import BeautifulSoup

def znajdz_linki(url):
    # Wysyłanie żądania HTTP do strony
    response = requests.get(url)
    
    if response.status_code == 200:
        # Przetwarzanie zawartości strony za pomocą BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Znajdowanie wszystkich tagów <a> (hiperłącza)
        linki = [a['href'] for a in soup.find_all('a', href=True)]
        return linki
    else:
        print(f"Błąd przy próbie dostępu do strony: {response.status_code}")
        return []

if __name__ == '__main__':
    # Wprowadź adres URL strony, którą chcesz przeanalizować
    url = "https://www.leagueoflegends.com/pl-pl/"  # Zmień na wybraną stronę
    linki = znajdz_linki(url)
    
    # Wyświetlenie lub zapisanie hiperłączy
    if linki:
        print(f"Znaleziono {len(linki)} linków:")
        for link in linki:
            print(link)
    else:
        print("Nie znaleziono żadnych linków.")