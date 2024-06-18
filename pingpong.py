from pygame import *


win_width = 600
win_height = 500
back = (255, 255, 255)
window = display.set_mode((win_width, win_height))
window.fill(back)



class GameSprite(sprite.Sprite):
	def __init__(self, pl_image, pl_x, pl_y, pl_speed, pl_weight, pl_height):
		super().__init__()
		self.image = transform.scale(image.load(pl_image), (pl_weight, pl_height))
		self.speed = pl_speed
		self.rect = self.image.get_rect()
		self.rect.x = pl_x
		self.rect.y = pl_y
	def reset(self):
		window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
	def update_l(self):
		keys = key.get_pressed()
		if keys[K_w] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[K_s] and self.rect.y < 495:
			self.rect.y += self.speed

	def update_r(self):
		keys = key.get_pressed()
		if keys[K_UP] and self.rect.y > 5:
			self.rect.y -= self.speed
		if keys[K_DOWN] and self.rect.y < 495:
			self.rect.y += self.speed


racket1 = Player('myach.png',30, 200, 4, 50, 150)
racket2 = Player('myach.png',520, 200, 4, 50, 150)

clock = time.Clock()
FPS = 60
game = True
speed_x = 0
speed_y = 0

while game:
	for e in event.get():
		if e.type == QUIT:
			game = False

	window.fill(back)
	racket1.update_l()
	racket2.update_r()
	racket1.reset()
	racket2.reset()
	display.update()
	clock.tick(FPS)