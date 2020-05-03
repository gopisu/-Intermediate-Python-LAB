"""
dodaj metodę pozwalającą na wygodne formatowanie obiektów klasy Cake do postaci tekstu.
Niech zwracany będzie napis składający się z atrybutów kind, name oraz additives

dodaj metodę pozwalającą na dodawanie do klasy napisu.
Ten napis ma być dołączany jako kolejny element na liście additives

zmodyfikuj powyższą metodę tak, aby możliwe było przekazanie na raz większej ilości  dodatków.
Wszystkie one mają być dołączone do listy additives.

zmodyfikuje powyższą metodę tak, że jeśli zostanie ona wykorzystana do dodania zmiennych innych typów,
to wygenerowany zostanie błąd.

przetestuj w/w metody
"""


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        self.additives.show_info()
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("-" * 20)

    def __str__(self):
        return f"{self.name}: {self.kind}, additives: {self.additives}."

    def __iadd__(self, other):
        self.additives += other
        return self


class Additives:
    def __init__(self, list_of_add):
        self.list_of_add = list_of_add.copy()

    def __str__(self):
        result = ""
        for additive in self.list_of_add:
            result += additive + ", "
        return result.rstrip(", ")

    def __iter__(self):
        return iter(self.list_of_add)

    def __len__(self):
        return len(self.list_of_add)

    def show_info(self):
        if len(self.list_of_add) > 0:
            print("Additives:")
            for add in self.list_of_add:
                print("\t\t{}".format(add))

    def __iadd__(self, other):
        if type(other) is str:
            new_additives = self.list_of_add
            new_additives.append(other)
        elif type(other) is list:
            new_additives = self.list_of_add
            new_additives.extend(other)
        else:
            raise Exception(
                f"Method __iadd__ for type {type(other)} and Additives not implemented"
            )
        return Additives(new_additives)


if __name__ == "__main__":

    a = Additives(["chocolate", "nuts"])
    cake01 = Cake("Vanilla Cake", "cake", "vanilla", a, "cream")
    cake01 += "advocat"
    cake01 += ["lemon", "strawberry", "raspberry"]
    print(cake01)
    cake01.show_info()
    b = Additives([])
    cake02 = Cake("Chocolate Cake", "cake", "chocolate", b, "cream")
    cake02.show_info()

    # commented code below will raise exception
    # cake01 += {"additive": "something not tasty"}
