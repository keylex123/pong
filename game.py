from pygame import *

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
FPS = 60

player1 = Player("racket.png", 30, 200, 6, 50, 100)
player2 = Player("racket.png", 620, 200, 6, 50, 100)
ball = GameSprite("tennis_ball.png", 325, 200, 4, 50, 50)

font.init()
font_vacs = font.Font(None, 70)
font_mens = font.Font(None, 35)
lose1 = font_vacs.render('PLAYER 1 LOST!', True, (50, 150, 50))
lose2 = font_vacs.render('PLAYER 2 LOST!', True, (50, 150, 50))

l_counter_int = 0
r_counter_int = 0
odraz_l = True
odraz_r = True

ball_speed_x = 5
ball_speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:
        
        window.fill((200, 255, 255))
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        player1.update_l()
        player2.update_r()
        
        if sprite.collide_rect(player1, ball):
            if odraz_l == True:
                ball_speed_x *= -1
                l_counter_int += 1
                odraz_l = False
            

        if sprite.collide_rect(player2, ball):
            if odraz_r == True:
                ball_speed_x *= -1
                r_counter_int += 1
                odraz_r = False

        if ball.rect.x > 200:
            odraz_l = True
        if ball.rect.x < 400:
            odraz_r = True

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            ball_speed_y *= -1


        if ball.rect.x < -50:
            finish = True
            window.blit(lose1, (165, 225))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (165, 225))

        r_counter = font_mens.render('R Score: ' + str(r_counter_int), True, (0, 0, 0))
        l_counter = font_mens.render('L Score: ' + str(l_counter_int), True, (0, 0, 0))
        window.blit(l_counter, (75, 30))
        window.blit(r_counter, (500, 30))

        player1.reset()
        player2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
