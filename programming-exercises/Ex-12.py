"""Zamienić wszystkie litery o na 0, e na 3, i na 1, a na 4 w podanej przez użytkownika sentencji."""

# Sentencja od użytkownika
def zamien():
    zamiana = {'o': '0', 'e': '3', 'i': '1', 'a': '4'}  # słownik zamian
    sentencja = input(f"Sentencja: ")
    # Iterujemy przez każdy znak i dokonujemy zamiany, jeśli jest w słowniku
    wynik = ''.join(zamiana.get(znak, znak) for znak in sentencja)
    return wynik

if __name__ == '__main__':
    print(f"Odwrócona sentencja: {zamien()}")