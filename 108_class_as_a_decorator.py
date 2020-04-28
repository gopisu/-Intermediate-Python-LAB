"""
Na zewnątrz klasy została zdefiniowana inna funkcja, która będzie wykorzystywana w internetowym systemie zamówień wypieków. Oto ona:


Problem polega na tym, że podczas składania zamówienia klient może dobierać dodatki do wypieku. Niektóre z wypieków
już te dodatki posiadają, więc można doprowadzić do tego, że wśród składników jedna
pozycja znajdzie się kilka razy. Zobacz, jak aktualnie zachowuje się funkcja, która dodaje czekoladę i orzechy:

Rozwiążesz ten problem definiując dekorator, który również będzie klasą,
 a następnie oznaczysz tym dekoratorem funkcję add_extra_additives
"""


class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("-" * 20)

    def add_additives(self, additives):
        self.additives.extend(additives)


cake01 = Cake("Vanilla Cake", "cake", "vanilla", ["chocolade", "nuts"], "cream")


class NoDuplicates:
    def __init__(self, function):
        self.function = function

    def __call__(self, cake, new_additives):
        additives_to_add = [
            item for item in new_additives if item not in cake.additives
        ]
        self.function(cake, additives_to_add)


@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


add_extra_additives(cake01, ["strawberries", "sugar-flowers"])
cake01.show_info()
add_extra_additives(cake01, ["strawberries", "sugar-flowers", "chocolade", "nuts"])
cake01.show_info()
