"""Napisz blok try/except/else/finally, który:
w bloku try
jeśli istnieje plik tmpfile_path to go usunie
korzystając z funkcji save_url_to_file pobierze stronę spod adresu url do pliku tmpfile_path
skopiuje plik tmpfile_path do file_path

w przypadku błędów wykonaj blok except, a w nim:
wyświetli informacje o błędzie, w tym szczegóły wyjątku

w bloku else  wyświetl komunikat o sukcesie
w bloku finally
usuń plik tmpfile_path jeśli istnieje
wyświetl komunikat
Przetestuj działanie programu z poprawnym i błędnym adresem url. Sprawdzaj wyniki wyświetlan"""

import requests
import os
import shutil


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print(f"The file {path} does not exist")


def copy_file(original, target):
    if os.path.exists(original):
        shutil.copyfile(original, target)
    else:
        print(f"The file {original} does not exist")


def save_url_to_file(url, file_path):
    r = requests.get(url, stream=True)
    with open(file_path, "wb") as f:
        f.write(r.content)


def create_file_path(file, dir):
    return os.path.join(dir, file)


def save_url_to_temp_and_copy_to_target(url, temp_file_path, target_file_path):
    try:
        remove_file(temp_file_path)
        save_url_to_file(url, temp_file_path)
        copy_file(temp_file_path, target_file_path)
    except Exception as e:
        print(e)
    else:
        print(f"Successfully saved url to {target_file_path}")
    finally:
        remove_file(temp_file_path)


url = "http://www.mobilo24.eu/spis/"
dir = "temp"
tmpfile = "download.tmp"
file = "spis.html"

tmpfile_path = create_file_path(file=tmpfile, dir=dir)
file_path = create_file_path(file=file, dir=dir)

save_url_to_temp_and_copy_to_target(
    url=url, temp_file_path=tmpfile_path, target_file_path=file_path
)
