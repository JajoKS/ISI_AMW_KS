"""Prosta gra, program generuje losową liczbę od 1 do 100, użytkownik ma odgadnąć liczbę, 
jeżeli nie trafi ma zostać wyświetlona podpowiedź czy za duża czy za mała liczba."""

def palindrom():
    tekst = input("Podaj tekst: ")
    tekst = tekst.replace(" ", "").lower() # Usuwanie spacji i konwersja na małe litery
    if(tekst == tekst[::-1]):  # Sprawdzanie, czy tekst jest taki sam od tyłu
        return "Jest to palindromem"
    else:
        return "Nie jest to palindrom"
                          
if __name__ == '__main__':
    print(palindrom())