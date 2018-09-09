#!/usr/bin/env python
__author__ = "lrtao2010"

import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """显示得分信息的类"""
    def __init__(self, ai_settings, screen, stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #self.prep_level()
        self.prep_ships()

        #显示得分信息使用的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 32)

        #准备包含最高得分和当前得分的图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_high_score(self):
        """将最高得分转换为渲染的图像"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        highest_score_str = 'H_score: %s ' % high_score_str
        self.high_score_image = self.font.render(highest_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在屏幕顶部中间
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.screen_rect.top = 20


    def prep_score(self):
        """将得分转换为一副渲染的图像"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        current_score_str = 'C_score: %s ' % score_str
        self.score_image = self.font.render(current_score_str, True, self.text_color, self.ai_settings.bg_color)

        #将得分放在屏幕右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def prep_level(self):
        """将等级转换为一副渲染的图像"""
        level_str = 'Level: %s' % self.stats.level
        self.level_image = self.font.render(str(level_str), True, self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下放
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """显示剩余多少艘飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        #绘制剩余的飞船
        self.ships.draw(self.screen)
