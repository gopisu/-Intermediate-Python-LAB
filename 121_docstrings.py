class Cake:
    """Defines an item in bakery offer and keeps a list of all created objects"""

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """
        :param name: string, name of item in offer
        :param kind: string, ie. cookie, muffin, etc.
        :param taste: string, is it sweet or salty
        :param additives: list with strings or [], extra ingredients
        :param filling: string or None, what kind of filling it containes
        :return: Cake object"""
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

    @property
    def full_name(self):
        """Prints upper case name and kind of an offer item"""
        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


help(Cake)
help(Cake.__init__)
help(Cake.full_name)
