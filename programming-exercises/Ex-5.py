"""Napisz program (na dwa sposoby), który szuka pierwiastków liczb od 1 do 256 (włącznie)
podzielnych bez reszty przez 2.
Hint: skorzystaj z modułu math i z tzw. 'list comprehensions'.
"""
import math
def pierwiastki1():
    wyn = []
    for i in range(1, 257):
        sqrt_index = math.sqrt(i)
        if sqrt_index.is_integer() and i % 2 == 0:
            wyn.append(int(sqrt_index))
    return print(f"Pierwiastki liczb to: {wyn}")
def pierwiastki2():
    return print(f"Pierwiastki liczb to: {[int(math.sqrt(i)) for i in range(1, 257) if math.sqrt(i).is_integer() and i % 2 == 0]}")
if __name__ == '__main__':
    pierwiastki1()
    pierwiastki2()
