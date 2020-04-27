import glob
import os
import pickle
import types
from templates import html


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
            else print(f"Error: {self.kind.upper()} can't be decorated with text. ")
        )

    def save_to_file(self, path):
        with open(os.path.join(path, f"{self.name}.bakery"), "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def read_from_file(cls, path):
        with open(path, "rb") as file:
            cake = pickle.load(file)
        cls.bakery_offer.append(cake)
        return cake

    @staticmethod
    def get_bakery_files(directory):
        return glob.glob(f"{directory}/*.bakery")


pistacchio_maccaroni = Cake(
    "pistacchio macaroni",
    "macaroni",
    "",
    [],
    "pistacchio",
    gluten_free=True,
    text='"I like"',
)
chocolate_ice_cream = Cake("chocolate ice cream", "ice cream", "sweet", [], "chocolate")
vanilla_cake = Cake(
    "vanilla cake", "cake", "sweet", ["cherry", "chocolate"], "vanilla mousse"
)
waffle = Cake("Cocoa waffle", "waffle", "cocoa", [], "cocoa")


print(Cake.get_bakery_files("bakery"))
vanilla_cake.save_to_file("bakery/")
chocolate_ice_cream.save_to_file("bakery/")
pistacchio_maccaroni.save_to_file("bakery/")
waffle.save_to_file("bakery/")
vanilla_cake2 = Cake.read_from_file("bakery/vanilla cake.bakery")

pistacchio_maccaroni.add_additives(["chocolate", "cinnamon"])
pistacchio_maccaroni.set_filling("cherry&blueberry")
vanilla_cake.add_additives(["nuts"])
vanilla_cake.set_filling("cheesecake tasing filling")
vanilla_cake.text = "Happy birthday"
waffle.text = "I like waffles"


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


# practice adding method to class dynamically
def export_1_cake_to_html(obj, path):
    with open(path, "w") as f:
        content = html.menu_template.format(
            obj.name, obj.kind, obj.taste, obj.additives, obj.filling
        )
        f.write(content)


def export_all_cakes_to_html(cls, path):
    with open(path, "w") as f:
        content = ""
        for obj in cls.bakery_offer:
            content += html.menu_template.format(
                obj.name, obj.kind, obj.taste, obj.additives, obj.filling
            )
        f.write(content)


def export_this_cake_to_html(self, path):
    with open(path, "w") as f:
        content = html.menu_template.format(
            self.name, self.kind, self.taste, self.additives, self.filling
        )
        f.write(content)


Cake.export_1_cake_to_html = types.MethodType(export_1_cake_to_html, Cake)
Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
for item_in_offer in Cake.bakery_offer:
    item_in_offer.export_this_cake_to_html = types.MethodType(
        export_this_cake_to_html, item_in_offer
    )

for item_in_offer in Cake.bakery_offer:
    item_in_offer.export_this_cake_to_html(
        f"exported_html/{item_in_offer.name.replace(' ', '_')}.html"
    )

Cake.export_all_cakes_to_html("exported_html/all.html")
