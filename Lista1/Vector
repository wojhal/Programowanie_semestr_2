import math
import random

class Vector:
    """
    Klasa służąca do tworzenia wektorów i wykonywania działań na nich

    Atrybuty:
    ----------
    args: int
        rozmiar wektora

    Metody:
    ---------
    __getitem__(index)
        pozwala na uzyskanie elementu wektora pod indeksem podanym przez użytkownika
    __str__
        pozwala na użycie metody print() wobec wektora stworzonego w naszej klasie
    __add__
        pozwala na dodanie do wektora stworzonego w naszej klasie wektora o takiej samej długości
    __sub__
        pozwala na odjęcie od wektora stworzonego w naszej klasie wektora o takiej samej długości
    __mul__
        pozwala na uzyskanie iloczynu skalarnego wektora stworzonego w naszej klasie oraz innego wektora
    __contains__
        pozwala na sprawdzenie czy w wektorze stworzonym w naszej klasie znajduje się dany element
    skalar
        pozwala na pomnożenie wszystkich elementów wektora przez daną liczbę
    suma
        pozwala na uzyskanie sumy wszystkich elementów stworzonego wektora
    dlugosc
        pozwala na uzyskanie długości stworzonego wektora (pierwiastka kwadratowego z sumy kwadratów wszystkich jego elementów)
    randomizer
        pozwala na wygenerowanie przypadkowych wartości z zakresu [-10,10] dla każdego elementu stworzonego wektora
    podmieniacz
        pozwala na zamienienie wektora stworzonego na wektor zaproponowany przez użytkownika

    """
    def __init__(self, args=3):
        """
        Parametry:
        ----------
        args: int >= 3
            rozmiar wektora
        Output:
        ---------
        wektor: list
            wektor, na którym będziemy wykonywać działania

        """
        if type(args) == int:
            if args >= 3:
                self.args = args
                wektor = []
                for argumenty in range(args):
                    wektor.append(0)
                self.wektor = wektor
            elif args < 3:
                print(f"Nie da się wygenerować wektora o liczbie {args} elementów")
        elif type(args) != int:
            raise TypeError("Niewłaściwy typ rozmiaru wektora, spróbuj podać liczbę naturalną większą bądź równą 3")
    def __getitem__(self, index):
        """
        Funkcja odpowiedzialna za uzyskanie elementu wektora pod indeksem podanym przez użytkownika

        Parametry:
        ----------
        index: int
            indeks elementu wektora, który użytkownik chcę otrzymać
        Output:
        ---------
        self.wektor[index]: float/int
            element wektora z indeksem podanym przez użytkownika

        """
        if -1*self.args <= index <= self.args-1:
            return self.wektor[index]
        elif index < -1*self.args or index > self.args-1:
            raise IndexError(f"Niewłaściwy index, musi to być liczba całkowita w przedziale [{-1*self.args},{self.args-1}]")
    def __str__(self):
        """
        Funkcja odpowiedzialna za przedstawienie wektora w postaci listy na ekranie komputera

        Output:
        ---------
        str(self.wektor): str
            wektor "wyprintowany" na ekranie

        """
        return str(self.wektor)
    def __add__(self, obiekt1):
        """
        Funkcja odpowiedzialna za dodanie do stworzonego wektora drugiego wektora podanego przez użytkownika

        Parametry:
        ----------
        obiekt1: list
            wektor, który ma być dodany do stworzonego w klasie wektora
        Output:
        ---------
        self.wektor: list
            wektor stworzony w klasie będący efektem dodawania wektorów tą funkcją

        """
        if len(obiekt1.wektor) == self.args:
            for argumenty in range(self.args):
                self.wektor[argumenty] += obiekt1.wektor[argumenty]
            return self.wektor
        elif len(obiekt1.wektor) != self.args:
            raise ValueError("Różne długości wektorów")
    def __sub__(self, obiekt2):
        """
        Funkcja odpowiedzialna za odjęcie od stworzonego wektora drugiego wektora podanego przez użytkownika

        Parametry:
        ----------
        obiekt2: list
            wektor, który ma być odjęty od stworzonego w klasie wektora
        Output:
        ---------
        self.wektor: list
            wektor stworzony w klasie będący efektem odjęcia od wektora stworzonego w klasie wektora podanego przez użytkownika

        """
        if len(obiekt2.wektor) == self.args:
            for argumenty in range(self.args):
                self.wektor[argumenty] -= obiekt2.wektor[argumenty]
            return self.wektor
        elif len(obiekt2.wektor) != self.args:
            raise ValueError("Różne długości wektorów")
    def __mul__(self, obiekt3):
        """
        Funkcja odpowiedzialna za obliczenie iloczynu skalarnego dwóch wektorów

        Parametry:
        ----------
        obiekt3: list
            wektor, z którym wektor stworzony w klasie stworzy iloczyn skalarny
        Output:
        ---------
        iloczyn: float
            iloczyn skalarny wektora w klasie oraz podanego przez użytkownika

        """
        if len(obiekt3.wektor) == self.args:
            nowa_lista = []
            for argumenty in range(self.args):
                nowa_lista.append(self.wektor[argumenty]*obiekt3.wektor[argumenty])
            iloczyn = sum(nowa_lista)
            return iloczyn
        elif len(obiekt3.wektor) != self.args:
            raise ValueError("Różne długości wektorów")
    def __contains__(self, element):
        """
        Funkcja odpowiedzialna za sprawdzenie czy w wektorze stworzonym w naszej klasie znajduje się dany element

        Parametry:
        ----------
        element: int/float
            element, którego obecność chce sprawdzić użytkownik
        Output:
        ----------
        True/False
            informacja zwrotna, czy podany element znajduje się w wektorze

        """
        if element in self.wektor:
            return True
        elif element not in self.wektor:
            return False
    def skalar(self, skalar):
        """
        Funkcja odpowiedzialna za przemnożenie wektora stworzonego w klasie przez skalar

        Parametry:
        ----------
        skalar: int/float
            skalar, przez który ma być przemnożony wektor stworzony w klasie
        Output:
        ----------
        self.wektor: list
            wektor stworzony w klasie o współrzędnych przemnożonych przez skalar

        """
        for h in range(self.args):
            self.wektor[h] = skalar*self.wektor[h]
        return self.wektor
    def suma(self):
        """
        Funkcja odpowiedzialna za zsumowanie wszystkich elementów wektora stworzonego w klasie

        Output:
        ----------
        suma: int/float
            suma wszystkich elementów wektora stworzonego w klasie

        """
        suma = sum(self.wektor)
        return suma
    def dlugosc(self):
        """
        Funkcja odpowiedzialna za otrzymanie długości wektora

        Output:
        ---------
        math.sqrt(dlugosc): int/float
            długość wektora stworzonego w klasie

        """
        najnowsza = []
        for p in range(self.args):
            najnowsza.append((self.wektor[p])**2)
        dlugosc = sum(najnowsza)
        return math.sqrt(dlugosc)
    def randomizer(self):
        """
        Funkcja odpowiedzialna za ustalenie przypadkowych współrzędnych naszego wektora

        Output:
        ---------
        self.wektor: list
            wektor stworzony w klasie ze zmienionymi współrzędnymi

        """
        for b in range(self.args):
            self.wektor[b] = round(random.uniform(-10, 10), 2)
        return self.wektor
    def podmieniacz(self, lista):
        """
        Funkcja odpowiedzialna za podmienienie wektora z klasy na inny, podany przez użytkownika

        Parametry:
        ----------
        lista: list
            wektor, który ma być od teraz wektorem w klasie
        Output:
        ---------
        self.wektor: list
            wektor w klasie pod podmienieniu na ten podany przez użytkownika

        """
        if type(lista) == list:
            if len(lista) == self.args:
                for a in range(self.args):
                    self.wektor[a] = lista[a]
                return self.wektor
            elif len(lista) != self.args:
                raise ValueError("Różne długości wektorów")
        elif type(lista) != list:
            raise TypeError(f"Niewłaściwy typ zmiennika, spróbuj podać listę o {self.args} elementach")


if __name__=="__main__":
    c = Vector(5)
    d = Vector(5)
    print("creator", c, d)
    print("checker", 2 in c, 0 in d)
    print("randomizer", c.randomizer())
    print("suma", c.suma())
    print("dlugosc", c.dlugosc())
    print("iloczyn", c*d)
    print("dod, ode", c + d, c-d)
    print("skalar", c.skalar(100))
    print("getter", c[4])
    print("podmieniacz", c.podmieniacz(["a", 2, "a", "a", "a"]))

