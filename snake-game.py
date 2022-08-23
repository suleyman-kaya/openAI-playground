# build a basic snake game which our goal is eat the red dot and avoid being hit by the wall or hit itself


# import the library
import pygame
import time
import random

# initialize the game
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# create a window
window_width = 600
window_height = 400
gameDisplay = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# define the time for the game
FPS = 30
clock = pygame.time.Clock()

# define the size of the snake
block_size = 10

# define the number of blocks for the snake to have at first
no_of_blocks = 1

# define the font size of the score
font = pygame.font.SysFont(None, 25)


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [window_width / 6, window_height / 3])


def gameLoop():
    # define the starting position of the snake
    x = window_width / 2
    y = window_height / 2
    # define the speed of the snake
    x_change = 0
    y_change = 0
    # set the position of the red dot
    foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
    # define the game over condition
    game_over = False
    # define the game winner condition
    game_winner = False

    # create the snake
    snake_list = []
    snake_length = 1

    # main game loop
    while not game_over:
        # game over winner loop
        while game_winner == True:
            gameDisplay.fill(white)
            message_to_screen("Congratulations! You have won! Press C to play again or Q to quit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_winner = False
                    if event.key == pygame.K_c:
                        gameLoop()
        # game over loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = block_size
                    x_change = 0
                # if the player press q the game will end
                elif event.key == pygame.K_q:
                    game_over = True
                # if the player press p the game will pause
                if event.key == pygame.K_p:
                    pause()
        # if the player hit the boundary the game will end
        if x >= window_width or x < 0 or y >= window_height or y < 0:
            game_over = True
        # update the game display
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [foodx, foody, block_size, block_size])
        # for i in range(len(snake_list)):
        # pygame.draw.rect(gameDisplay, black, [snake_list[i][0], snake_list[i][1], block_size, block_size])
        # pygame.draw.rect(gameDisplay, black, [x, y, block_size, block_size])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        for segment in snake_list[:-1]:
            if segment == snake_Head:
                game_over = True
        snake(block_size, snake_list)
        score(snake_length - 1)
        # if the head of the snake hit the red dot, the red dot will move to a new position and the length of the
        # snake will increase
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            # foodx = round(random.randrange(0, window_width - block_size) / 10.0) * 10.0
            # foody = round(random.randrange(0, window_height - block_size) / 10.0) * 10.0
            snake_length += 1
        # update the position of the snake
        x += x_change
        y += y_change

        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


def snake(block_size, snake_list):
    for XnY in snake_list:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])


def score(score):
    value = font.render("Your Score: " + str(score), True, black)
    gameDisplay.blit(value, [0, 0])


def pause():
    paused = True
    message_to_screen("Paused, press C to continue or Q to quit", black)
    pygame.display.update()
    clock.tick(5)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        clock.tick(5)

gameLoop()