from pygame import * 
from typing import *
init()

W = 800
H = 500
back = (0, 255, 120)
#test_back = transform.scale(image.load('background_test.png'), (W, H))

window = display.set_mode((W, H))
display.set_icon(image.load("tenis_ball.png"))
display.set_caption("Ping Pong")

font.init()
f1 = font.SysFont(None, 70)
f2 = font.SysFont(None, 50)

class GameSprite(sprite.Sprite):
    # конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # 
        super().__init__()
        # 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.size_x = size_x
        self.size_y = size_y
        self.speed = player_speed
        # 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < H-self.size_y:
            self.rect.y += self.speed

    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < H-self.size_y:
            self.rect.y += self.speed
            


racket1 = Player("racket.png", 10, H/3, 50, 150, 5)
racket2 = Player("racket.png", W-50, H/3, 50, 150, 5)
ball = GameSprite('tenis_ball.png', W/2, H/2, 50, 50, 7)


speed_x, speed_y = 3, 3

points1 = 0
points2 = 0

game = True
finish = False
while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
    points1_txt = f1.render(str(points1), True, (0, 0, 0))
    points2_txt = f1.render(str(points2), True, (0, 0, 0))

    player1_win = f1.render("PLAYER 1 WINS!", True, (0, 0, 0))
    player2_win = f1.render("PLAYER 2 WINS!", True, (0, 0, 0))

    window.blit(points1_txt, (20, 20))
    window.blit(points2_txt, (750, 20))

    if not finish:
        time.delay(10)
        #window.blit(test_back, (0, 0))

        racket1.reset()
        racket1.update_l()

        racket2.reset()
        racket2.update_r()

        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y < 0 or ball.rect.y > H-50:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x > W-50:
            points1 += 1
            ball.rect.x, ball.rect.y = W/2, H/2
        if ball.rect.x < 0:
            points2 += 1
            ball.rect.x, ball.rect.y = W/2, H/2

    if points1 >= 1:
        finish = True
        window.blit(player1_win, (W/3-50, H/2))
            

    if points2 >= 1:
        finish = True
        window.blit(player2_win, (W/3-50, H/2))
            




    display.update()