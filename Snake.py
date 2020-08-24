import pygame
import sys
from snake_class import Snake
from food_class import Food
pygame.init()


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
snake = Snake()
food = Food()
while 1:
    snake.move()
    snake.update(food.rect)
    snake.draw(screen, snake.rect)
    # --------------------------------------
    # Eating food
    if snake.rect.colliderect(food.rect):
        snake.add_block()
        food = Food()
        print(snake.score)
    # --------------------------------------
    food.draw(screen, food.color, food.rect)
    print(food.rect)
    draw_grid(screen, width, 40)
    pygame.display.update()
    screen.fill((0, 0, 0))
    clock.tick(2)

pygame.quit()
