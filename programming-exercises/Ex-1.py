"""Napisz program (na dwa sposoby), który sprawdza czy wczytany pojedynczy znak jest cyfrą lub nie.
Jeśli wczytamy więcej znaków, należy wziąć tylko pierwszy.
Hint: skorzystaj z funkcji isdigit() i isinstance()."""
def funkcja1(char):
        fchar = char[0]
        if fchar.isdigit():
            return print("Podany znak jest cyfrą.")
        else:
            return print("Podany znak nie jest cyfrą.")
def funkcja2(char):
    fchar = char[0]
    if isinstance(fchar,str) and fchar in '0123456789':
        return print("Podany znak jest cyfrą.")
    else:
        return print("Podany znak nie jest cyfrą.")

if __name__ == '__main__':
    pyt = input("Podaj znak: ")
    funkcja1(pyt)
    funckja2(pyt)