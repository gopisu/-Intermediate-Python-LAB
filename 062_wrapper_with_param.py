import os
from datetime import datetime


def logger_with_path(file_to_log_into):
    def logger(func):
        def func_with_wrapper(*arg):
            result = func(*arg)
            with open(file_to_log_into, "a") as file:
                file.write("\n")
                file.write(
                    f'Action {func.__name__} executed on {path} on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
                )
                file.write("\n")
                file.write("--" * 20)
            return result

        return func_with_wrapper

    return logger


path = r"c:\temp\dummy_file.txt"


@logger_with_path(r"c:\temp\dummy_file_create.txt")
def create_file(path):
    print("creating file {}".format(path))
    open(path, "w+")


@logger_with_path(r"c:\temp\dummy_file_delete.txt")
def delete_file(path):
    print("deleting file {}".format(path))
    os.remove(path)


create_file(r"c:\temp\dummy_file.txt")
delete_file(r"c:\temp\dummy_file.txt")
create_file(r"c:\temp\dummy_file.txt")
delete_file(r"c:\temp\dummy_file.txt")
