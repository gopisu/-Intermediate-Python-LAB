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


pistacchio_macaroni = Cake(
    "pistacchio macaroni",
    "macaroni",
    "sweet",
    [],
    "pistacchio",
    gluten_free=True,
    text='"I like you"',
)
chocolate_ice_cream = Cake("chocolate ice cream", "ice cream", "sweet", [], "chocolate")
vanilla_pancake = Cake(
    "vanilla pancake", "pancake", "sweet", ["cherry", "chocolate"], "vanilla mousse"
)


pistacchio_macaroni.add_additives(["chocolate", "cinnamon"])
pistacchio_macaroni.set_filling("cherry&blueberry")
vanilla_pancake.add_additives(["nuts"])
vanilla_pancake.set_filling("cheesecake tasing filling")

cake04 = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa")

bakery_offer = [pistacchio_macaroni, cake04, chocolate_ice_cream, vanilla_pancake]

print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()

print(isinstance(cake04, Cake))
print(type(cake04))

print(vars(cake04))
print(vars(Cake))

print("-" * 20)
print(dir(cake04))
print(dir(Cake))

"""Do klasy należy dodać atrybut ukryty __text. Odpowiada on za napis umieszczony na torcie.

W funkcji __init__ przyjmij nowy argument text

Zapisz go w zmiennej __text przeprowadzając kontrolę: napis można zapisać w instancji tylko jeżeli kind jest 'cake' 
lub text jest napisem pustym. Jeśli te warunki nie są spełnione wyświetl diagnostyczny komunikat (print dla Ciebie, żeby było wiadomo co się dzieje)

Dodaj ukrytą funkcję __get_text, która będzie zwracać wartość zapisaną w __text

Dodaj ukrytą funkcje __set_text, która przyjmie dodatkowy argument new_text i zaktualizuje atrybut
 __text tylko dla wyrobów z kind 'cake'

Zdefiniuj właściwość Text korzystającą z powyższych funkcji.

Tworząc obiekty klasy Cake przekaż dodatkowy argument text - umieść napisy puste lub inne typowo  
"tortowe", część poprawnych (czyli napis na torcie) i część niepoprawnych (np. napis na waflu)

Wyświetl wszystkie informacje o wszystkich wypiekach

Spróbuj wstawić do właściwości Text napis na torcie i na innym wypieku nietortowym - 
prześledź poprawność tych operacji ponownie wyświetlając ofertę cukierni"""
