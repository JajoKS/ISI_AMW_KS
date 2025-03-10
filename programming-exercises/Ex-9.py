"""Stwórz klasy Vehicle i Car z polami nazwa, rok_produkcji i przebieg oraz metodami is_old() 
i is_long_mileage(). Stwórz po jednym obiekcie dla każdej z klas oraz trzeci obiekt, gdzie 
klasa Car dziedziczy z klasy Vehicle. Dla każdego z obiektów wywołaj obie metody, co najmniej 
raz użyj dekoratora @property w każdym z trzech przypadków."""

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg
    @property
    def is_old(self):
        obecny_rok = 2025
        return obecny_rok - self.rok_produkcji > 20 #starszy niz 20 lat jest za stary
    @property
    def is_long_mileage(self):
        return self.przebieg > 200000 #wiekszy niz 200000 jest wysoki
    
class Car(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg):
        super().__init__(nazwa, rok_produkcji, przebieg)

veh1 = Vehicle("BMW", 2000, 280000)
car1 = Car("Toyota", 2008, 260000)
car2 = Car("Honda",2015, 160000)

if __name__ == '__main__':
    print(f"Czy {veh1.nazwa} jest stary: {veh1.is_old}, czy ma duży przebieg: {veh1.is_long_mileage}")
    print(f"Czy {car1.nazwa} jest stary: {car1.is_old}, czy ma duży przebieg: {car1.is_long_mileage}")
    print(f"Czy {car2.nazwa} jest stary: {car2.is_old}, czy ma duży przebieg: {car2.is_long_mileage}")