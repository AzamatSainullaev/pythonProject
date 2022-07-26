# HW:
# Создать классы машин допустим (Bmw, Mercedes)
# определить такие атрибуты как (title, model, weight, hp, nm, max_speed, color)
# создать метод start_engine() -> output title + model engine started!
# создать метод stop_engine() -> output title + model engine stoped!
# создать метод info() -> All Info

class Car:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    def start_engine(self):
        print(f'Engine on {self.title} {self.model} started!')

    def stop_engine(self):
        print(f'Engine on {self.title} {self.model} stoped!')

    def info(self):
        print(f'Title:{self.title}\nModel:{self.model}\nWeinght{self.weight}'
              f"Hp:{self.hp}\nNm:{self.nm}\nMax_speed:{self.max_speed}\nColor{self.color}")


mers = Car('Mersedes', 'CLS53', '4988', '435', '48', '250', 'blue')
mers.start_engine()
mers.stop_engine()
mers.info()

BMW = Car('BMW', 'M8', '2385', '460', '68', '250', 'Green')
BMW.start_engine()
BMW.stop_engine()
BMW.info()