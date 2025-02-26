"""Napisz program, który szuka określonego ciągu znaków w łańcuchu znakowym i zwraca
indeksy wszystkich wystąpień ciągu lub -1, gdy nie ma takiego ciągu.
Hint: skorzystaj z funkcji split().
"""
def znajdz_ciagi(stringGL, string):
    czesci = stringGL.split(string)
    if len(czesci) == 1:
        return print("-1")
    wyn = []
    ciag = 0
    for czesc in czesci[:-1]:
        ciag += len(czesc)
        wyn.append(ciag)
        ciag += len(string)
    return print(f"Ciąg znaków został znaleziony na indeksie: {wyn}")

if __name__ == '__main__':
    stringGL = input("Podaj główny łańcuch znakowy: ")
    string_do_znalezienia = input("Podaj ciąg znaków do znalezienia: ")
    znajdz_ciagi(stringGL,string_do_znalezienia)
