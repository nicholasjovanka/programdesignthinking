import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        super(Ship, self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('IMAGES/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()#To treat the screen like its rectangle
        #Position of the ship
        self.rect.centerx=self.screen_rect.centerx
        self.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.center=float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx+=self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.rect.centery-=self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.centery<self.screen_rect.bottom:
            self.rect.centery+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx-=self.ai_settings.ship_speed_factor

    def center_ship(self):
        self.center=self.screen_rect.centerx

