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

all = ((port_a, port_b) for port_a in ports for port_b in ports)
all_connections = (
    (port_a, port_b) for port_a in ports for port_b in ports if port_a != port_b
)
all_connections_filtered = (
    (port_a, port_b) for port_a in ports for port_b in ports if port_a > port_b
)

print(all_connections)
print(all_connections_filtered)

number_of_all = 0
for connection in all:
    print(connection)
    number_of_all += 1


number_of_all_connections = 0
for connection in all_connections:
    print(connection)
    number_of_all_connections += 1

number_of_all_connections_filtered = 0
for connection in all_connections_filtered:
    print(connection)
    number_of_all_connections_filtered += 1

print(number_of_all)
print(number_of_all_connections)
print(number_of_all_connections_filtered)
