class Cake:
    def __init__(self, name, kind, taste, additions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additions = additions.copy()
        self.filling = filling

    def show_additives(self):
        if self.additions is not []:
            print("Additives:")
            for additive in self.additions:
                print(f"     {additive}")

    def show_info(self):
        print(f"{self.name.upper()} \nKind:   {self.kind}\nTaste:  {self.taste}")
        self.show_additives()
        print(f"Filling: {self.filling}")
        print("--------------------")

    def set_filling(self, filling):
        self.filling = filling

    def add_additions(self, additions_list):
        for addition in additions_list:
            self.additions.append(addition)


pistacchio_macaroni = Cake("pistacchio macaroni", "macaroni", "sweet", [], "pistacchio")
chocolate_ice_cream = Cake("chocolate ice cream", "ice cream", "sweet", [], "chocolate")
vanilla_pancake = Cake(
    "vanilla pancake", "pancake", "sweet", ["cherry", "chocolate"], "vanilla mousse"
)


pistacchio_macaroni.add_additions(["chocolate", "cinnamon"])
pistacchio_macaroni.set_filling("cherry&blueberry")
vanilla_pancake.add_additions(["nuts"])
vanilla_pancake.set_filling("cheesecake tasing filling")

pistacchio_macaroni.show_info()
vanilla_pancake.show_info()

bakery_offer = [pistacchio_macaroni, chocolate_ice_cream, vanilla_pancake]
