"""Używając pętli wyświetl liczby w przedziale od 1 do 100 podzielne przez 3 i 4 oraz podaj ich liczbę."""

# Sentencja od użytkownika
def wyswietl():
    i=0
    for liczba in range(1, 101):
        if liczba % 3 == 0 or liczba % 4 == 0:
            print(liczba, end=' ')
            i+=1
    print(f"\nIlosc liczb: {i}")
            

if __name__ == '__main__':
    wyswietl()