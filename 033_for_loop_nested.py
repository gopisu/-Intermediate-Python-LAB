"""Na przekręcie z wpłatomatem z poprzedniego zadania postanawiasz wraz ze swoim szefem otworzyć linie lotnicze "Flying Python". Linie będą krajowe. Oto wykaz portów lotniczych:


1. Zbuduj listę tupletów symbolizujących port początkowy i końcowy. Wykonaj połączenie każdy-z-każdym

2. Wyeliminuj z powyższej listy połączenie z portu do tego samego portu

3. Ponieważ połączenie z A do B dubluje się z połączeniem z B do
A - wygeneruj możliwe połączenia krajowe pomijając takie zdublowane trasy.

4. Policz ilość generowanych połączeń w krokach 1,2,3"""

ports = [
    "WAW",
    "KRK",
    "GDN",
    "KTW",
    "WMI",
    "WRO",
    "POZ",
    "RZE",
    "SZZ",
    "LUZ",
    "BZG",
    "LCJ",
    "SZY",
    "IEG",
    "RDO",
]

all = [(port_a, port_b) for port_a in ports for port_b in ports]
all_connections = [
    (port_a, port_b) for port_a in ports for port_b in ports if port_a != port_b
]
all_connections_filtered = []

for a, b in all_connections:
    if (b, a) not in all_connections_filtered:
        all_connections_filtered.append((a, b))

print(all_connections)
print(all_connections_filtered)

print(len(all))
print(len(all_connections))
print(len(all_connections_filtered))
