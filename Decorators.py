from typing import Callable
from datetime import datetime


def log_func(old_function: Callable, ):
    def saving_log(new_log):
        with open(f'log_file.txt', 'a', encoding='UTF-8') as f:
            f.write(new_log)

    def new_functions(*args, **kwargs):
        start = datetime.now().strftime('%d-%m-%Y в %H:%M:%S')
        name = old_function.__name__
        result = old_function(*args, **kwargs)
        log = (f'Функция {name} \nЗапустиласть {start} \nС аргументами {args} и {kwargs} \
               \nИ получила результат {result}\n\n')
        print(log)
        saving_log(log)
        return result
    return new_functions


def save_log(path):
    def logger_func(old_function: Callable):
        def new_function(*args, **kwargs):
            start = datetime.now().strftime('%d-%m-%Y в %H:%M:%S')
            name = old_function.__name__
            result = old_function(*args, **kwargs)
            new_log = (f'Функция {name} \nЗапустиласть {start} \nС аргументами {args} и {kwargs} \
                   \nИ получила результат {result} \nЗапись сохранилась в {path}\n')
            print(new_log)
            with open(f'{path}log_file.txt', 'a', encoding='UTF-8') as f:
                f.write(new_log)
            return result
        return new_function
    return logger_func


if __name__ == '__main__':

    @log_func
    def multiplier(a, b):
        return a * b

    @save_log('D:\\')
    def summa(c, d):
        return c + d

    multiplier(5, 4)
    summa(5, 9)
