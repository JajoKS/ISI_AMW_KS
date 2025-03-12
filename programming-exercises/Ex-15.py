"""Używając pętli dodawaj do wcześniej zadeklarowanej tabeli liczby z przedziału od 1 do 100, 
które są podzielne przez 3 lub podzielne przez 5."""

def wyswietl():
    tabela = []
    for liczba in range(1, 101):
        if liczba % 3 == 0 or liczba % 5 == 0:
            tabela.append(liczba)
    print(' '.join(map(str, tabela)))
            

if __name__ == '__main__':
    wyswietl()