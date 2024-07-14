#导入单个类
from car import Car
#导入多个类
#from car import Car,ElectricCar,Bettery
#导入整个模块，然后再用.号访问要调用的类，导入简单易读
import car

#from electricCar import ElectricCar,Bettery
#别名  将冗长的类名转化为简单的代词
from electricCar import ElectricCar as EC

#调用类中的方法要和前面类的方法名相同
print("\ntest1")
my_new_car = Car("Tesla", "Tesla", 2021)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print("\ntest2")
my_leaf = EC('ford', 'mustang', 2019)
print(my_leaf.get_descriptive_name())

print("\ntest3")
my_mustang = car.Car('ford', 'Mustang', 2021)
print(my_mustang.get_descriptive_name())

my_bezn = EC('dazhong', 'bezn', 2010)
print(my_bezn.get_descriptive_name())

print("\ntest4")
my_byd = EC('byd', 'byd_qin', 2024)
print(my_byd.get_descriptive_name())