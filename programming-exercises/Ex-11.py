"""Odwrócić sentencję podaną przez użytkownika."""

# Sentencja od użytkownika
def OdwS():
    sentencja = input("Podaj sentencję: ")
    return sentencja[::-1]

if __name__ == '__main__':
    print(f"Odwrócona sentencja: {OdwS()}")