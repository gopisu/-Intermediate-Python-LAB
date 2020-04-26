"""Szef cukierni w której pracujesz poprosił Cię o napisanie programu, który koniecznie ma działać obiektowo!

Zaczynamy od zdefiniowania klasy Cake, która ma posiadać atrybuty:

-name opisujące nazwę produktu

-kind opisujący rodzaj wypieku np. torty, ciastka, muffinki, bezy

-taste z głównym smakiem

-addictions - zawierający listę dodatków do danego ciasta, np. owoce, posypki, polewy itp, jeżeli ciasto nie ma dodatków, to będzie to pusta lista

-filling - opis nadzienia, jeżeli dane ciasto nie ma nadzienia, to ma to być pusty napis

-... możesz dodać dalsze własne pomysły :)



Po zdefiniowaniu klasy utwórz kilka instancji tej klasy, to dobry moment na wzbogacenie słownictwa w zakresie słodkości w języku angielskim

Utwórz listę bakery_offer i dodaj do niej instancje wcześniej utworzonych obiektów klasy Cake



Napisz pętlę przechodzącą przez wszystkie instance klasy znajdujące się na liście bakery_offer i wyświetl coś w rodzaju
(dane pochodzące z instancji zostały wytłuszczone):

Today in our offer:

Vanilla Cake - (cake) main taste: vanilla with additives of ['chocolade', 'nuts'], filled with cream

Chocolade Muffin - (muffin) main taste: chocolade with additives of ['chocolade'], filled with

Super Sweet Maringue - (meringue) main taste: very sweet with additives of [], filled with

"""



class Cake:


    def __init__(self, name, kind, taste, additions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additions = additions.copy()
        self.filling = filling

pistacchio_macaroni = Cake("pistacchio macaroni", "macaroni", "sweet", [], "pistacchio")
chocolate_ice_cream = Cake("chocolate ice cream", "ice cream", "sweet", [], "chocolate")
vanilla_pancake = Cake("vanilla pancake", "pancake", "sweet", ["cheese", "chocolate"], "vanilla mousse")

bakery_offer = [pistacchio_macaroni, chocolate_ice_cream, vanilla_pancake]

for cake in bakery_offer:
    print(f'{cake.name} - ({cake.kind}) main taste: {cake.taste} with additives of {cake.additions}, '
          f'filled with {cake.filling}')
