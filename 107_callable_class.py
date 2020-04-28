"""
Trzeba zdefiniować klasę NoDuplicates, która będzie miała tylko jeden atrybut - list.
Ten atrybut to lista, która ma przechowywać tylko wartości unikalne.

Zdefiniuj klasę NoDuplicates
W metodzie __init__ utwórz atrybut list, który będzie pustą listą
Dodaj metodę __call__
metoda ma przyjąć argument self i listę z nowymi obiektami, jakie mają być przechowywane w liście new_items
dla każdego elementu z new_items, jeśli ten element nie występuje jeszcze na liście list, dodaj go do tej listy
Przetestuj działanie klasy
Utwórz obiekt my_no_dup_list, który będzie instancją klasy NoDuplicates. Wyświetl ten obiekt.
Wywołując instancję dodaj do listy elementy z listy ['keyboard','mouse']. Wyświetl ten obiekt.
Oba napisy powinny zostać dodane do listy
Wywołując instancję dodaj do listy elementy z listy ['keyboard','mouse','pendrive']. Wyświetl ten obiekt.
Tylko pendrive powinien zostać dodany
Wywołując instancję dodaj do listy elementy z listy ['charger','pendrive'].Wyświetl ten obiekt.
Tylko charger powinien zostać dodany"""


class NoDuplicates:
    def __init__(self, list=[]):
        self.list = list.copy()

    def __call__(self, new_items):
        for item in new_items:
            self.list.append(item) if item not in self.list else True

    def __str__(self):
        return str(self.list)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list)

my_no_dup_list(["keyboard", "mouse"])
print(my_no_dup_list)
my_no_dup_list(["keyboard", "mouse", "pendrive"])
print(my_no_dup_list)
my_no_dup_list(["charger", "pendrive"])
print(my_no_dup_list)
