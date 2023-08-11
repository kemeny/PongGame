
import pygame

class Paddle:
    def __init__(self, x, y, width, height, color, screen, speed=5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move_up(self):
        if self.y > 0:
            self.y -= self.speed

    def move_down(self, screen_height):
        if self.y + self.height < screen_height:
            self.y += self.speed
