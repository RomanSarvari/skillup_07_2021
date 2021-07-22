# ====================================================================================================================
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег (доллары, евро, гривны и т.д.) 
# и поле для хранения копеек (центы, евроценты, копейки и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.
# ====================================================================================================================

class Money:
    def __init__(self, **kwargs):
        self.currency = kwargs.get('currency', None)
        self.symbol = kwargs.get('symbol', None)
        self.integrate = kwargs.get('integrate', 0)
        self.fraction = kwargs.get('fraction', 0)

    def __str__(self) -> str:
        item = ''
        for key, value in self.__dict__.items():
            item += f'{key}:{value}\n'
        return item
    
    def set_integrate(self, integrate):
        self.integrate = integrate
    
    def get_integrate(self):
        return self.integrate

    def set_fraction(self, fraction):
        self.fraction = fraction
    
    def get_fraction(self):
        return self.fraction

class Hryvnya(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Dolar(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Euro(Money):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

hrivnya = Hryvnya(
    currency = 'UAH',
    symbol = '₴',
    integrate = 0,
    fraction = 0,
)

dolar = Dolar(
    currency = 'USD',
    symbol = '$',
    integrate = 10000,
    fraction = 78,
)

euro = Euro(
    currency = 'EUR',
    symbol = '€',
    integrate = 5000,
    fraction = 54,
)

print(hrivnya)

print(dolar)

print(euro)

hrivnya.set_fraction(77)
hrivnya.set_integrate(560000)
print(hrivnya)