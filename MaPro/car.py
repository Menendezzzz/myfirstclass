class Car:

    def __init__(self, model, color, year, price=None):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def ride(self):
        print('Car', self.model, 'is riding')

    def info(self):
        print('Car model=',self.model, 'color=',self.color, 'year=', self.year,'price=', self.price)

car1 = Car('Lexus', 'Black', '2012', '45000')
car1.info()