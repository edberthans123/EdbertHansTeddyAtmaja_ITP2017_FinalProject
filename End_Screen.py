import sys
import pygame
from pygame import *
from pygame.font import Font
from pygame.locals import *
from pygame.sprite import *

def all():
	screen = display.set_mode((1200,600))
	mouse.set_visible(True)
	display.set_caption("Pokemon Mini Story")
	class profoak(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("prof_oak.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (600,200)

	class Next(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("next.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1100,100)

	def FirstText():
		a = pygame.font.Font(None,24)
		b = "Thanks for helping me getting this pokeball back!"
		text = a.render(b,1,(0,0,0))
		screen.blit(text,(100,100))

	def SecondText():
		a = pygame.font.Font(None, 24)
		b = "Thanks for helping me getting this pokeball back!"
		c = "Now, go and explore more of this world of pokemon!"
		text = a.render(b , 1, (0,0,0))
		screen.blit(text,(100,100))
		text = a.render(c,1,(0,0,0))
		screen.blit(text, (100,120))

	class ThankYou(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("thx.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (600,200)

	a = profoak()
	b = Next()
	c = ThankYou()
	my = Group(a,b)
	oo = 1
	ok = Group(c)
	while True:
		for e in event.get():
			screen.fill((255,255,255))
			my.draw(screen)
			FirstText()

			if b.rect.collidepoint(mouse.get_pos()):
				if e.type == MOUSEBUTTONDOWN:
					oo += 1

			if oo >= 2:
				SecondText()

			if oo >= 3:
				screen.fill((0,0,0))
				ok.draw(screen)
				a = pygame.font.Font(None,60)
				b = "THANK YOU FOR PLAYING!"
				text = a.render(b,1,(255,0,255))
				screen.blit(text,(100,420))
			if e.type == QUIT:
				sys.exit()
			if e.type == K_ESCAPE:
				sys.exit()

		display.update()

