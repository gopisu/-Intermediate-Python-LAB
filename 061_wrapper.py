from datetime import datetime

x = 0


def wrapper_with_time_logger(func):
    start_time = datetime.now()

    def func_with_wrapper(*args):
        result = func(*args)
        end_time = datetime.now()
        print(end_time - start_time)
        return result

    return func_with_wrapper


def get_sequence(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i)) / 2
        return v


get_sequence = wrapper_with_time_logger(get_sequence)
print(get_sequence(19))
