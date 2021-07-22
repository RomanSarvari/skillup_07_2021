# ====================================================================================================
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования:
# реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере),
# класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.
# ====================================================================================================

class Device:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.price = kwargs.get('price', 0.0)
        self.made = kwargs.get('made', None)
        self.date = kwargs.get('date', None)
    def __str__(self) -> str:
        result = ''
        for key, value in self.__dict__.items():
            result += f'{key}:{value}\n'
        return result

class CoffeeMachine(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.pressure = kwargs.get('pressure', None)
    def coffe_make(self):
        print ('If you want a coffe, I will do it for you')

class Blender(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rpm = kwargs.get('rpm', None)
        self.volume = kwargs.get('volume', 0.0)
    def whip_whip (self):
        print ('I can whiping something for you at {}'.format(self.rpm))

class Meatgrinder(Device):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.material = kwargs.get('material', None)
        self.power_usage = kwargs.get('power', None)
    def grinding(self):
        print ('By the way, I consume electricians in {}'.format(self.power_usage))

coffemachine_1 = CoffeeMachine(
    name= 'Coffemachine Nespresso C30 Essenza Mini',
    price= '4277 UAH',
    made = 'Made in Ukraine',
    date = 'Manufactured 22/07/2021',
    type = 'capsule type',
    pressure = '19 Bar',
)

blender_1 = Blender(
    name = 'Braun MQ 7045 X',
    price = '2999 UAH',
    made = 'Romania',
    date = 'Manufactured 15/06/2021',
    rpm = '13300 rpm/min',
    volume = '1.25 L',
)

meatgrinder_1 = Meatgrinder(
    name = 'Bosch MFW3640A',
    price = '3399 UAH',
    made = 'Poland',
    date = 'Manufactured 23/03/2021',
    material = 'plastic',
    power = '1600 Watt',
)

coffemachine_1.coffe_make()
print(coffemachine_1)

blender_1.whip_whip()
print(blender_1)

meatgrinder_1.grinding()
print(meatgrinder_1)
