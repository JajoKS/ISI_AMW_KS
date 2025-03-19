"""Prosta gra, program generuje losową liczbę od 1 do 100, użytkownik ma odgadnąć liczbę, 
jeżeli nie trafi ma zostać wyświetlona podpowiedź czy za duża czy za mała liczba."""

import random

def gra_odgadywanie():
    liczba_do_odgadniecia = random.randint(1, 100) # Generowanie losowej liczby od 1 do 100
    
    print("Zgadnij liczbę od 1 do 100!")

    while True:
        try:
            liczba_uzyt = int(input("Twoja liczba: "))
            # Sprawdzenie, czy zgadnięta liczba jest za duża, za mała czy poprawna
            if liczba_uzyt < liczba_do_odgadniecia:
                print("Za mała!")
            elif liczba_uzyt > liczba_do_odgadniecia:
                print("Za duża!")
            else:
                print(f"Brawo! Odgadłeś liczbę {liczba_do_odgadniecia}.")
                break
        except ValueError:
            print("Proszę podać poprawną liczbę.")
            continue

if __name__ == '__main__':
    gra_odgadywanie()