from typing import Callable
import re


def generator_numbers(text: str):
    pattern = r'[\d,]+(?:\.\d+)?'
    numbers = re.findall(pattern, text)
    for num in numbers:
        num = num.replace(',', '')
        if num:
            yield float(num)


def sum_profit(text: str, func: Callable):
    total_profit = 0

    for profit in generator_numbers(text):
        total_profit += profit

    return total_profit


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")










