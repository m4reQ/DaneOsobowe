import colored
from colored import stylize
print("Witaj, emm...")
print("Jak mam cie nazywac?")
class dane:
    def __init__(self, imie, nazwisko, wiek, miasto, plec, waga):
        self.imie = imie 
        self.nazwisko = nazwisko 
        self.wiek = wiek 
        self.miasto = miasto
        self.plec = plec
        self.waga = waga

osoba = dane("","",0,"",0,0)

def zmianaplci():
        while 1>0:
            print("Wybierz Płeć\n1. Mężczyzna\n2. Kobieta\n3. Inne")
            osoba.plec = input("Wybierz Płeć: ")
            if osoba.plec == str(1):
                osoba.plec = "Mężczyzna"
                print("Wybrano płeć: " + osoba.plec)
                break
            elif osoba.plec == str(2):
                osoba.plec = "Kobieta"
                print("Wybrano płeć: " + osoba.plec)
                break
            elif osoba.plec == str(3):
                osoba.plec = input("Podaj Swoją Płeć: ")
                print("Wybrano płeć: " + osoba.plec)
                break
            else:
                continue

def zmianaimienia():
    osoba.imie = input("Podaj Imie: ")
    print("Wpisane Imię to " + osoba.imie)

def zmiananazwiska():
    osoba.nazwisko = input("Podaj Nazwisko: ")
    print("Wpisane Nazwisko to " + osoba.nazwisko)

def zmianawieku():
    osoba.wiek = input("Podaj Wiek: ")
    print("Wpisany Wiek to " + (osoba.wiek))

def zmianawagi():
    osoba.waga = input("Podaj swoją wagę (w kilogramach): ")
    print("Wpisana Waga to " + (osoba.waga) + "kg")

def zmianamiasta():
    osoba.miasto = input("Podaj miasto: ")
    print("Wpisane miasto to " + osoba.miasto)

def zmianadanych():
    if osoba.imie == "":
        zmianaimienia()
    else:
        while 1>0:
            print("Czy chcesz zmienić imię?")
            TakNie = input("T/N: ")
            if TakNie == "T":
                zmianaimienia()
                break
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
    if osoba.nazwisko == "":
        zmiananazwiska()
    else:
        while 1>0:
            print("Czy chcesz zmienić nazwisko?")
            TakNie = input("T/N: ")
            if TakNie == "T":
                zmiananazwiska()
                break
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
    if osoba.wiek == 0:
        zmianawieku()
    else:
        while 1>0:
            print("Czy chcesz zmienić wiek?")
            TakNie = input("T/N: : ")
            if TakNie == "T":
                zmianawieku()
                break
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję!")
                continue
    if osoba.miasto == "":
        zmianamiasta()
    else:
        while 1>0:
            print("Czy chcesz zmienic miasto")
            TakNie = input("T/N: : ")
            if TakNie == "T":
                zmianamiasta()
                break
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję!")
                continue
    if osoba.plec == 0:
        zmianaplci()
    else:
        while 1>0:
            print("Czy chcesz zmienić Płeć? ")
            TakNie = input("T/N: ")
            if TakNie == "T":
                zmianaplci()
                break
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
    if osoba.waga == 0:
        zmianawagi()
    else:
        while 1>0:
            print("Czy chcesz zmienić wage? ")
            TakNie = input("T/N: ")
            if TakNie == "T":
                zmianawagi()
                break
            elif TakNie == "N":
                break
            else:
                print("Wybrano nieprawidłową opcję")
                continue
            

ZmienianieDanych = False
while ZmienianieDanych == False:
    zmianadanych()
    print("---------------------------")
    print("Imie: " + osoba.imie)
    print("Nazwisko: " + osoba.nazwisko)
    print("Wiek: " + osoba.wiek)
    print("Plec: " + osoba.plec)
    print("Miasto: " + osoba.miasto)
    print("Waga: " + osoba.waga)
    print("---------------------------")
    print("Czy twoje dane sa poprawne?")
    while True:
        TakNie = input("T/N: ")
        if TakNie == "T":
            ZmienianieDanych = True
            break
        elif TakNie == "N":
            break
        else:
            print("Zly wybor")
            continue
        continue
print("Dziekujemy za informacje")