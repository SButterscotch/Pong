
None selected 

Skip to content
Using Gmail with screen readers
pong 
Enable desktop notifications for Gmail.
   OK  No thanks
Meet
New meeting
Join a meeting
Hangouts

Conversations
2.14 GB of 15 GB used
Terms · Privacy · Programme Policies
Last account activity: 21 minutes ago
Details
import pygame
import sys
import time

pygame.init()
clock = pygame.time.Clock()
FPS = 50

# Screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("SamPong")

# Images

icon = pygame.image.load('pong.png')
pygame.display.set_icon(icon)

grey_img = pygame.image.load('grey.png')
grey_img = pygame.transform.scale(grey_img, (screen_width, screen_height))

image = pygame.image.load('GameIcon.png')
image = pygame.transform.scale(image, (500, 200))

# Moving Text
text_img = pygame.image.load('text.png')
text_img = pygame.transform.scale(text_img, (800, 700))
text_x = screen_width / 2 - 450
text_y = -300
text_x_change = 4


# Start
def Start():
    global text_x
    start = True
    while start:
        clock.tick(70)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    GameLoop()
                if event.key == pygame.K_q:
                    sys.exit()
        screen.fill(grey)
        Text("Pong", black, y=-100, font="3", size="large")
        Text("By SamGames", black, y=-25, font="1", size="small")
        Text("Press G to start", black, y=50, font="3", size="med")
        Text("In game press P to pause", black, y=150, x=300, font="1", size="med")
        Text("Whoever scores 5 wins", black, y=150, x=-300, font="1", size="med")
        Text("Press Q to quit", black, y=220, font="1", size="med")

        screen.blit(text_img, (text_x, text_y))
        text_x += text_x_change
        if text_x >= screen_width:
            text_x = -800

        # MoveText("The game is still in experimental stage, glitches are common", red, font="4", size="med")
        pygame.display.update()


def Pause():
    global score1, score2
    pause = True
    while pause:
        clock.tick(70)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False
                if event.key == pygame.K_q:
                    pause = False
                    Start()
                if event.key == pygame.K_r:
                    GameLoop()

        screen.blit(grey_img, (0, 0))
        Text("Press P to Resume", black, y=-100, font="1", size="med")
        Text("Press R to Select New Mode", black, font="1", size="med")
        Text("Press Q to Quit", black, y=100, font="1", size="med")
        Text("To Win:", black, y=-250, x=-450, font="4", size="small")
        Text("Opponent: " + str(score_over - score1), black, y=-220, x=-395, font="4", size="small")
        Text("Player: " + str(score_over - score2), black, y=-195, x=-388, font="4", size="small")
        screen.blit(image, (620, -40))
        pygame.display.update()


# Colors
black = (0, 0, 0)
white = (255, 255, 255)
grey = (90, 90, 90)
silver = (190, 190, 190)
red = (155, 0, 0)

# Fonts
Font1_small = pygame.font.Font('D:/Python/Projects/Pong/fonts/Amatic-Bold.ttf', 20)
Font1_med = pygame.font.Font('D:/Python/Projects/Pong/fonts/Amatic-Bold.ttf', 40)
Font1_large = pygame.font.Font('D:/Python/Projects/Pong/fonts/Amatic-Bold.ttf', 60)

Font2_small = pygame.font.Font('D:/Python/Projects/Pong/fonts/Raleway-Black.ttf', 20)
Font2_med = pygame.font.Font('D:/Python/Projects/Pong/fonts/Raleway-Black.ttf', 40)
Font2_large = pygame.font.Font('D:/Python/Projects/Pong/fonts/Raleway-Black.ttf', 60)

Font3_small = pygame.font.Font('D:/Python/Projects/Pong/fonts/SEASRN__.ttf', 20)
Font3_med = pygame.font.Font('D:/Python/Projects/Pong/fonts/SEASRN__.ttf', 40)
Font3_large = pygame.font.Font('D:/Python/Projects/Pong/fonts/SEASRN__.ttf', 60)

Font4_small = pygame.font.Font('D:/Python/Projects/Pong/fonts/GrandHotel-Regular.otf', 20)
Font4_med = pygame.font.Font('D:/Python/Projects/Pong/fonts/GrandHotel-Regular.otf', 40)
Font4_large = pygame.font.Font('D:/Python/Projects/Pong/fonts/GrandHotel-Regular.otf', 60)


# Initializing TextBox
def TextBox(text, color, font, size):
    if font == "1":
        if size == "small":
            message = Font1_small.render(text, True, color)
        if size == "med":
            message = Font1_med.render(text, True, color)
        if size == "large":
            message = Font1_large.render(text, True, color)
    if font == "2":
        if size == "small":
            message = Font2_small.render(text, True, color)
        if size == "med":
            message = Font2_med.render(text, True, color)
        if size == "large":
            message = Font2_large.render(text, True, color)
    if font == "3":
        if size == "small":
            message = Font3_small.render(text, True, color)
        if size == "med":
            message = Font3_med.render(text, True, color)
        if size == "large":
            message = Font3_large.render(text, True, color)
    if font == "4":
        if size == "small":
            message = Font4_small.render(text, True, color)
        if size == "med":
            message = Font4_med.render(text, True, color)
        if size == "large":
            message = Font4_large.render(text, True, color)

    return message, message.get_rect()


def Text(text, color, x=0, y=0, font="1", size="small"):
    message, text_rect = TextBox(text, color, font, size)
    text_rect.center = (screen_width / 2 + x), (screen_height / 2 + y)
    screen.blit(message, text_rect)


# Sizes
player_length = 100
opponent_length = 100
breadth = 10
ball_size = 40

# Speed
player_speed = 10
opponent_speed = 10
ballx_speed = 10
bally_speed = 10

# Player
playerx = screen_width - breadth
playery = screen_height / 3 + 50
playery_change = 0


def Player():
    screen.fill(black, (playerx, playery, breadth, player_length))


# Opponent
AIx = 0
AIy = screen_height / 3 + 50


def AI():
    screen.fill(black, (AIx, AIy, breadth, opponent_length))


# Ball
ball_img = pygame.image.load('ball.png')
ball_img = pygame.transform.scale(ball_img, (ball_size, ball_size))
ballx = screen_width / 2 - ball_size / 2
bally = screen_height / 2 - ball_size / 2


def Ball():
    screen.blit(ball_img, (ballx, bally))


# Middle Line
def Line():
    pygame.draw.aaline(screen, black, (screen_width / 2, 0), (screen_width / 2, screen_height))


# Values
score1 = 0
score2 = 0
score_over = 5


def GameLoop():
    global ballx, bally, ballx_speed, bally_speed
    global playerx, playery, playery_change
    global AIx, AIy, AIy_change
    global score1, score2
    global opponent_speed, player_speed, opponent_length, player_length
    global text_x, text_y

    score1 = 0
    score2 = 0

    playerx = screen_width - breadth
    playery = screen_height / 3 + 50

    AIx = 0
    AIy = screen_height / 3 + 50

    run = True
    modes = True
    over1 = False
    over2 = False
    while modes:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    opponent_speed = 3
                    opponent_length = opponent_length - 10
                    player_speed = 7
                    ballx_speed = 7
                    bally_speed = 7
                    modes = False
                if event.key == pygame.K_x:
                    opponent_speed = 7
                    player_speed = 10
                    ballx_speed = 10
                    bally_speed = 10
                    modes = False
                if event.key == pygame.K_c:
                    opponent_speed = 8
                    player_speed = 10
                    ballx_speed = 10
                    bally_speed = 10
                    modes = False
                if event.key == pygame.K_v:
                    opponent_speed = 10
                    player_speed = 10
                    ballx_speed = 10
                    bally_speed = 10
                    modes = False

        screen.fill(grey)
        Text("Press Z for Easy Mode", black, y=-100, font="3", size="med")
        Text("Press X for Normal Mode", black, font="3", size="med")
        Text("Press C for Hard Mode", black, y=100, font="3", size="med")
        Text("Press V for Impossible Mode", black, y=200, font="3", size="med")
        screen.blit(text_img, (text_x, text_y))
        text_x += text_x_change
        if text_x >= screen_width:
            text_x = -800
        pygame.display.update()

    while run:
        while over1:
            clock.tick(70)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        GameLoop()
                    if event.key == pygame.K_m:
                        Start()
                    if event.key == pygame.K_q:
                        sys.exit()
            screen.blit(grey_img, (0, 0))
            Text("You Lose", black, y=-200, font="1", size="large")
            Text("Press R to Select New Mode", black, y=-100, font="1", size="med")
            Text("Press M to Go to Main Menu", black, font="1", size="med")
            Text("Press Q to Quit", black, y=100, font="1", size="med")
            pygame.display.update()

        while over2:
            clock.tick(70)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        GameLoop()
                    if event.key == pygame.K_m:
                        Start()
                    if event.key == pygame.K_q:
                        sys.exit()
            screen.blit(grey_img, (0, 0))
            Text("You Win", black, y=-200, font="1", size="large")
            Text("Press R to Select New Mode", black, y=-100, font="1", size="med")
            Text("Press M to Go to Main Menu", black, font="1", size="med")
            Text("Press Q to Quit", black, y=100, font="1", size="med")
            pygame.display.update()

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    playery_change = -player_speed
                if event.key == pygame.K_DOWN:
                    playery_change = player_speed
                if event.key == pygame.K_p:
                    Pause()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playery_change = 0

        # Player Movement
        playery += playery_change
        if playery >= screen_height - player_length:
            playery = screen_height - player_length
        if playery <= 0:
            playery = 0

        # Opponent Movement
        if AIy > bally:
            AIy -= opponent_speed
        if AIy < bally:
            AIy += opponent_speed
        if AIy >= screen_height - opponent_length:
            AIy = screen_height - opponent_length
        if AIy <= 0:
            AIy = 0

        # Ball Movement
        ballx += ballx_speed
        bally += bally_speed
        if bally <= 0:
            bally_speed += player_speed
        if bally >= screen_height - ball_size:
            bally_speed -= player_speed

        if ballx <= 0:
            ballx = screen_width / 2 - ball_size / 2
            bally = screen_height / 2 - ball_size / 2
            ballx_speed = player_speed
            bally_speed = player_speed
            score2 += 1

        if ballx >= screen_width - breadth:
            ballx = screen_width / 2 - ball_size / 2
            bally = screen_height / 2 - ball_size / 2
            ballx_speed = -player_speed
            bally_speed = player_speed
            score1 += 1

        # Collision
        if ballx + ball_size >= playerx:
            if playery <= bally + ball_size <= playery + player_length:
                ballx_speed -= player_speed
        if ballx <= AIx + breadth:
            if AIy <= bally + ball_size <= AIy + opponent_length:
                ballx_speed += player_speed
        if score1 == score_over:
            over1 = True
        if score2 == score_over:
            over2 = True
        screen.fill(grey)
        Line()
        Player()
        AI()
        Ball()
        Text(str(score1) + "     " + str(score2), black, font="4", size="small")
        Text(str(clock), black, x=-420, y=-260, font="4", size="small")
        pygame.display.update()
    sys.exit()


Start()
GameLoop()
source Pong.txt
Displaying source Pong.txt.