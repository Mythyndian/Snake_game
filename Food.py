import pygame
import random
pygame.init()


def random_spawn_point(width, height, length):
    current_height = 0
    current_width = 0
    spawn_points = []
    for _ in range(height // length):
        for i in range(width // length):
            spawn_points.append(pygame.Rect(
                current_width, current_height, 20, 20))
            current_width += 20
        current_width = 0
        current_height += 20
    return spawn_points


class Food(pygame.sprite.Sprite):
    def __init__(self):
        self.color = (0, 0, 255)
        self.rect = random.choice(random_spawn_point(800, 600, 20))

    def draw(self, screen, color, rect):
        pygame.draw.rect(screen, color, rect)

    def eaten(self, snake):
        if self.rect.colliderect(snake.head.rect):
            self.rect = random.choice(random_spawn_point(800, 600, 20))
