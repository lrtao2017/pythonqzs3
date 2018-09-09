#!/usr/bin/env python 
__author__ = "lrtao2010" 


class Settings():
    '''存放《外星人入侵》的所有设置的类'''
    def __init__(self):
        """初始化游戏设置"""
        #屏幕设置
        self.screen_width = 960
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #飞船设置
        self.ship_speed_factorx = 1.5
        self.ship_speed_factory = 1.0
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 1.5
        #self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10 #限制屏幕上子弹的数量

        #外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 20
        #fleet_direction为1 表示向右移动，-1 表示向左移动
        self.fleet_direction = 1