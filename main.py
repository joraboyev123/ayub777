# OOP

# object oriented programming

class Car:
    def __init__(self, name, model, speed, price, color):
        self.name = name
        self.model = model
        self.speed = speed
        self.price = price
        self.color = color
    
    def __str__(self):
        return f'Car: {self.name} - {self.model} - {self.speed} - {self.price} - {self.color}'

car1 = Car('Porsche', '911', 600, '130000', 'gray')
car2= Car('Ferrari', 'Spider', 820, '330000', 'red')
car3= Car('Chevrolet', 'Matiz', 3000, '2000', 'white')

cars = []
cars.append(car1)
cars.append(car2)
cars.append(car3)

for i in cars:
    print(f'{i.name} - {i.model}')