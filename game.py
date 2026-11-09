from pygame import *
from random import randint


class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height)) 
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
   
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < win_height - 105:
           self.rect.y += self.speed

   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < win_height - 105:
           self.rect.y += self.speed


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Pong")
window.fill((200, 255, 255))



game = True
finish = False
clock = time.Clock()
FPS = 120

player1 = Player("racket.png", 30, 200, 3, 50, 100)
player2 = Player("racket.png", 620, 200, 3, 50, 100)
ball = GameSprite("tennis_ball.png", 325, 200, 4, 50, 50)

font.init()
font_countdown = font.Font(None, 150)
font_vacs = font.Font(None, 70)
font_mens = font.Font(None, 35)
lose1 = font_vacs.render('PLAYER 1 LOST!', True, (150, 50, 50))
lose2 = font_vacs.render('PLAYER 2 LOST!', True, (150, 50, 50))

l_counter_int = 0
r_counter_int = 0
odraz_l = True
odraz_r = True

ball_speed_x = 3
ball_speed_y = 3

start = False
speed_increaser = 0
mozes_bouncnut = True


urcovanie_smeru = True



while game:
    if urcovanie_smeru == True:
        smer = randint(0,1)
        if smer == 0:
            smer = -1
        urcovanie_smeru = False
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if not finish:
        if start == False:
            window.fill((200, 255, 255))
            text_3 = font_countdown.render('3', True, (0, 0, 0))
            window.blit(text_3, (310, 200))
            display.update()
            time.wait(700)

            window.fill((200, 255, 255))
            text_2 = font_countdown.render('2', True, (0, 0, 0))
            window.blit(text_2, (310, 200))
            display.update()
            time.wait(700)

            window.fill((200, 255, 255))
            text_1 = font_countdown.render('1', True, (0, 0, 0))
            window.blit(text_1, (310, 200))
            display.update()
            time.wait(700)

            start = True

        if start == True:
            window.fill((200, 255, 255))
            ball.rect.x += (ball_speed_x * (speed_increaser /12 + 1)) * smer
            ball.rect.y += (ball_speed_y * (speed_increaser /12 + 1)) * smer

            player1.update_l()
            player2.update_r()
            
            if sprite.collide_rect(player1, ball):
                if odraz_l == True:
                    ball_speed_x *= -1
                    
                    speed_increaser += 1
                    odraz_l = False
                

            if sprite.collide_rect(player2, ball):
                if odraz_r == True:
                    ball_speed_x *= -1

                    speed_increaser += 1
                    odraz_r = False

            if ball.rect.x > 200:
                odraz_l = True
            if ball.rect.x < 400:
                odraz_r = True

            if ball.rect.y > win_height - 50 or ball.rect.y < 0:
                if mozes_bouncnut == True:
                    ball_speed_y *= -1
                    mozes_bouncnut = False

            if ball.rect.y < win_height - 80 and ball.rect.y > 30:
                mozes_bouncnut = True

            if ball.rect.x < -50:
                vyhral = "R"
                finish = True
                window.blit(lose1, (165, 225))
            if ball.rect.x > win_width:
                vyhral = "L"
                finish = True
                window.blit(lose2, (165, 225))

            r_counter = font_mens.render('R Score: ' + str(r_counter_int), True, (0, 0, 0))
            l_counter = font_mens.render('L Score: ' + str(l_counter_int), True, (0, 0, 0))
            window.blit(l_counter, (75, 20))
            window.blit(r_counter, (500, 20))

            player1.reset()
            player2.reset()
            ball.reset()


    else:
        time.wait(1000)

        player1 = Player("racket.png", 30, 200, 3, 50, 100)
        player2 = Player("racket.png", 620, 200, 3, 50, 100)
        ball = GameSprite("tennis_ball.png", 325, 200, 4, 50, 50)

        if vyhral == "L":
            l_counter_int += 1

        else:
            r_counter_int += 1


        speed_increaser = 0
        finish = False
        start = False
        urcovanie_smeru = True

    display.update()
    clock.tick(FPS)
