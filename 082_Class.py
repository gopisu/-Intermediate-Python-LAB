class Cake:
    known_types = [
        "cake",
        "muffin",
        "ice cream",
        "macaroni",
        "pancake",
        "christmas",
        "pretzel",
        "other",
    ]
    bakery_offer = []

    def __init__(
        self, name, kind, taste, additives, filling, text="", gluten_free=False
    ):
        self.name = name
        self.kind = kind if kind in self.known_types else "other"
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.__gluten_free = gluten_free
        self.text = text
        self.bakery_offer.append(self)

    def show_additives(self):
        if self.additives and self.additives is not []:
            print("Additives:")
            for additive in self.additives:
                print(f"     {additive}")

    def show_info(self):
        print(f"{self.name.upper()} \nKind:   {self.kind}\nTaste:  {self.taste}")
        self.show_additives()
        print(f"Filling: {self.filling}")
        print(f"Text: {self.text}") if self.text not in ["", None] else True
        print(f"Alergies info: Gluten free") if self.__gluten_free is True else print(
            "Alergies info: Conatins GLUTEN"
        )
        print("--------------------")

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives_list):
        for additive in additives_list:
            self.additives.append(additive)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        self.__text = (
            new_text
            if self.kind == "cake" or new_text == ""
            else print(
                f"Tries to decorate {self.kind} with text: {new_text}. "
                f"Only cakes are decoratied with text"
            )
        )


pistacchio_maccaroni = Cake(
    "pistacchio macaroni",
    "macaroni",
    "sweet",
    [],
    "pistacchio",
    gluten_free=True,
    text='"I like maccaroni"',
)
chocolate_ice_cream = Cake("chocolate ice cream", "ice cream", "sweet", [], "chocolate")
vanilla_cake = Cake(
    "vanilla cake", "cake", "sweet", ["cherry", "chocolate"], "vanilla mousse"
)


pistacchio_maccaroni.add_additives(["chocolate", "cinnamon"])
pistacchio_maccaroni.set_filling("cherry&blueberry")
vanilla_cake.add_additives(["nuts"])
vanilla_cake.set_filling("cheesecake tasing filling")
vanilla_cake.text = 'Happy birthday'

waffle = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa")
waffle.text = 'I like waffles'

bakery_offer = [pistacchio_maccaroni, waffle, chocolate_ice_cream, vanilla_cake]

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()

print(isinstance(waffle, Cake))
print(type(waffle))

print(vars(waffle))
print(vars(Cake))

print("-" * 20)
print(dir(waffle))
print(dir(Cake))