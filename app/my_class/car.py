#!/usr/bin/env python 
__author__ = "lrtao2010" 

#python3.7 类导入测试

class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.modle = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        '''返回整车的描述信息'''
        long_descriptive = str(self.year) + ' ' + self.make + ' ' + self.modle
        return long_descriptive.title()

    def update_odometer(self,mileage):
        '''将里程表数值设置成指定值'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        '''将里程表读数增加指定的值'''
        if int(miles) >= 0:
            self.odometer_reading += miles
        else:
            self.odometer_reading -= miles

    def read_odometer(self):
        '''打印汽车行驶里程'''
        long_odometer = 'This car has ' + str(self.odometer_reading) + ' miles on it.'
        return long_odometer
    def fuel_tank_information(self,liter):
        """打印油箱信息"""
        tank_information = 'This car tank volume is  ' + str(liter) + 'L'
        return (tank_information)

class E_car(Car):

    def __init__(self,make, model, year):
        '''先初始化父类的属性，在初始化电动汽车的特有属性'''
        super().__init__(make,model,year)
        self.battery_size = 70

    def describe_battery(self):
        '''返回电瓶信息'''
        e_information = 'This car has a '+ str(self.battery_size) + '-KWh battery.'
        return e_information
    def fuel_tank_information(self,liter):
        t_information = "This car doesn't need a gas tank!"
        return t_information