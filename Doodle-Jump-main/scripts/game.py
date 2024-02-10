import pygame
import os
from scripts.functions import load_image
from scripts.sprite import Sprite
from scripts.player import Player
from scripts.platform import Platform
from scripts.constants import display_size

class Game:
    def __init__(self):
        self.background = load_image("assets", "images", "background.png")
        self.player = Player((240,600), load_image("assets","images","player.png"),5, 20, 0.65)
        self.offset_y = 0
        self.platforms = [
            Platform((240, 700), load_image("assets","images","platform.png")),
            Platform((100, 450), load_image("assets","images","platform.png")),
            Platform((400, 200), load_image("assets","images","platform.png"))
        ]
        self.loser = False
        self.fond = pygame.Font(os.path.join('assets', "fonts","pixel.ttf"),32)
    def restart(self):
        self.offset_y = 0
        self.loser = False
        self.platforms = list()
        self.platform_generator.create_start_configuration()

    def render(self,surface: pygame.Surface):
        surface.blit(self.background,(0,0))

        for platform in self.platforms:
            platform.render(surface, self.offset_y)
        self.player.render(surface, self.offset_y)
        score = round(-self.offset_y/10)
        if self.loser:
            score_text = font.render(f"Ваш рекорд{score}",True,(1,1,1))
            hint_text = font.render("Нажмите клавишу",True,(1,1,1))

            score_rect = score_text.get_rect(
                centerx=display_size[0]/2,
                centery=display_size[1]/2-25
            )
            hint_rect = hint_text.get_rect(
                centerx=display_size[0]/2,
                centery=display_size[1]/2+25
            )
            surface.blit(score_text,score_rect)
            surface.blit(hint_text,hint_rect)
        else:
            text = self.fond.render(str(score),True,(1,1,1))
            rect = text.get_rect(midtop = (display_size[0]/2,10))
            surface.blit(text,rect)

    def handle_key_down_event(self,key):
        if self.loser:
            self.restart()
        elif key == pygame.K_a:
            self.player.is_walking_left = True
        elif key == pygame.K_d:
            self.player.is_walking_right = True

    def handle_key_up_event(self,key):
        if key == pygame.K_a:
            self.player.is_walking_left = False
        elif key == pygame.K_d:
            self.player.is_walking_right = False
    def update(self):
        self.player.update()
        self.loser = self.player.rect.top - self.offset_y >=display_size[1]
        if self.loser:
            return
        for platform in self.platforms:
            if self.player.collide_sprite(platform):
                self.player.on_platform = True
        if self.player.rect.bottom - self.offset_y < display_size[1]/3:
            self.offset_y = self.player.rect.bottom - display_size[1] / 3
       