import pygame
import pygame.freetype
import sys
import time
from Player import Snake
from Food import Food
pygame.init()
pygame.font.init()

FONT = pygame.freetype.Font('font/pixelated.ttf', 40)


def draw_grid(surface, width, rows):
    # current_height = 20
    # current_width = 20
    size_between = width // rows

    x = 0
    y = 0
    for _ in range(rows):
        x += size_between
        y += size_between

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))


# making a screen
screen_size = width, height = 800, 600
pygame.display.set_caption('Snake')
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Object creation
snake = Snake(0, 0, 20, 20)
food = Food()
while 1:

    snake.move()
    snake.update()
    if pygame.sprite.spritecollide(snake.head, snake.body, False) or snake.game_over:
        screen.fill((0, 0, 0))

        FONT.render_to(screen,
                       (350, 250),
                       f'SCORE: {snake.score}',
                       (255, 255, 255))
        pygame.display.update()
        pygame.time.wait(1000)
        sys.exit(0)
    # --------------------------------------
    # Eating food
    if snake.head.rect.colliderect(food.rect):
        food.eaten(snake)
        snake.score += 1
        snake.add_block(food.rect.x, food.rect.y,
                        food.rect.width,
                        food.rect.height)

        print(snake.score)
        # print(snake.movements)
    # --------------------------------------

    snake.draw(screen, (255, 0, 0), snake)
    food.draw(screen, food.color, food.rect)
    draw_grid(screen, width, 40)

    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(4)

pygame.quit()
