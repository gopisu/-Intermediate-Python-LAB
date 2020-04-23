"""Oto przykład niezbyt dobrze napisanej funkcji wyliczającej wartość w ciągu Finobacciego:

def fib(n):

    if n <= 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)

    return result

Funkcja zamiast wyliczać wartości od najmniejszych do największych i korzystać z poprzednich wyników
do wyznaczenia kolejnych wartości, każdorazowo wyznacza poprzednie wartości. Zoptymalizuj funkcję metodą cache,
(a jak masz ochotę to również przepisz funkcję do lepszej postaci)

przygotuj funkcję do testu pomiaru czasu

zaimportuj moduł time

w zmiennej start zapisz aktualny czas

napisz pętlę wyliczającą wartość ciągu zaczynając od 1, a kończąc na sensownej na Twoim komputerze wartości,
na którą masz cierpliwość doczekać (u mnie to do około 33-37)
każdorazowo wyświetl numer iteracji w pętli i różnicę między czasem bieżącym, a czasem ze zmiennej start
zapamiętaj czas trwania obliczeń

zoptymalizuj funkcję"""


import time
import functools


@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result


start = time.time()

for i in range(36):
    result = fib(i)
    print(f'{i}. {round(time.time()-start, 3)}')

