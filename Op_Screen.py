import sys
import pygame
from pygame import *
from pygame.font import Font
from pygame.locals import *
from pygame.sprite import *
import FinalProject.MazeGamePika

def go():
	pygame.init()
	pygame.mixer.music.load("cianwood.mp3")
	screen = display.set_mode((1200,600))
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
		a = pygame.font.Font(None, 24)
		b = "Welcome players! My name is Oak!"
		c = "You can pick one from these three choices!"
		d = "Now, go and pick one then!"
		f = "It will be your first day picking a pokemon huh?"
		text = a.render(b , 1, (0,0,0))
		screen.blit(text,(100,100))

	def SecondText():
		a = pygame.font.Font(None, 24)
		b = "Welcome players! My name is Oak!"
		c = "You can pick one from these three choices!"
		d = "Now, go and pick one then!"
		f = "It will be your first day picking a pokemon huh?"
		text = a.render(b , 1, (0,0,0))
		screen.blit(text,(100,100))
		text = a.render(f,1,(0,0,0))
		screen.blit(text, (100,120))

	def ThirdText():
		a = pygame.font.Font(None, 24)
		b = "Welcome players! My name is Oak!"
		c = "You can pick one from these three choices!"
		d = "Now, go and pick one then!"
		f = "It will be your first day picking a pokemon huh?"
		text = a.render(b , 1, (0,0,0))
		screen.blit(text,(100,100))
		text = a.render(f,1,(0,0,0))
		screen.blit(text, (100,120))
		text = a.render(c,1,(0,0,0))
		screen.blit(text, (100,140))

	def FourthText():
		a = pygame.font.Font(None, 24)
		b = "Welcome players! My name is Oak!"
		c = "You can pick one from these three choices!"
		d = "Now, go and pick one then!"
		f = "It will be your first day picking a pokemon huh?"
		text = a.render(b , 1, (0,0,0))
		screen.blit(text,(100,100))
		text = a.render(f,1,(0,0,0))
		screen.blit(text, (100,120))
		text = a.render(c,1,(0,0,0))
		screen.blit(text, (100,140))
		text = a.render(d,1,(0,0,0))
		screen.blit(text,(100,160))

	def FifthText():
		a = pygame.font.Font(None, 24)
		b = "Welcome players! My name is Oak!"
		c = "You can pick one from these three choices!"
		d = "Now, go and pick one then!"
		f = "It will be your first day picking a pokemon huh?"
		g = "Seems like all the pokemons have been taken by someone else!"
		h = "Oh wait! I have one more pokemon available here!"
		text = a.render(b , 1, (0,0,0))
		screen.blit(text,(100,100))
		text = a.render(f,1,(0,0,0))
		screen.blit(text, (100,120))
		text = a.render(c,1,(0,0,0))
		screen.blit(text, (100,140))
		text = a.render(d,1,(0,0,0))
		screen.blit(text,(100,160))
		text = a.render(g,1,(0,0,0))
		screen.blit(text,(100,180))
		text = a.render(h,1,(0,0,0))
		screen.blit(text,(100,200))

	def PokeName():
		a = pygame.font.Font(None,24)
		b = "Bulbasaur"
		c = "Charmander"
		d = "Squirtle"
		text = a.render(b , 1 , (0,0,0))
		screen.blit(text,(160,360))
		text = a.render(d , 1 , (0,0,0))
		screen.blit(text,(560,360))
		text = a.render(c,1,(0,0,0))
		screen.blit(text,(930,355))

	def PokeName2():
		a = pygame.font.Font(None,24)
		b = "Bulbasaur"
		c = "Charmander"
		d = "Squirtle"
		text = a.render(d , 1 , (0,0,0))
		screen.blit(text,(560,360))
		text = a.render(c,1,(0,0,0))
		screen.blit(text,(930,355))

	def PokeName3():
		a = pygame.font.Font(None,24)
		b = "Bulbasaur"
		c = "Charmander"
		d = "Squirtle"
		text = a.render(c,1,(0,0,0))
		screen.blit(text,(930,355))

	class Bulbasaur(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("bulbasaur.png")
			self.rect = self.image.get_rect()
			self.rect.center = (200,450)

	class pic(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("empty.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (200,430)

	class pic2(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("empty.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (600,430)

	class pic3(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("empty.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (1000,430)

	class Click(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("empty.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (200,450)

	class Squirtle(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("squirtle.png")
			self.rect = self.image.get_rect()
			self.rect.center = (600,450)

	class Charmander(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("charmander.png")
			self.rect = self.image.get_rect()
			self.rect.center = (1000,450)

	class Cursor(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("cursor.png")
			self.rect = self.image.get_rect()

		def update(self):
			self.rect.center = mouse.get_pos()

	class getpika(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("pikachucaught.jpg")
			self.rect = self.image.get_rect()
			self.rect.center = (600,450)

	class Spritecollide(Sprite):
		def __init__(self):
			Sprite.__init__(self)
			self.image = image.load("curs.png").convert()
			self.rect = self.image.get_rect()

		def update(self):
			self.rect.center = mouse.get_pos()

	mouse.set_visible(False)

	bul = Bulbasaur()
	squ = Squirtle()
	char = Charmander()
	prof = profoak()
	next = Next()
	all_sprites = Group(prof,bul,squ,char,next)
	cur = Cursor()
	iu = getpika()
	lol = Group(iu)
	texts = 1
	pygame.mixer.music.play(-1)
	bulba = True
	squi = True
	charm = True
	pi = pic()
	pi2 = pic2()
	pi3 = pic3()
	select = 0
	select2 = 0
	select3 = 0

	while True:
		for e in event.get():
			screen.fill((255,255,255))
			all_sprites.draw(screen)
			pointer= Group(cur)
			pointer.draw(screen)
			pointer.update()

			FirstText()
			if texts >=2:
				SecondText()
			if texts >=3:
				ThirdText()
			if texts >=4:
				FourthText()

			if bulba:
				PokeName()
			if squi:
				PokeName2()
			if charm:
				PokeName3()

			if e.type == QUIT:
				pygame.quit()
				break

			if e.type == MOUSEBUTTONDOWN:
				if next.rect.collidepoint(mouse.get_pos()):
					if texts == 4:
						if bul in all_sprites:
							if char in all_sprites:
								if squ in all_sprites:
									texts += 0

					if texts == 4:
						if bul not in all_sprites:
							if squ not in all_sprites:
								if char not in all_sprites:
									texts += 1

					else:
						texts += 1

			if texts < 4 and bul.rect.collidepoint(mouse.get_pos()):
				if e.type == MOUSEBUTTONDOWN:
					a = pygame.font.Font(None,48)
					b = "Finish all the story first pls :)"
					text = a.render(b,1,(255,0,0))
					screen.blit(text,(600,300))

			if texts < 4 and squ.rect.collidepoint(mouse.get_pos()):
				if e.type == MOUSEBUTTONDOWN:
					a = pygame.font.Font(None,48)
					b = "Finish all the story first pls :)"
					text = a.render(b,1,(255,0,0))
					screen.blit(text,(600,300))

			if texts < 4 and char.rect.collidepoint(mouse.get_pos()):
				if e.type == MOUSEBUTTONDOWN:
					a = pygame.font.Font(None,48)
					b = "Finish all the story first pls :)"
					text = a.render(b,1,(255,0,0))
					screen.blit(text,(600,300))

			if select == 0:
				if texts >= 4 and bul.rect.collidepoint(mouse.get_pos()):
					if e.type == MOUSEBUTTONDOWN:
						while True:
							a = pygame.font.Font(None,24)
							b = "The ball is empty! seems like Bulbasaur has been taken"
							text = a.render(b,1,(0,255,0))
							screen.blit(text,(60,530))
							all_sprites.remove(bul)
							bulba = False
							PokeName()
							nonee = Group(pi)
							nonee.draw(screen)
							display.update()
							wait = event.wait()
							select += 1
							if wait.type == MOUSEBUTTONDOWN:
								break


			if select2 == 0:
				if texts >= 4 and squ.rect.collidepoint(mouse.get_pos()):
					if e.type == MOUSEBUTTONDOWN:
						while True:
							a = pygame.font.Font(None,24)
							b = "The ball is empty! seems like Squirtle has been taken"
							text = a.render(b,1,(0,255,0))
							screen.blit(text,(460,530))
							all_sprites.remove(squ)
							squi = False
							PokeName2()
							nonee = Group(pi2)
							nonee.draw(screen)
							display.update()
							select2+=1
							wait = event.wait()
							if wait.type == MOUSEBUTTONDOWN:
								break

			if select3 == 0:
				if texts >= 4 and char.rect.collidepoint(mouse.get_pos()):
					if e.type == MOUSEBUTTONDOWN:
						while True:
							a = pygame.font.Font(None,24)
							b = "The ball is empty! seems like Charmander has been taken"
							text = a.render(b,1,(0,255,0))
							screen.blit(text,(860,530))
							all_sprites.remove(char)
							charm = False
							PokeName3()
							nonee = Group(pi3)
							nonee.draw(screen)
							display.update()
							select3 += 1
							wait = event.wait()
							if wait.type == MOUSEBUTTONDOWN:
								break

			if bul not in all_sprites:
				if squ not in all_sprites:
					if char not in all_sprites:
						FifthText()

			if texts >= 5 and bul not in all_sprites:
				if texts >= 5 and squ not in all_sprites:
					if texts >= 5 and char not in all_sprites:
						lol.draw(screen)
						a = pygame.font.Font(None,24)
						b = "This guy name is pikachu! he is really nice!"
						c = "You received pikachu from professor oak!"
						text = a.render(b,1,(0,255,255))
						screen.blit(text,(100,240))
						text = a.render(c,1,(0,255,255))
						screen.blit(text,(100,260))

			if texts >= 6 and bul not in all_sprites:
				if texts >= 6 and squ not in all_sprites:
					if texts >= 6 and char not in all_sprites:
						a = pygame.font.Font(None,24)
						b = "Since you received a pikachu just now, can i ask u a favor?"
						c = "Would you mind going to the forest and help me retrieve the "
						e = "pokeball that i lost yesterday?"
						d = "Yes? Thanks a lot!"
						f = "I will take u there!"
						text = a.render(b,1,(0,0,0))
						screen.blit(text,(700,200))
						text = a.render(c,1,(0,0,0))
						screen.blit(text,(700,220))
						text = a.render(e,1,(0,0,0))
						screen.blit(text,(700,240))
						text = a.render(d,1,(0,0,0))
						screen.blit(text,(700,260))
						text = a.render(f,1,(0,0,0))
						screen.blit(text,(700,280))

			if texts >= 7 and bul not in all_sprites:
				if texts >= 7 and squ not in all_sprites:
					if texts >= 7 and char not in all_sprites:
						FinalProject.MazeGamePika.game()


		display.update()
