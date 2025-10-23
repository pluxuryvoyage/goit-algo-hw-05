import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]: # генератор знаходить та повертає всі дійсні числа з тексту.
   pattern = r' \d+(?:\.\d+)?' # регулярний вираз для пошуку дійсних чисел
   matches = re.finditer(pattern, text) # знаходимо всі числа у тексті 
   for match in matches:
        yield float(match.group()) # повертаємо кожне число яке знайшли як float

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float: # ця функція обчислює загальну суму всіх чисел у тексті через переданий генератор
    return sum(func(text)) # підсумовуємо всі числа через вбудовану функцію sum

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин:" \
    " 1000.01 як основний дохід, доповнений додатковими надходженнями" \
    " 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers) # виведення результату у змінну total income
print(f"Загальний дохід: {total_income}")