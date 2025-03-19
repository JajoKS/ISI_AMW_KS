"""Napisz program, który korzystająć z metody chr() wygeneruje łańcuch znakowy z alfabetem, czyli 'abc....xyz'.
Do pliku alfabet1-numeralbumu.txt zapisz wygenerowany łańcuch znakowy, a do pliku alfabet2-numeralbumu.txt 
zapisz litery z ww. łańcucha znakowego, tylko że każda litera ma się znaleźć w osobnej linii w pliku.
Hint: oprócz funkcji write() skorzystaj również z menadżera kontekstu with, żeby nie zapomnieć o zamknięciu pliku."""

import os

alfabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1)) # Generowanie lancucha
sciezka = r"H:\ISI_LAB\programming-exercises\Ex-10"
sciezka2 = r"H:\ISI_LAB\programming-exercises\Ex-10"
with open(os.path.join(sciezka, "alfabet1-numeralbumu.txt"), "w") as file1: # Zapis lancucha do pliku
    file1.write(alfabet)


with open(os.path.join(sciezka2, "alfabet2-numeralbumu.txt"), "w") as file2: # Zapis kazdej litery w osobnej linii do pliku
    for litera in alfabet:
        file2.write(litera + '\n')

if __name__ == '__main__':
    print("Zapisano dane do plików alfabet1-numeralbumu.txt oraz alfabet2-numeralbumu.txt.")