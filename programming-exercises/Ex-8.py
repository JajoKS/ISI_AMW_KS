"""Napisz program, który generuje losowy ciąg znaków o długości 100, a następnie utwórz
słownik którego kluczami będą unikalne znaki występujące w ciągu, a wartościami liczba
ich wystąpień w ciągu znakowym. Utwórz listę, której każdy element to krotka (tupla),
zawierająca kolejny klucz z ww. słownika i odpowiadającą mu wartość liczbową.
Hint: skorzystaj z modułu collections i klasy Counter().
"""
import string
import random
from collections import Counter

def funkcja():
    ciag_rand = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    print(f"Ciag znakow o dlugosci 100: ")

    znaki_uni = Counter(ciag_rand)
    print(f"Słownik z unikalnymi znakami: {znaki_uni}")

    lista = list(znaki_uni.items())
    print(f"Lista krotek (klucz, wartość): {lista}")

if __name__ == '__main__':
    funkcja()