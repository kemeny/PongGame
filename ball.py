
import pygame
import random

class Ball:
    def __init__(self, x, y, radius, color, screen, speed=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed * random.choice([-1, 1])
        self.speed_y = speed * random.choice([-1, 1])
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def move(self, screen_width, screen_height):
        # Bounce off top and bottom
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = -self.speed_y

        # Update position
        self.x += self.speed_x
        self.y += self.speed_y
