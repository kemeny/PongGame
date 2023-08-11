
import pygame
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 55)

        # Create paddles and ball
        self.paddle1 = Paddle(10, screen_height // 2 - 40, 15, 80, (0, 255, 0), self.screen)
        self.paddle2 = Paddle(screen_width - 25, screen_height // 2 - 40, 15, 80, (0, 0, 255), self.screen)
        self.ball = Ball(screen_width // 2, screen_height // 2, 15, (255, 0, 0), self.screen)

        # Initialize scores
        self.score1 = 0
        self.score2 = 0

    def display_score(self):
        score_display = self.font.render(f"{self.score1} - {self.score2}", True, (255, 255, 255))
        self.screen.blit(score_display, (self.screen.get_width() // 2 - 60, 10))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle1.move_up()
            if keys[pygame.K_s]:
                self.paddle1.move_down(self.screen.get_height())
            if keys[pygame.K_UP]:
                self.paddle2.move_up()
            if keys[pygame.K_DOWN]:
                self.paddle2.move_down(self.screen.get_height())

            # Ball collision with paddles
            if self.ball.x - self.ball.radius <= self.paddle1.x + self.paddle1.width and                self.ball.y > self.paddle1.y and self.ball.y < self.paddle1.y + self.paddle1.height or                self.ball.x + self.ball.radius >= self.paddle2.x and                self.ball.y > self.paddle2.y and self.ball.y < self.paddle2.y + self.paddle2.height:
                self.ball.speed_x = -self.ball.speed_x

            # Ball out of bounds
            if self.ball.x - self.ball.radius <= 0:
                self.score2 += 1
                self.ball = Ball(self.screen.get_width() // 2, self.screen.get_height() // 2, 15, (255, 0, 0), self.screen)

            if self.ball.x + self.ball.radius >= self.screen.get_width():
                self.score1 += 1
                self.ball = Ball(self.screen.get_width() // 2, self.screen.get_height() // 2, 15, (255, 0, 0), self.screen)

            # Update ball movement
            self.ball.move(self.screen.get_width(), self.screen.get_height())

            # Drawing
            self.screen.fill((0, 0, 0))
            self.paddle1.draw()
            self.paddle2.draw()
            self.ball.draw()
            self.display_score()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
