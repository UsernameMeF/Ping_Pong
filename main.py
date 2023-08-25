from pygame import * 
init()

W = 800
H = 500
back = (0, 255, 120)

window = display.set_mode((W, H))
display.set_icon(image.load("tenis_ball.png"))
display.set_caption("Ping Pong")


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
racket2 = Player("racket.png", W-60, H/3, 50, 150, 5)

game = True
finish = False

while game:
    time.delay(5)
    window.fill(back)

    racket1.reset()
    racket1.update_l()

    racket2.reset()
    racket2.update_r()

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()