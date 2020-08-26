import pygame
import sys
pygame.init()


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(x, y, width, height)
        self.movement_speed = 20
        self.direction_of_movement = 'right'

    def draw(self, surface, color, rect):
        pygame.draw.rect(surface, color, rect)


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        self.body = pygame.sprite.Group()
        self.score = 0
        self.head = Cube(0, 0, 20, 20)
        self.color = (255, 0, 0)
        self.movements = []

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.head.direction_of_movement = 'left'
                elif event.key == pygame.K_d:
                    self.head.direction_of_movement = 'right'
                elif event.key == pygame.K_s:
                    self.head.direction_of_movement = 'down'
                elif event.key == pygame.K_w:
                    self.head.direction_of_movement = 'up'

    def update(self, colliding_object):
        # if len(self.body) > 1
        #    for part in self.body:
        # Body update
        if self.body != []:
            for number, value in enumerate(self.body):
                if number != 0:
                    value.rect.x = self.movements[-number][0]
                    value.rect.y = self.movements[-number][1]
                else:
                    value.rect.x = self.movements[number][0]
                    value.rect.y = self.movements[number][1]

        # Head update
        if self.head.direction_of_movement == 'right':
            if self.head.rect.x + 20 < 800:
                self.head.rect.x += 20
        elif self.head.direction_of_movement == 'left':
            if self.head.rect.x - 20 > -20:
                self.head.rect.x -= 20
        elif self.head.direction_of_movement == 'up':
            if self.head.rect.y - 20 > -20:
                self.head.rect.y -= 20
        elif self.head.direction_of_movement == 'down':
            if self.head.rect.y + 20 < 600:
                self.head.rect.y += 20
        # Tracking movements
        self.movements.append((self.head.rect.x, self.head.rect.y))

    def draw(self, surface, color, head, body):
        # Draw head
        pygame.draw.rect(surface, color, head.rect)
        # Draw body
        for item in body:
            pygame.draw.rect(surface, color, item.rect)

    def add_block(self, x, y, width, height):
        self.body.add(Cube(x, y, width, height))
