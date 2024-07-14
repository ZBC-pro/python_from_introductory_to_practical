#一个模块可存储多个类
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    #通过方法修改属性的值
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    #通过方法让属性值递增  接收一个英里数并追加到odometer_reading中
    def increment_odometer(self, miles):
        if miles < 0:
            print("增长数不能为负")
        else:
            self.odometer_reading += miles
