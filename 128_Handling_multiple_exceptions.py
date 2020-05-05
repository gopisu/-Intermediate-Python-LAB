"""
LAB- Reagowanie na różne błędy
Rozpocznij zadanie od rozwiązania z poprzedniej lekcji (jeśli nie masz swojego, możesz skorzystać z mojego)

Obsłuż niezależnie następujące kategorie błędów:

requests.exceptions.ConnectionError - ten błąd łatwo sprowokujesz wpisując nieprawidłowy adres URL

PermissionError - ten błąd uzyskasz zaznaczając atrybut "tylko do odczytu" dla pliku spis.html

FileNotFoundError - może się pojawić w trakcie prób, gdy plik download.tmp nie będzie istniał, a wykonywać będzie się instrukcja kopiowania plików

Exception - ogólna obsługa błędów "na wszelki wypadek"

Obsługując błędy wyświetlaj po prostu komunikaty
"""


import requests
import os
import shutil
from stat import S_IREAD, S_IRGRP, S_IROTH


def remove_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        pass


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
    except requests.exceptions.ConnectionError as e:
        print(f"Url {url} cannot be found. {e}")
    except PermissionError as e:
        print(f"No permission to {temp_file_path}. {e}")
    except FileNotFoundError as e:
        print(f"File to copy doesn't exist: {temp_file_path}. {e}")
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
