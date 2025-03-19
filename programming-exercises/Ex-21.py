"""Dziedziczenie klas. Klasa Animal ma zawierać atrybuty takie jak name, age, sex oraz metodę sound(). 
Klasy Dog, Cat oraz Fox dziedziczą po klasie Animal oraz nadpisują funkcje sound() odpowiednimi dźwiękami, 
dodatkowo klasy Dog oraz Cat posiadają atrybut breed."""

class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        raise "Empty" # Raise przerywa program

class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return f"{self.name} is barking!"

class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return f"{self.name} is meowing!"

class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sound(self):
        return f"{self.name} is screaming!"

dog = Dog("Rex", 3, "Male", "Golden Retriever")
cat = Cat("Whiskers", 2, "Female", "Persian")
fox = Fox("Foxy", 4, "Male")

if __name__ == '__main__':
    print(f"{dog.sound()} and its breed is {dog.breed}")
    print(f"cat.sound() and its breed is {cat.breed}")
    print(fox.sound())