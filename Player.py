import pygame
import sys
pygame.init()


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(x, y, width, height)
        self.direction_of_movement = 'right'

    def draw(self, surface, color, rect):
        pygame.draw.rect(surface, color, rect)


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        self.body = pygame.sprite.Group()
        self.score = 0
        self.head = Cube(x, y, width, height)
        self.head_group = pygame.sprite.Group()
        self.head_group.add(self.head)
        self.color = (255, 0, 0)
        self.movements = []
        self.game_over = False

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

    def update(self):
        # Body update
        # Needs bugfix
        for number, value in enumerate(self.body):
            value.rect.x = self.movements[-number-1][0]
            value.rect.y = self.movements[-number-1][1]

        # Head update
        if self.head.direction_of_movement == 'right':
            if self.head.rect.x + 20 < 800:
                self.head.rect.x += 20
            else:
                self.game_over = True
        elif self.head.direction_of_movement == 'left':
            if self.head.rect.x - 20 > -20:
                self.head.rect.x -= 20
            else:
                self.game_over = True
        elif self.head.direction_of_movement == 'up':
            if self.head.rect.y - 20 > -20:
                self.head.rect.y -= 20
            else:
                self.game_over = True
        elif self.head.direction_of_movement == 'down':
            if self.head.rect.y + 20 < 600:
                self.head.rect.y += 20
            else:
                self.game_over = True
        # Tracking movements
        self.movements.append((self.head.rect.x, self.head.rect.y))

    def draw(self, surface, color, snake):
        # Draw head
        snake.head.draw(surface, color, snake.head.rect)
        # Draw body
        for item in snake.body:
            item.draw(surface, color, item.rect)

    def add_block(self, x, y, width, height):
        self.body.add(Cube(x, y, width, height))
