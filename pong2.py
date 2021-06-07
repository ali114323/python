import pygame, sys, random
#Initialisation
pygame.init()
#Variables
clock = pygame.time.Clock()
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 24)
score1 = 0
score2 = 0

def ball_animation():
    global ball_speedy
    global ball_speedx
    global score1
    global score2
    ball.x += ball_speedx
    ball.y += ball_speedy

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speedy *= -1
    if ball.left <= 0:
        score2 += 1
        ball_restart()
    if ball.right >= screen_width:
        score1 += 1
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



#Give da screeeeeeeeen
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
#Title
pygame.display.set_caption("Pong - By Ali Saleh")

#Players/Enemy functions
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20,20)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 5,70)
opponent = pygame.Rect(10, screen_height/2 - 70, 5,70)
#Colors
bg_color = pygame.Color("grey12")
light_grey = (200,200,200)
#Super sonic sPEEED
ball_speedx = 7
ball_speedy = 7
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
            if event.key == pygame.K_s:
                player_speed += 7
            if event.key == pygame.K_w:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            if event.key == pygame.K_s:
                player_speed -= 7
            if event.key == pygame.K_w:
                player_speed += 7

    player.y += player_speed
    ball_animation()
    player_animation()
    opponent_ai()
    #Visual
    screen.fill(bg_color)
    myWriting = font.render('Pong!', False, WHITE)
    myScore = font.render(str(score1), False, WHITE)
    myScore2 = font.render(str(score2), False, WHITE)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    screen.blit(myWriting,(270,10))
    screen.blit(myScore,(270, 50))
    screen.blit(myScore2,(320, 50))
    #Background - RGB (255, 255, 255) <-- Can be random
    pygame.display.update()
    clock.tick(60)
