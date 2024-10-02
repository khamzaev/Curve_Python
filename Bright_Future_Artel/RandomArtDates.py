from datetime import datetime
from random import sample


def choose_days():
    """Выбирает случайные дни для занятий рисованием в первой половине месяца."""
    # Определяем диапазон дат первой половины месяца (1-15).
    first_month_half = list(range(1, 16))   # от 1 до 15 включительно

    # Выбор трёх случайных чисел:
    random_days = sample(first_month_half, k=3)

    # Cортировка этих чисел по возрастанию:
    sorted_days = sorted(random_days)

    # Получаем сегодняшнюю дату.
    # На её основе будут генерироваться даты для занятий:
    now = datetime.now()

    # Генерируем даты для занятий:
    for i in range(3):   # Цикл от 0 до 2, чтобы получить три занятия
        # Генерируем дату занятия, подменяя номер дня в сегодняшней дате.
        practice_day = now.replace(day=sorted_days[i]).strftime("%d.%m.%Y")
        print(f'{i + 1}-е занятие: {practice_day}')   # Печатаем номер занятия


choose_days()