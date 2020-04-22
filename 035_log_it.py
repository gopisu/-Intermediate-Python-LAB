'''ZADANIE 2

Piszesz funkcję log_it, która ma zapisać w pliku tekstowym
np. c:\temp\log_it.txt przesłane do funkcji argumenty.
Funkcja będzie wykorzystywana w innych miejscach programu,
gdzie będzie wywoływana w strategicznych momentach, dokumentując działanie programu.
Jeśli nie masz innych pomysłów to zadbaj o to aby:

można było przesłać dowolną ilość argumentów

podczas dopisywania informacji do pliku poszczególne argumenty rozdzielaj spacją

na końcu w pliku zapisz ENTER, aby kolejne wywołanie funkcji dopisywało od nowej linijki'''
from datetime import datetime

log_file ="log_it1.txt"

def log_it(*args):
    with open(log_file, "a") as file:
        file.write(f'{datetime.now()}')
        for pos, arg in enumerate(args):
            file.write(f"{pos + 1}: {arg} ")
        file.write('\r')

log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')

with open(log_file, 'rb') as f:
    print(f.read())

