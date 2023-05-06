from pygame import *

win_width = 1300
win_height = 720
size = (win_width, win_height)

clock = time.Clock()
FPS = 60

window = display.set_mode(size)
display.set_caption("")

background = transform.scale(
    image.load("background.jpg"), size
    )

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), (80, 100))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] or keys_pressed[K_w]:
            if self.rect.y > 0:
                self.rect.y -= self.speed
            else:
                self.rect.y = win_height
        elif keys_pressed[K_DOWN] or keys_pressed[K_s]:
            if self.rect.y < win_height-80:
                self.rect.y += self.speed
            else:
                self.rect.y = 0

        elif keys_pressed[K_LEFT] or keys_pressed[K_a]:
            if self.rect.x > 0:
                self.rect.x -= self.speed
            else:
                self.rect.x = win_width
        elif keys_pressed[K_RIGHT] or keys_pressed[K_d]:
            if self.rect.x < win_width-80:
                self.rect.x += self.speed
            else:
                self.rect.x = 0


game_over = False
finish = False

#нові спрайти створюємо тут
# спрайт = Клас("каритнка", x, y, швидкість)
pac = Player("pac.png", 100, 100, 5)

while not game_over:
    
    for e in event.get():
        if e.type == QUIT:
            game_over = True

    if not finish:
        window.blit(background, (0,0))
        #усім новим спайтам тут треба задати reset i update
    pac.reset()
    pac.update()

    display.update()
    clock.tick(FPS)