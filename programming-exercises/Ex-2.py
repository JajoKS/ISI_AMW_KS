"""Napisz program, który sprawdza czy wczytany łańcuch znakowy jest liczbą lub nie.
Muszą być wczytane co najmniej dwa znaki.
Hint: skorzystaj z funkcji all().
"""
def funkcja1(string):
        if all(char.isdigit() for char in string):
            return print("Podany lancuch jest cyfrą.")
        else:
            return print("Podany lancuch nie jest cyfrą.")

if __name__ == '__main__':
    pyt = input("Podaj lancuch: ")
    funkcja1(pyt)
