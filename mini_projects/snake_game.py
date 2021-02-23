import sys, pygame
from random import random
pygame.init()

size = width, height = 1200, 800
direct = {'left': [-1, 0], 'right': [1, 0], 'up': [0, -1], 'down': [0, 1]}
select = 'right'
speed = direct[select]
black = "#455a64"
is_event = False
# elem_coords = x, y = (round(random() * 1200) // 50) * 50, (round(random() * 800) // 50) * 50

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
# elem = pygame.image.load("ball.png")
# elem = pygame.transform.scale(elem, (50, 50))
# elemrect = elem.get_rect()
# snake = []

# def draw_snake(ballrect, snake):
#     if len(snake) != 0:
#         pass
#     pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and select != 'right':
                select = 'left'
                is_event = True
            if event.key == pygame.K_RIGHT and select != 'left':
                select = 'right'
                is_event = True
            if event.key == pygame.K_UP and select != 'down':
                select = 'up'
                is_event = True
            if event.key == pygame.K_DOWN and select != 'up':
                select = 'down'
                is_event = True
            if event.key == ord('r'):
                ballrect.left = size[0] // 2 - 30
                ballrect.top = size[1] // 2 - 30
                speed = [1, 0]

    ballrect = ballrect.move(speed)
    # elemrect = elemrect.update(elem_coords)
    # draw_snake(ballrect, snake)
    if is_event and ballrect.left % 50 == 0 and ballrect.right % 50 == 0:
        speed = direct[select]
        is_event = False
    if ballrect.left < 0 or ballrect.right > width or ballrect.top < 0 or ballrect.bottom > height:
        speed = [0, 0]

    screen.fill(black)
    screen.blit(ball, ballrect)
    # screen.blit(elem, elemrect)
    pygame.display.flip()