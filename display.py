import test
import Car

car1 = Car.Car("I20", "Sportz", "2017")

class_content = dir(Car)
print(class_content)
print(car1.get_car_brand())
print(car1.get_car_model())
print(car1.get_car_manu_year())