import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    # Знаходимо всі дійсні числа, які відокремлені пробілами
    pattern = r'(?<=\s)(-?\d+(?:\.\d+)?)(?=\s)'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    # Обчислюємо суму всіх чисел, що повертає генератор
    return sum(func(text))

# Приклад використання:
text = ("Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів.")

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
