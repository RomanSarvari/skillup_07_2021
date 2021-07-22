# ===================================================================================================================
# Реализуйте класс «Стадион».
# Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость.
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.
# ===================================================================================================================


class Stadium:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.date = kwargs.get('date', None)
        self.country = kwargs.get('country', None)
        self.city = kwargs.get('city', None)
        self.capacity = kwargs.get('capacity', 0.0)
    
    def set_name(self, name):
        self.name = name
    def set_date(self, date):
        self.date = date
    def set_country(self, country):
        self.country = country
    def set_city(self, city):
        self.city = city
    def set_capacity(self, capacity):
        self.capacity = capacity
    
    def get_name(self):
        return self.name
    def get_date(self):
        return self.date
    def get_country(self):
        return self.country
    def get_city(self):
        return self.city
    def get_capacity(self):
        return self.capacity
    
    def __str__(self) -> str:
        result = ''
        for key, value in self.__dict__.items():
            result += f'{key}:{value}\n'
        return result
    
    
donbass_arena = Stadium(
        name = 'Donbass Arena',
        date = '29 August 2009',
        country = 'Ukraine',
        city = 'Donetsk',
        capacity = '52667',
    )

print(donbass_arena)