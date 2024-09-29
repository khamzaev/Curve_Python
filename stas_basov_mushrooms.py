class MushroomsCollector:
    def __init__(self):
    # Проверьте, нет ли здесь ошибки:
        self.mushrooms = []

    # Исправьте ошибку в этом методе.
    def is_poisonous(self, mushroom_name):
        poisonous_mushrooms = ['Мухомор', 'Поганка']
        if mushroom_name in poisonous_mushrooms:
            return True
        return False

    # Допишите метод.
    def add_mushroom(self, mushroom_name):
        if self.is_poisonous(mushroom_name):
            print('Нельзя добавить ядовитый гриб')
        else:
            self.mushrooms.append(mushroom_name)
            print(f'Добавлен гриб: {mushroom_name}')

    # Напишите магический метод __str__,
    def __str__(self):
        return ', '.join(self.mushrooms)


# Пример запуска для самопроверки
collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)
print(collector_2)
