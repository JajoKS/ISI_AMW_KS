"""Stwórz folder utils, a w nim plik 'obliczenia.py', w którym należy zaimplementować cztery 
wybrane funkcje matematyczne z modułu math. Następnie należy utworzyć plik skrypt7-nr_albumu.py
i zaimportować w nim ww. funkcje do obliczeń na przykładowych wartościach.
"""
from utils.obliczenia import kwadrat, silnia, logarytm, sinus

if __name__ == '__main__':
    a = input("Pierwiastek kwadratowy z: ")
    print(f"Pierwiastek kwadratowy z {a} wynosi {kwadrat(a)}")

    b = input("Silnia z liczby: ")
    print(f"Silnia z liczby {b} wynosi: {silnia(b)}")

    x = input("Logarytm: ")
    y = input("z podstawą: ")
    print(f"Logarytm {x} z podstawą {y} wynosi {logarytm(x, y)}")
    
    c = input("Sinus kąta: ")
    print(f"Sinus kąta {c} ma {sinus(c)} stopni")