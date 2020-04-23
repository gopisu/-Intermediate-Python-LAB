"""Napisz funkcję calculate_paint, która:

przyjmuje argument efficency_ltr_per_m2
- określającą ile farby trzeba do pomalowania metra kwadratowego

przyjmuje dowolną ilość kolejnych argumentów odpowiadających
za powierzchnie do pomalowania dla pokoi mieszkania, które ma być pomalowane
funkcja ma zwracać informację o ilości potrzebnej farby

Przetestuj funkcję na dwa sposoby:
przekazując powierzchnie do pomalowania w poszczególnych pokojach po prostu po przecinku wywołując funkcję
definiując listę z powierzchniami, a następnie przekazując do funkcji tą listę"""


def calculate_paint(efficiency_per_ltr_per_m2, *rooms_sizes_in_meters):
    return sum(rooms_sizes_in_meters) * efficiency_per_ltr_per_m2


print("We need", calculate_paint(1, 100), "l of paint for room of 100 m2")
print("We need", calculate_paint(1, 50, 50), "l of paint for two rooms of 50 m2")

rooms_1 = [50, 50]
rooms_2 = [1, 1, 1, 1, 1]

print(
    "We need",
    calculate_paint(1, *rooms_1),
    "l of paint for",
    len(rooms_1),
    "rooms of the sizes",
    rooms_1,
)
print(
    "We need",
    calculate_paint(1, *rooms_2),
    "l of paint for",
    len(rooms_2),
    "rooms of the sizes",
    rooms_2,
)
