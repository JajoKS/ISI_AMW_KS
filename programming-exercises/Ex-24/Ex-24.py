"""Napisać funkcję tworzącą plik pc.csv. Pierwszy wiersz ma zawierać nazwy kolumn: pc_name, ip. 
Nazwy komputerów mają zaczynać się literą P oraz 4 oktetem adresu ip. Adresy zaczynają się od 172.30.2.1 do 172.30.2.100. 
Plik csv ma być rozdzielany przecinkami."""
import csv

def utworz_pc_csv(nazwa, poczIp, konIp):
    ip_range = [f"172.30.2.{i}" for i in range(poczIp,konIp + 1)] #Tworzenie listy z ip
    dane = [{"pc_name": f"P{i}", "ip": ip} for i, ip in enumerate(ip_range, start=1)] #Tworzenie danych: pc_name i ip
    with open(nazwa, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["pc_name", "ip"], delimiter=',')
        writer.writeheader()  # Zapisanie nagłówka
        writer.writerows(dane)  # Zapisanie danych

if __name__ == '__main__':
    plik = 'H:\ISI\ISI_AMW_KS\programming-exercises\Ex-24\pc.csv'
    utworz_pc_csv(plik, poczIp=1, konIp=100)
    print(f"Plik {plik} został utworzony.")
