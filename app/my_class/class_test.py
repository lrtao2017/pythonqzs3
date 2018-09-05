#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 类--dog class

# class Dog():
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self,name,age):
#         """初始化属性name和age"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """模拟小狗被命令下蹲"""
#         return (self.name.title() + " is now sitting.")
#
#     def roll_over(self):
#         """模拟小狗被命令打滚"""
#         return (self.name.title() + " rolled over...")

# my_dog = Dog('willie',6)
# my_dog2 = Dog('bigboo',1)
# print("my dog's name is " + my_dog.name.title() + '.')
# print("my dog is " + str(my_dog.age) + " years old.")
# print(my_dog.sit())
# print(my_dog.roll_over())
#
# print("my dog's name is " + my_dog2.name.title() + '.')
# print("my dog is " + str(my_dog2.age) + " years old.")
# print(my_dog2.sit())
# print(my_dog2.roll_over())
#
# # my dog's name is Willie.
# # my dog is 6 years old.
# # Willie is now sitting.
# # Willie rolled over...
# # my dog's name is Bigboo.
# # my dog is 1 years old.
# # Bigboo is now sitting.
# # Bigboo rolled over...


# class User():
#     def __init__(self,first_name,last_name):
#         self.name = first_name + last_name
#     def describe_user(self):
#         if "lei" in self.name:
#             return (self.name + ' is a boy')
#         else:
#             return (self.name + ' is a girl')
#     def greet_user(self):
#         return ('Hello ' + self.name + '!')
#
# user_li = User('li','lei')
# user_han = User('han','meimei')
# print(user_li.name)
# print(user_li.describe_user())
# print(user_li.greet_user())
# print(user_han.name)
# print(user_han.describe_user())
# print(user_han.greet_user())
#
# # lilei
# # lilei is a boy
# # Hello lilei!
# # hanmeimei
# # hanmeimei is a girl
# # Hello hanmeimei!



# class Car():
#     '''一次模拟汽车的简单尝试'''
#     def __init__(self,make,model,year):
#         '''初始化描述汽车的属性'''
#         self.make = make
#         self.modle = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         '''返回整车的描述信息'''
#         long_descriptive = str(self.year) + ' ' + self.make + ' ' + self.modle
#         return long_descriptive.title()
#
#     def update_odometer(self,mileage):
#         '''将里程表数值设置成指定值'''
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self,miles):
#         '''将里程表读数增加指定的值'''
#         if int(miles) >= 0:
#             self.odometer_reading += miles
#         else:
#             self.odometer_reading -= miles
#
#     def read_odometer(self):
#         '''打印汽车行驶里程'''
#         long_odometer = 'This car has ' + str(self.odometer_reading) + ' miles on it.'
#         return long_odometer
#     def fuel_tank_information(self,liter):
#         """打印油箱信息"""
#         tank_information = 'This car tank volume is  ' + str(liter) + 'L'
#         return (tank_information)
#
# class E_car(Car):
#
#     def __init__(self,make, model, year):
#         '''先初始化父类的属性，在初始化电动汽车的特有属性'''
#         super().__init__(make,model,year)
#         self.battery_size = 70
#
#     def describe_battery(self):
#         '''返回电瓶信息'''
#         e_information = 'This car has a '+ str(self.battery_size) + '-KWh battery.'
#         return e_information
#     def fuel_tank_information(self,liter):
#         t_information = "This car doesn't need a gas tank!"
#         return t_information
#
# if __name__ == '__main__':
#     my_new_car = Car('subaru', 'outback', 2018)
#     my_old_car = Car('subaru', 'outback_old', 2008)
#     my_used_car = Car('subaru', 'outback_used', 2006)
#     my_tesla = E_car('tesla','model s',2018)
#     print(my_tesla.get_descriptive_name())
#     print(my_tesla.describe_battery())
#     print(my_tesla.fuel_tank_information(30))
#     print('\n')
#     print(my_new_car.get_descriptive_name())
#     print(my_new_car.read_odometer())
#     print(my_new_car.fuel_tank_information(30))
#     print('\n')
#     my_old_car.update_odometer(10000)
#     print(my_old_car.get_descriptive_name())
#     print(my_old_car.read_odometer())
#     my_old_car.update_odometer(1000)
#     print(my_old_car.read_odometer())
#     print('\n')
#     my_used_car.update_odometer(12000)
#     my_used_car.increment_odometer(300)
#     print(my_used_car.get_descriptive_name())
#     print(my_used_car.read_odometer())
#     my_used_car.increment_odometer(-45)
#     print(my_used_car.read_odometer())
#
# # 2018 Tesla Model S
# # This car has a 70-KWh battery.
# # This car doesn't need a gas tank!
# #
# #
# # 2018 Subaru Outback
# # This car has 0 miles on it.
# # This car tank volume is  30L
# #
# #
# # 2008 Subaru Outback_Old
# # This car has 10000 miles on it.
# # You can't roll back an odometer!
# # This car has 10000 miles on it.
# #
# #
# # 2006 Subaru Outback_Used
# # This car has 12300 miles on it.
# # This car has 12345 miles on it.
