from random import random
from setting import *

import pygame


class Position:
    def __init__(self, name, x, y, speed_x=5, speed_y=5, gravity=9.8, wind=0):
        self.name = f"position of {name}"
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.gravity = gravity
        self.wind = wind


class Weapons:
    def __init__(self, name, player, damage=50):
        self.name = name
        self.position = Position(name, player.position.x, player.position.y)
        self.damage = damage


class Player:
    def __init__(self, name, health=100 , image_path="",flipped=False):
        self.name = name
        self.health = health
        self.stockRocket = 5
        self.stockGrenade = 2
        self.position = Position(name,0,0)
        self.flipped = flipped
        if image_path:
            self.image = pygame.image.load(image_path)
            self.rect = self.image.get_rect()
        else:
            self.image = None
            self.rect = None

    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, (self.position.x, self.position.y - self.rect.height))

    def shoot(self):
        if self.stockRocket > 0:
            self.stockRocket -= 1
        else:
            print(f"{self.name} has no rocket")

    def sendGrenade(self,):
        if self.stockGrenade > 0:
            self.stockGrenade -= 1
        else:
            print(f"{self.name} has no grenade")

    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} die")
        else:
            print(f"{self.name} has lost health")

    def reload(self):
        self.stockRocket = 5

    def draw(self):
        screen.blit(self.image, self.rect)


def movements(key, character):
    up_movement = key[pygame.K_z] or key[pygame.K_UP]
    down_movement = key[pygame.K_s] or key[pygame.K_DOWN]
    left_movement = key[pygame.K_q] or key[pygame.K_LEFT]
    right_movement = key[pygame.K_d] or key[pygame.K_RIGHT]

    if left_movement:
        if up_movement != down_movement:
            character.move_ip(-1, 0)
        else:
            character.move_ip(-2, 0)
    if right_movement:
        if up_movement != down_movement:
            character.move_ip(1, 0)
        else:
            character.move_ip(2, 0)
    if up_movement:
        if left_movement != right_movement:
            character.move_ip(0, -1)
        else:
            character.move_ip(0, -2)
    if down_movement:
        if left_movement != right_movement:
            character.move_ip(0, 1)
        else:
            character.move_ip(0, 2)
