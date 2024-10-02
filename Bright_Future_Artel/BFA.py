from datetime import datetime


def validate_record(name, birth_date):
    """Проверяет корректность даты рождения.

        Аргументы:
        name -- имя сотрудника
        birth_date -- дата рождения в виде строки

        Возвращает:
        True, если дата корректна и соответствует формату 'ДД.ММ.ГГГГ'.
        False, если формат некорректен.
        """

    try:
        datetime.strptime(birth_date, '%d.%m.%Y')
        return True
    except ValueError:
        print(f'Некорректный формат даты в записи: {name}, {birth_date}')
        return False


def process_people(data):
    """Обрабатывает список сотрудников и подсчитывает количество корректных и некорректных записей.

        Аргументы:
        data -- список кортежей с именами и датами рождения

        Возвращает:
        Словарь с количеством корректных и некорректных записей.
        """
    good_count = 0   # Счетчик корректных записей
    bad_count = 0   # Счетчик некорректных записей

    for name, birth_date in data:
        if validate_record(name, birth_date):
            good_count += 1   # Увеличиваем счетчик корректных записей
        else:
            bad_count += 1   # Увеличиваем счетчик некорректных записей

    return {'good': good_count, 'bad': bad_count}


def main():
    data = [
        ('Акакій Башмачкинъ', '23 марта 1791 года'),
        ('Яков Степанов', 'Двадцать шестое июля 1971'),
        ('Потап Алексеев', '16.09.1990'),
        ('Евгений Женин', '5 декабря 1984'),
        ('Кондрат Александров', '18.01.1994')
    ]

    result = process_people(data)
    print(f'Корректных записей: {result["good"]}')
    print(f'Некорректных записей: {result["bad"]}')


if __name__ == '__main__':
    main()