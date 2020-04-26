class Cake:
    known_types = ['cake', 'muffin', 'ice cream', 'macaroni', 'pancake', 'christmas', 'pretzel', 'other']
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling, gluten_free=False):
        self.name = name
        self.kind = kind if kind in self.known_types else "other"
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free

    def show_additives(self):
        if self.additives and self.additives is not []:
            print("Additives:")
            for additive in self.additives:
                print(f"     {additive}")

    def show_info(self):
        print(f"{self.name.upper()} \nKind:   {self.kind}\nTaste:  {self.taste}")
        self.show_additives()
        print(f"Filling: {self.filling}")
        print(f"Alergies info: Gluten free") if self._Cake__gluten_free is True else print("Alergies info: Conatins GLUTEN")
        print("--------------------")

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives_list):
        for additive in additives_list:
            self.additives.append(additive)


pistacchio_macaroni = Cake("pistacchio macaroni", "macaroni", "sweet", [], "pistacchio", gluten_free=True)
chocolate_ice_cream = Cake("chocolate ice cream", "ice cream", "sweet", [], "chocolate")
vanilla_pancake = Cake(
    "vanilla pancake", "pancake", "sweet", ["cherry", "chocolate"], "vanilla mousse"
)


pistacchio_macaroni.add_additives(["chocolate", "cinnamon"])
pistacchio_macaroni.set_filling("cherry&blueberry")
vanilla_pancake.add_additives(["nuts"])
vanilla_pancake.set_filling("cheesecake tasing filling")

cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')

bakery_offer = [pistacchio_macaroni, cake04, chocolate_ice_cream, vanilla_pancake]

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()

print(isinstance(cake04, Cake))
print(type(cake04))

print(vars(cake04))
print(vars(Cake))

print('-'*20)
print(dir(cake04))
print(dir(Cake))

