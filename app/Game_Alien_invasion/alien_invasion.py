#!/usr/bin/env python 
__author__ = "lrtao2010"

import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #初识化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    s_b = Scoreboard(ai_settings, screen, stats)

    #创建一艘飞船
    ship = Ship(ai_settings, screen)
    #创建一个用于存储子弹的编组
    bullets = Group()

    #创建一个外星人编组
    aliens = Group()

    #创建一个外星人
    #alien = Alien(ai_settings, screen)

    # 创建一群外星人
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建Play 按钮
    play_button = Button(ai_settings, screen, "Play")

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, stats, s_b, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, s_b, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, s_b, ship, aliens,bullets, play_button)


run_game()

