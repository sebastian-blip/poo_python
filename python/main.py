from car import Car
from account import Account

if __name__ == '__main__':
    print("Hola mundo")
    car = Car("AWS435", Account("Andres Herrera", "123RT"))
    print(vars(car))
    print(vars(car.driver))



