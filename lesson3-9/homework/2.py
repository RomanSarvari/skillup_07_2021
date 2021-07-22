# ====================================================================================================================
# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования:
# реализуйте класс Frigate (содержит информацию о фрегате) 
# класс Destroyer (содержит информацию об эсминце)
# класс Cruiser (содержит информацию о крейсере)
# Каждый из классов должен содержать необходимые для работы методы.
# ====================================================================================================================

class Ship:
    def __init__(self, **kwargs):
        self.type = kwargs.get('type', None)
        self.name = kwargs.get('name', None)
        self.country = kwargs.get('country', None)
        self.tonnage = kwargs.get('tonnage', 0.0)
        self.length = kwargs.get('length', 0.0)
        self.width = kwargs.get('width', 0.0)
        self.speed = kwargs.get('speed', 0.0)
        self.crew = kwargs.get('crew', 0.0)
    
    def __str__(self) -> str:
        item = ''
        for key, value in self.__dict__.items():
            item += f'{key}:{value}\n'
        return item

class Frigate(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.accost = kwargs.get('accost', None)
        self.belonging = kwargs.get('belonging', None)

    def tagline(self):
        print('{}. Welcome!!!'.format(self.accost), '\n')

class Destroyer(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.power = kwargs.get('power', 0.0)
        self.aviation = kwargs.get('aviation', None)
    
    def possibilities(self):
        print('We have {} and artillery'.format(self.aviation), '\n')

class Cruiser(Ship):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.armament = kwargs.get('armament', None)
        self.mover = kwargs.get('mover', None)

    def presentation(self):
        print('This Cruiser from {} and have onboard {}'.format(self.country, self.armament), '\n')

hetman_sahaydachniy = Frigate(
    type = 'Frigate',
    name = 'Hetman Sahaydachniy',
    country = 'Ukraine',
    tonnage = '3650 tons',
    length = '123.5 meters',
    width = '14.3 meters',
    speed = '32 knots',
    crew = '180 peoples',
    accost = 'Glory to Ukraine! Glory to the heroes!',
    belonging = 'Ukrainian Navy',
)

uss_ross = Destroyer(
    type = 'Destroyer',
    name = 'USS Ross (DDG-71)',
    country = 'USA',
    tonnage = '8775 tons',
    length = '153.92 meters',
    width = '20.1 meters',
    speed = '32 knots',
    crew = '337 peoples',
    power = '108000 horsepowers',
    aviation = 'Helicopter - SH-60 LAMPS',
)

hms_shannon = Cruiser(
    type = 'Cruiser',
    name = 'HMS Shannon',
    country = 'Great Britain',
    tonnage = '5670 tons',
    length = '90.5 meters',
    width = '16.46 meters',
    speed = '12.25 knots',
    crew = '452 peoples',
    armament = 'artillery',
    mover = '1 propeller and sails',
)

print(hetman_sahaydachniy)
hetman_sahaydachniy.tagline()

print(uss_ross)
uss_ross.possibilities()

print(hms_shannon)
hms_shannon.presentation()