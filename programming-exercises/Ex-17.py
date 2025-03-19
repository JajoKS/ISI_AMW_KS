"""Stwórz klasę o nazwie Dog, która będzie posiadała zmienne takie jak: name, age, coat_color. 
Dodatkowo klasa posiada funkcje sound(), po wywołaniu której wypisywany jest tekst: {name} is barking! 
Stworzyć 3 obiekty klasy Dog."""

class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(f"{self.name} is barking!")

dog1 = Dog("Rex", 3, "brown")
dog2 = Dog("Bella", 5, "black")
dog3 = Dog("Charlie", 2, "white")

if __name__ == '__main__':
    dog1.sound()
    dog2.sound()
    dog3.sound()