class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10


    # Реализуйте методы get_price() и set_discount().
    def get_price(self,original_price):
        discount_multiplier = (100 - self.__discount) / 100
        discounted_price = original_price * discount_multiplier
        return round(discounted_price, 2)


    def set_discount(self, new_discount):
        if new_discount > 80:
            self.__discount = 80
            print(f'Скидка не может превышать 80%. Установлена скидка 80%.')
        elif new_discount < 0:
            self.__discount = 0
            print(f'Скидка не может быть отрицательной. Установлена скидка 0%.')
        else:
            self.__discount = new_discount
            print(f'Скидка обновлена до {self.__discount}%.')


customer = Customer("Иван Иванович")
customer.get_price(100)
customer.set_discount(20)
customer.get_price(100)