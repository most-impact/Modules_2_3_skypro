from datetime import datetime

from src.decorators import log


def test_log() -> None:
    @log("test_log.txt")
    def test_function_1(x: int | float, y: int | float) -> float:
        return x / y

    test_function_1(1, 1)
    test_function_1(5, 2)

    with open("test_log.txt", "r") as file:
        lines = file.readlines()
        assert lines[-2].strip() == f"{str(datetime.now())[:-7]} " + "test_function_1 ok"
        assert lines[-1].strip() == f"{str(datetime.now())[:-7]} " + "test_function_1 ok"

    try:
        test_function_1(1, 0)
    except ZeroDivisionError:
        pass

    with open("test_log.txt", "r") as file:
        lines = file.readlines()
        first_line = lines[-1].strip()
        assert (
            first_line == f"{str(datetime.now())[:-7]} " + "test_function_1 error: division by zero. Input: (1, 0), {}"
        )
