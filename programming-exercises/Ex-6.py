"""Napisz program, który tworzy słownik o nazwie zawierającej Twój numer albumu.
Kluczami powinny być liczby od 10 do 20, a wartościami pseudolosowe łańcuch znaków o długości 8.
Hint: skorzystaj z modułów string i random.
"""
import string
import random

def stworz_słownik():
    nr_albumu = 25102
    wyn = {}

    for klucz in range(10, 21):
        wartosci_rand = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        wyn[klucz] = wartosci_rand

    return print(f"Slownik o nazwie: {nr_albumu} Zawartość: {wyn}")

if __name__ == '__main__':
    stworz_słownik()