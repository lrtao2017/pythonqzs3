#!/usr/bin/env python 
__author__ = "lrtao2010"

import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每一艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery #Y轴中央
        #self.rect.bottom = self.screen_rect.bottom  #Y轴底部（底部）

        #在飞船的属性center中存储小数值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        # if self.moving_right:
        #     self.rect.centerx += 1
        # if self.moving_left:
        #     self.rect.centerx -= 1
        #更新飞船center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.centerx += self.ai_settings.ship_speed_factorx
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factorx
        if self.moving_up and self.rect.top >0 :
            self.centery -= self.ai_settings.ship_speed_factory
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factory

        #根据self.centerx或self.centery 更新rect 对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

