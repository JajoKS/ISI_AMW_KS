#Za pomocą pętli stworzyć 1000 losowych 6 znakowych wyrazów [A-Z][a-z][0-9] i zapisać je do pliku passwords.txt.
import random
import string
def generuj():
    znaki = string.ascii_letters + string.digits # [A-Z][a-z][0-9]
    hasla = [''.join(random.choices(znaki, k=6)) for _ in range(1000)] # k oznacza dlugosc znakowego wyrazu
    return hasla

def zapisz(nazwa, hasla):
    with open(nazwa, 'w') as f:
        for haslo in hasla:
            f.write(haslo + '\n')

if __name__ == '__main__':
    plik = 'H:\ISI\ISI_AMW_KS\programming-exercises\Ex-23\passwords.txt'
    hasla = generuj() #zmienna z haslami
    zapisz(plik,hasla)

