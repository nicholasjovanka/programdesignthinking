import pygame
from pygame.sprite import Sprite
from alien import Alien

class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship):
         super(Bullet, self).__init__()
         self.screen = screen
         self.image=pygame.image.load('IMAGES/bullet.bmp')
         self.rect = self.image.get_rect()
         self.rect.centerx = ship.rect.centerx
         self.rect.top = ship.rect.top
         self.y = float(self.rect.y)
         self.color = ai_settings.bullet_color
         self.speed_factor = ai_settings.bullet_speed_factor

    def draw_bullet(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
         self.y -= self.speed_factor
         self.rect.y = self.y

