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
        self.ship_limit = 2

        #子弹设置
        #self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10 #限制屏幕上子弹的数量

        #外星人设置
        self.fleet_drop_speed = 20

        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #得分提高的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factorx = 1.5
        self.ship_speed_factory = 1.0
        self.bullet_speed_factor = 1.5
        self.alien_speed_factor = 1
        # fleet_direction为1 表示向右移动，-1 表示向左移动
        self.fleet_direction = 1
        #记分
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed_factorx *= self.speedup_scale
        self.ship_speed_factory *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
