"""Napisz program, który szuka określonego ciągu znaków w łańcuchu znakowym i zwraca indeks
pierwszego wystąpienia ciągu lub -1, gdy nie ma takiego ciągu.
Hint: skorzystaj z funkcji find().
"""
def znajdz_ciag(stringGL, string):
    wyn = stringGL.find(string)
    if wyn != -1:
        return print(f"Ciąg znaków został znaleziony na indeksie: {wyn}")
    else:
        return print("-1")

if __name__ == '__main__':
    stringGL = input("Podaj główny łańcuch znakowy: ")
    string_do_znalezienia = input("Podaj ciąg znaków do znalezienia: ")
    znajdz_ciag(stringGL,string_do_znalezienia)
