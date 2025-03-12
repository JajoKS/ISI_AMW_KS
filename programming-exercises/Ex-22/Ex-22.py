"""Należy wykorzystać plik wordlist_10000.txt i stworzyć funkcję wyszukującą najdłuższy wyraz w tym pliku 
oraz drugą funkcję, która wyszuka wyrazy o długości 10.
"""
def najdluzszy_wyraz(plik):
    najdluzszy = ""
    with open(plik, 'r') as f:
        for linia in f:
            wyraz = linia.strip()
            if len(wyraz) > len(najdluzszy):
                najdluzszy = wyraz
    return najdluzszy

def wyrazy_dlugosci_10(plik):
    wyrazy_10 = []
    with open(plik, 'r') as f:
        for linia in f:
            wyraz = linia.strip()
            if len(wyraz) == 10:
                wyrazy_10.append(wyraz)
    return 

if __name__ == '__main__':
    plik = 'wordlist_10000.txt'
    
    # Wyszukiwanie najdłuższego wyrazu
    najdluzszy = najdluzszy_wyraz(plik)
    print(f"Najdłuższy wyraz: {najdluzszy}")
    
    # Wyszukiwanie wyrazów o długości 10
    wyrazy_10 = wyrazy_dlugosci_10(plik)
    print(f"Wyrazy o długości 10: {', '.join(wyrazy_10)}")