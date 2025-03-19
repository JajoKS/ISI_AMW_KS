"""Napisz prostą funkcję o nazwie potega(), przyjmującą jeden argument, 
podnoszącą podaną liczbę do trzeciej potęgi."""

def potega(x):
    return x ** 3
            

if __name__ == '__main__':
    x = float(input("Podaj liczbe: "))
    print(potega(x))