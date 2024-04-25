import sys
from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str = "None") -> Callable:
    """Декоратор для логирования действий функции."""

    def wrapper(func: Callable) -> Callable:
        """Обертка декоратора для функции."""

        @wraps(func)
        def inner(*args: tuple, **kwargs: dict[str, str]) -> Any:
            """Внутренняя обертка для функции, выполняющая логирование."""

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                result = f"error: {e}. Input: {args}, {kwargs}"

            if filename != "None":
                with open(filename, "a") as file:
                    if isinstance(result, str):
                        file.write(f"{str(datetime.now())[:-7]} {func.__name__} {result}\n")
                    else:
                        file.write(f"{str(datetime.now())[:-7]} {func.__name__} ok\n")
            else:
                if isinstance(result, str):
                    print(f"{str(datetime.now())[:-7]} {func.__name__} {result}\n", file=sys.stdout)
                else:
                    print(f"{str(datetime.now())[:-7]} {func.__name__} ok\n", file=sys.stdout)

            return result

        return inner

    return wrapper
