from pygame import *


win_width = 700
win_height = 500
back = (128, 0, 0)
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

while game:
	for e in event.get():
		if e.type == QUIT:
			game = False

	display.update()
	clock.tick(FPS)