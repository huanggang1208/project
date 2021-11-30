# -*- coding = utf8 -*-
# @Author:hggg
# @File:alien_invasion.py
import sys
from settings import Setting
import pygame


class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings = Setting()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        # 设置背景色
        self.bg_color = (self.settings.bg_color)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # 每次循环都重绘屏幕
                self.screen.fill(self.bg_color)
                # 让最近绘制的屏幕可见
                pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
