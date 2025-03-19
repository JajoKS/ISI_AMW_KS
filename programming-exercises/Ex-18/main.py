"""Stworzyć plik funkcje.py, w którym należy zaimplementować funkcję: dodawanie, odejmowanie, dzielenie, 
mnożenie oraz modulo. W pliku main.py zaimportować plik funkcje.py i wykorzystać zaimportowane funkcje 
na przykładowych wartościach."""
import funkcje

if __name__ == '__main__':
    a = float(input("Podaj A: "))
    b = float(input("Podaj B: "))
    print(f"Dodawanie: {a} + {b} = {funkcje.dodawanie(a, b)}")
    print(f"Odejmowanie: {a} - {b} = {funkcje.odejmowanie(a, b)}")
    print(f"Dzielenie: {a} / {b} = {funkcje.dzielenie(a, b)}")
    print(f"Mnożenie: {a} * {b} = {funkcje.mnożenie(a, b)}")
    print(f"Modulo: {a} % {b} = {funkcje.modulo(a, b)}")