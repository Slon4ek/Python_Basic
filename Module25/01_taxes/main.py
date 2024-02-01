class Property:
    def __init__(self, worth):
        self.__worth = self.set_worth(worth)

    def set_worth(self, worth):
        self.__worth = worth
        return self.__worth

    def get_worth(self):
        return self.__worth

    def tax_calculation(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.__tax = 0.001

    def __str__(self):
        return 'Стоимость квартиры: {worth:,}\nНалог на квартиру: {tax:.2f}'.format(
            worth=super().get_worth(),
            tax=self.tax_calculation()
        )

    def tax_calculation(self):
        tax_amount = self.get_worth() * self.__tax
        return tax_amount


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.__tax = 0.005

    def __str__(self):
        return 'Стоимость машины: {worth:,}\nНалог на машину: {tax:.2f}'.format(
            worth=super().get_worth(),
            tax=self.tax_calculation()
        )

    def tax_calculation(self):
        tax_amount = self.get_worth() * self.__tax
        return tax_amount


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.__tax = 0.002

    def __str__(self):
        return 'Стоимость дачи: {worth:,}\nНалог на дачу: {tax:.2f}'.format(
            worth=super().get_worth(),
            tax=self.tax_calculation()
        )

    def tax_calculation(self):
        tax_amount = self.get_worth() * self.__tax
        return tax_amount


money = int(input('Введите количество денег: '))
print('Введите стоимость имущества:')
apartment_cost = int(input('Квартира: '))
car_cost = int(input('Машина: '))
country_house_cost = int(input('Дача: '))
apartment = Apartment(apartment_cost)
car = Car(car_cost)
country_house = CountryHouse(country_house_cost)
tax_sum = apartment.tax_calculation() + car.tax_calculation() + country_house.tax_calculation()
result = money - tax_sum
if result < 0:
    print('Сумма налога на имущество составляет {}руб.\nВам не хватает {}руб. для уплаты налогов!'.format(
        tax_sum, -result
    ))
else:
    print('Сумма налога на имущество составляет {}руб.\n'
          'Вам хватает денег, чтобы уплатить налоги и спать спокойно :)'.format(tax_sum))
