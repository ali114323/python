import pygame, sys, random

clock = pygame.time.Clock()

def ball_animation():
    global ball_speedy
    global ball_speedx
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speedy *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speedx *= -1

def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speedx
    global ball_speedy
    ball.center = (screen_width/2, screen_height/2)
    ball_speedy *= random.choice((1, -1))
    ball_speedx *= random.choice((1, -1))
#Initialisation
pygame.init()
#Give da screeeeeeeeen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
#Title
pygame.display.set_caption("Pong - By Ali Saleh")
icon = pygame.image.load(r"C:\Users\agarp\Desktop\python\vsc\icons\calc.ico")
pygame.display.set_icon(icon)

#Players/Enemy functions
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20,20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 5,70)
opponent = pygame.Rect(10, screen_height/2 - 70, 5,70)
#Colors
bg_color = pygame.Color("grey12")
light_grey = (200,200,200)
#Super sonic sPEEED
ball_speedx = 4
ball_speedy = 4
player_speed = 0
opponent_speed = 7


#game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    player.y += player_speed
    ball_animation()
    player_animation()
    opponent_ai()
    #Visual
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    #Background - RGB (255, 255, 255) <-- Can be random
    pygame.display.update()
    clock.tick(60)