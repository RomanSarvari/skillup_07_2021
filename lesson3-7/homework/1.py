class Car:
    def __init__(self, **kwargs):
        self.brand = kwargs.get('brand', None)
        self.model = kwargs.get('model', None)
        self.year = kwargs.get('year', None)
        self.engine_volume = kwargs.get('engine_volume', None)
        self.engine_power = kwargs.get('engine_power', None)
        self.acceleration = kwargs.get('acceleration', None)
        self.body_color = kwargs.get('body_color', None)
        self.price = kwargs.get('price', None)

    def set_brand(self, brand):
        self.brand = brand

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_engine_volume(self, engine_volume):
        self.engine_volume = engine_volume

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def set_acceleration(self, acceleration):
        self.acceleration = acceleration

    def set_body_color(self, body_color):
        self.body_color = body_color

    def set_price(self, price):
        self.price = price

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_engine_volume(self):
        return self.engine_volume
    
    def get_engine_power(self):
        return self.engine_power

    def get_acceleration(self):
        return self.acceleration

    def get_body_color(self):
        return self.body_color

    def get_price(self):
        return self.price
    
    def __str__(self) -> str:
        result = ''
        for key, value in self.__dict__.items():
            result += f'{key}: {value}\n'
        return result
    
audi_rs5 = Car(
    brand = 'AUDI',
    model = 'RS5',
    year = '2021',
    engine_volume = '2.9',
    engine_power = '450 horsepowers / 600 N.m torque',
    acceleration = '100 km/h - 3.7 seconds',
    body_color = 'Nardo Grey',
    price = '76.445 USD',
)
print (audi_rs5)