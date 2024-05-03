from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height)) #вместе 55,55 - параметры
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
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

window = display.set_mode((600, 500))
window.fill((200, 250, 255))
win_height = 500
player1 = Player('bullet.png', 30, 200, 4, 50, 150)
player2 = Player('bullet.png', 520, 200, 4, 50, 150)

game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((200, 250, 255))
    player1.update_l()
    player2.update_r()
    player1.reset()
    player2.reset()
    display.update()
    clock.tick(60)