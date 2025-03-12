"""Używając pętli wyświetl liczby w przedziale od 1 do 50 oprócz liczb podzielnych przez 3."""

# Sentencja od użytkownika
def wyswietl():
    for liczba in range(1, 51):
        if liczba % 3 !=0:
            print(liczba, end=' ')

if __name__ == '__main__':
    print(wyswietl())