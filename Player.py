import pygame
import sys
pygame.init()


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(x, y, width, height)
        self.movement_speed = 20

    def draw(self, surface, color, rect):
        pygame.draw.rect(surface, color, rect)


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.body = []
        self.turns = {}
        self.start_x = 0
        self.start_y = 0
        self.score = 0
        self.lenght = 1
        self.direction_of_movement = 'right'
        self.rect = pygame.Rect(self.start_x, self.start_y, 20, 20)
        self.movement_speed = 20
        self.head = Cube(0, 0, 20, 20)
        self.body.append(self.head)
        self.color = (255, 0, 0)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.direction_of_movement = 'left'
                elif event.key == pygame.K_d:
                    self.direction_of_movement = 'right'
                elif event.key == pygame.K_s:
                    self.direction_of_movement = 'down'
                elif event.key == pygame.K_w:
                    self.direction_of_movement = 'up'

    def update(self, colliding_object):
        if self.rect.colliderect(colliding_object):
            self.score += 1

        if self.direction_of_movement == 'right':
            if self.rect.x + 20 < 800:
                self.rect.x += 20
        elif self.direction_of_movement == 'left':
            if self.rect.x - 20 > -20:
                self.rect.x -= 20
        elif self.direction_of_movement == 'up':
            if self.rect.y - 20 > -20:
                self.rect.y -= 20
        elif self.direction_of_movement == 'down':
            if self.rect.y + 20 < 600:
                self.rect.y += 20

    def draw(self, surface, color, rect):
        for cube in self.body:
            cube.draw(surface, color, rect)

    def add_block(self):
        self.score += 1
        self.body.append(Cube(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
