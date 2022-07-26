from cars.create_car import Car
from cars.get_car_info import get_car_info

Bmw = Car('BMW', 'i8', "w12", 800, 400)

print(Bmw.start_engine())
print(Bmw.stop_engine())
get_car_info(Bmw)