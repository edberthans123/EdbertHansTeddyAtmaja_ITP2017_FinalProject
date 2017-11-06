import sys
import pygame
from pygame import *
from pygame.font import Font
from pygame.locals import *
from pygame.sprite import *
import FinalProject.End_Screen

def game():
	pygame.init()
	screen = display.set_mode((1200,600))
	display.set_caption("Pokemon Mini Story")

	class profoak(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("prof_oak.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (600,200)

	class Thx(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("thx.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (600,200)

	class mainscreen():
		def __init__(self,imagefile):
			self.display = pygame.display.set_mode((1200,600))
			self.image = image.load(imagefile)
			self.display.blit(self.image, (0,0))
	mainscr = mainscreen("maze.jpg")

	class Pikachu(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("pikachu.png")
			self.rect = self.image.get_rect()
			self.rect.center = (175,80)

		def Key(self):
			if e.type == KEYDOWN:
				if e.key == K_UP:
					self.rect.move_ip(0,-20)
				if e.key == K_DOWN:
					self.rect.move_ip(0,20)
				if e.key == K_LEFT:
					self.rect.move_ip(-20,0)
				if e.key == K_RIGHT:
					self.rect.move_ip(20,0)
				if e.key == K_ESCAPE:
					sys.exit()
		def MoveBack(self):
			if e.type == KEYDOWN:
				if e.key == K_UP:
					self.rect.move_ip(0,20)
				if e.key == K_DOWN:
					self.rect.move_ip(0,-20)
				if e.key == K_LEFT:
					self.rect.move_ip(20,0)
				if e.key == K_RIGHT:
					self.rect.move_ip(-20,0)

	class Fence1(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("bush.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (290,330)

	class Mark(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("pokeball.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1050,480)

	class TallBush(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("tall bush.png")
			self.rect = self.image.get_rect()
			self.rect.center = (90,100)

	class UpperBush(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("tall bush.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1150,0)

	class Busha(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("busha.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (460,270)

	class Pio(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("New Piskel.png")
			self.rect = self.image.get_rect()
			self.rect.center = (615,535)

	class Pao(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("newpi.png")
			self.rect = self.image.get_rect()
			self.rect.center = (525,16)

	class Puo(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("newpik.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1025,16)

	class Bushas(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("piyu.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (315,60)

	class Piuy(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("piuy.png")
			self.rect = self.image.get_rect()
			self.rect.center = (255,175)

	class Piot(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("puyt.png")
			self.rect = self.image.get_rect()
			self.rect.center = (530,435)

	class Puov(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("blak.png")
			self.rect = self.image.get_rect()
			self.rect.center = (690,135)

	class Paoh(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("lolh.png")
			self.rect = self.image.get_rect()
			self.rect.center = (600,112)

	class Puova(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("iuyt.png")
			self.rect = self.image.get_rect()
			self.rect.center = (957,455)

	class Kinn(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("blak.png")
			self.rect = self.image.get_rect()
			self.rect.center = (690,370)

	class Kinna(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("hihy.png")
			self.rect = self.image.get_rect()
			self.rect.center = (805,255)

	class Mnab(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("mnab.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (970,100)

	class Paob(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("newpik.png")
			self.rect = self.image.get_rect()
			self.rect.center = (850,70)

	class Cre(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("newpik.png")
			self.rect = self.image.get_rect()
			self.rect.center = (970,280)

	class Cred(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("hagar.png")
			self.rect = self.image.get_rect()
			self.rect.center = (960,265)

	class Chl(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vba.png")
			self.rect = self.image.get_rect()
			self.rect.center = (760,335)

	class Pyur(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vzc.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1110,425)

	class Chlo(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vba.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1050,555)

	class Chloe(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vba.png")
			self.rect = self.image.get_rect()
			self.rect.center = (175,555)

	class Kinnari(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vba.png")
			self.rect = self.image.get_rect()
			self.rect.center = (175,20)

	class Chlov(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vba.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1050,575)

	class Chloed(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vba.png")
			self.rect = self.image.get_rect()
			self.rect.center = (175,575)

	class Kinnarime(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("vba.png")
			self.rect = self.image.get_rect()
			self.rect.center = (175,0)

	class Next(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("next.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1100,100)

	def collide():
		if pika.rect.collidepoint(mark.rect.center):
			sys.exit()

	pika = Pikachu()
	fence1 = Fence1()
	mark = Mark()
	tall = TallBush()
	upper = UpperBush()
	busha = Busha()
	pio = Pio()
	pao = Pao()
	puo = Puo()
	pro = Bushas()
	pnn = Piuy()
	pyt = Piot()
	pz = Puov()
	py = Paoh()
	pb = Puova()
	kin = Kinn()
	kinn = Kinna()
	mn = Mnab()
	nv = Paob()
	ca = Cre()
	cb = Cred()
	wi = Chl()
	bhg = Pyur()
	fg = Chlo()
	yu = Chloe()
	ty = Kinnari()
	bn = Chlov()
	hj = Chloed()
	ghe = Kinnarime()
	all_sprites = Group(fence1,tall,upper,busha,pio,pao,puo,pro,pnn,pyt,pz,py,pb,kinn,kin,mn,nv,ca,cb,wi,bhg,fg,yu,ty)
	spriteonly = Group(pika,mark)
	blockades = Group(fence1,tall,upper,busha,pio,pao,puo,pro,pnn,pyt,pz,py,pb,kinn,kin,mn,nv,ca,cb,wi,bhg,bn,hj,ghe)
	outer = Group(fg,yu,ty)
	tyu = Group(mark)
	nex = Next()
	pmm = profoak()
	hjn = Group(pmm,nex)
	tha = Thx()
	nin = Group(tha)
	texts = 1
	while True:
		for e in event.get():
			mainscr.display.blit(mainscr.image, (0,0))
			all_sprites.draw(screen)
			mainscr.display.blit(mainscr.image,(0,0))
			spriteonly.draw(screen)
			pika.Key()

			if spritecollideany(pika, blockades):
				pika.MoveBack()

			elif spritecollideany(pika,outer):
				a = pygame.font.Font(None,48)
				b = "You need to find the pokeball first!"
				text = a.render(b,1,(255,0,0))
				screen.blit(text,(530,280))

			elif spritecollideany(pika,tyu):
				FinalProject.End_Screen.all()

				collide()
			display.update()

