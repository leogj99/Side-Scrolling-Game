# Name: Leonardo Guzman Jauregui
# Date: 05/05/2022
# Program: Implementation of a simple game with a character, a map and pot and the ability to throw boomerangs that break pots. 
from os import link
from platform import release
from tkinter import image_names
import pygame
import time

from pygame.locals import*
from time import sleep

class Model():
	def __init__(self):

		self.sprites = []                                                    #List that will hold all the sprites
		
		self.link = Link(100, 100, 37, 46, "Images/Image0.png")
		self.sprites.append(self.link)

		self.sprites.append( Brick(0, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 150, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 200, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(50, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(100, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 450, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 500, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 550, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(0, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(50, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(100, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(250, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 500, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(100, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(50, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(250, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(250, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(550, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(600, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(650, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(850, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(900, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(950, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 150, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 200, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 450, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 500, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 550, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(1000, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(950, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(900, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(850, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(650, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(600, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(550, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(550, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(600, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(650, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(850, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(850, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(850, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(850, 200, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 450, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 450, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 500, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(700, 550, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(650, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(650, 450, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(600, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(550, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(550, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(100, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 700, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(500, 550, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(850, 0, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(100, 650, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 400, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 250, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(150, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(200, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(450, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 50, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 100, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 300, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(800, 200, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(750, 500, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(400, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(350, 350, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 600, 50, 50, "Images/Red_brick.png"))
		self.sprites.append( Brick(300, 550, 50, 50, "Images/Red_brick.png"))
		
		self.sprites.append(Pot(750, 250, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(850, 150, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(550, 300, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(700, 100, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(800, 500, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(850, 650, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(550, 550, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(950, 550, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(450, 600, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(50, 450, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(200, 400, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(200, 600, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(300, 200, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(100, 550, 48, 48, "Images/pot.png"))
		self.sprites.append(Pot(200, 450, 48, 48, "Images/pot.png"))

	def update(self):
		for i in range(len(self.sprites)):
			self.sprites[i].update()
			
			if self.sprites[i].update():      # update returns false delete sprite i
				self.sprites.remove(self.sprites[i])     # removes sprite i from list
				break
			
			if not self.sprites[i].isBrick():    # If sprite i is not a brick 
				for j in range(len(self.sprites)):
					if self.checkCollision(self.sprites[i], self.sprites[j]) and i != j: # If there is a collision between sprite i and sprite j  and i != j

						#---------------------------------------Link collision----------------------------------
						if self.sprites[i].isLink() and self.sprites[j].isBrick():  # if sprite i is link and sprite j is a brick
							self.sprites[i].getOutOfSprite(self.sprites[j])
						elif self.sprites[i].isLink() and self.sprites[j].isPot():         # else if sprite j is a pot
							self.sprites[i].getOutOfSprite(self.sprites[j])
							self.sprites[j].setDirection(self.link.upside, self.link.downside, self.link.rightside, self.link.leftside)   # sets pot direction to slide to
						#---------------------------------------Pot collision------------------------------------
						elif self.sprites[i].isPot() and self.sprites[j].isBrick():     # if sprite i is a pot and sprite j is a brick
							self.sprites[i].collided()									# changes collisio variable to true to elimite sprite of list
							self.sprites[i].breakAnimation()            # animates the pot breaking
						#---------------------------------------Boomerang collision------------------------------
						elif self.sprites[i].isBoomerang() and self.sprites[j].isBrick():   # if i is a boomerang and j is a brick
							self.sprites[i].collided()           # boomerang collides
						elif self.sprites[i].isBoomerang() and self.sprites[j].isPot():  # if i is a boomerang and j is a pot
							self.sprites[i].collided()   # both boomerang and pot are collided
							self.sprites[j].collided()
							self.sprites[j].breakAnimation()            # animates the pot breaking

																	
	def addBoomerang(self):                                                     # Creates a new boomerang and adds it to the array.	
		self.boomerangX = self.link.x + self.link.w / 2
		self.boomerangY = self.link.y + self.link.h / 2

		self.boomerang = Boomerang(self.boomerangX, self.boomerangY, 8, 12, "Images/boomerang0.png")
		self.boomerang.setDirection(self.link.upside, self.link.downside, self.link.rightside, self.link.leftside)
		self.sprites.append(self.boomerang)
	
	def checkCollision(self, l, b):                                             # Checks if there is a collision between those sprites
		if l.y + l.h < b.y:              
			return False
		if l.y > b.y + b.h:                 
			return False
		if l.x + l.w < b.x:                 
			return False
		if l.x > b.x + b.w:
			return False
		return True
		

class View():
	scrollX = 0                  # Class variables for scrolling the view across the rooms
	scrollY = 0
	
	def __init__(self, model): # Constructor
		screen_size = (550, 400)
		self.screen = pygame.display.set_mode(screen_size, 32)
		self.model = model
		self.roomSizeX = 500                                              # Room dimentions X, Y
		self.roomSizeY = 350                                              
		self.currentRoom = 1                                              # Current room that link is in.

	def update(self):
		self.screen.fill([0, 0, 0])           # Sets background color to black

		for element in range(len(self.model.sprites)):
			self.sprite = self.model.sprites[element]
			self.loadImage = pygame.image.load(self.sprite.spriteImage)
			self.model.rect = self.loadImage.get_rect()
			self.screen.blit(self.loadImage, (self.sprite.x - View.scrollX, self.sprite.y - View.scrollY), self.model.rect)  # draws the sprite at x,y location 
			
		pygame.display.flip()
	
	def mapScrolling(self):                                                      # Changes the room to the next one if link walks to the next room
		if self.model.link.x > self.roomSizeX and self.currentRoom == 1:          # From room 1 to 2
			self.rightScroll()
			self.currentRoom += 1

		if self.model.link.x < self.roomSizeX and self.currentRoom == 2:          # From room 2 to 1
			self.leftScroll()
			self.currentRoom -= 1

		if self.model.link.x > self.roomSizeX and self.model.link.y > self.roomSizeY and self.currentRoom == 2: # From room 2 to 3
			self.downScroll()
			self.currentRoom += 1

		if self.model.link.x > self.roomSizeX and self.model.link.y < self.roomSizeY and self.currentRoom == 3: # From room 3 to 2
			self.upScroll()
			self.currentRoom -= 1
		
		if self.model.link.x < self.roomSizeX and self.model.link.y > self.roomSizeY and self.currentRoom == 3: # From room 3 to 4
			self.leftScroll()
			self.currentRoom += 1
		
		if self.model.link.x > self.roomSizeX and self.model.link.y > self.roomSizeY and self.currentRoom == 4: # From room 4 to 3
			self.rightScroll()
			self.currentRoom -= 1	
		
	
	def rightScroll(self):                                     # This methods scroll the view depending of the room entered
		View.scrollX = View.scrollX + self.roomSizeX
	def leftScroll(self):
		View.scrollX = View.scrollX - self.roomSizeX
	def downScroll(self):
		View.scrollY = View.scrollY + self.roomSizeY
	def upScroll(self):
		View.scrollY = View.scrollY - self.roomSizeY


class Controller():
	def __init__(self, model):
		self.model = model
		self.keep_going = True

	def update(self):
		self.model.link.previousLocation()            # Keeps track of link's previous location 
		
		for event in pygame.event.get():
			if event.type == QUIT:
				self.keep_going = False
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:		 # Closes the game when escape is pressed
					self.keep_going = False
				if event.key == K_LCTRL:         # Throws boomerang when left Control is pressed
					self.model.addBoomerang()	
				

		keys = pygame.key.get_pressed()
		if keys[K_LEFT]:
			self.model.link.x -= self.model.link.speed
			self.model.link.downside = False     # Starts True to draw to initial link before any user input.
			self.model.link.upside = False
			self.model.link.rightside = False
			self.model.link.leftside = True
			self.model.link.movement = True
			self.model.link.animation()         # Animates link's movement leftwards
		

		elif keys[K_RIGHT]:
			self.model.link.x += self.model.link.speed
			self.model.link.downside = False     # Starts True to draw to initial link before any user input.
			self.model.link.upside = False
			self.model.link.rightside = True
			self.model.link.leftside = False
			self.model.link.movement = True
			self.model.link.animation()         # Animates link's movement rightwards
		elif keys[K_UP]:
			self.model.link.y -= self.model.link.speed
			self.model.link.downside = False     # Starts True to draw to initial link before any user input.
			self.model.link.upside = True
			self.model.link.rightside = False
			self.model.link.leftside = False
			self.model.link.movement = True
			self.model.link.animation()         # Animates link's movement upwards

		elif keys[K_DOWN]:
			self.model.link.y += self.model.link.speed
			self.model.link.downside = True     # Starts True to draw to initial link before any user input.
			self.model.link.upside = False
			self.model.link.rightside = False
			self.model.link.leftside = False
			self.model.link.movement = True
			self.model.link.animation()         # Animates link's movement downwards

		else:
			self.model.link.movement = False
			self.model.link.animation()

		
		
		
		
		
		

class Sprite():
	def __init__(self, x, y, w, h, image_url):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.spriteImage = image_url
		self.collision = False
	
	def update(self):
		return self.collision

	def getOutOfSprite(self, sprite):          # Method that prevents link from talking through other sprites
		pass
	
	def breakAnimation(self):                               # loads pot breaking image to be used 
		pass

	def isLink(self):
		return False
	
	def isBrick(self):
		return False
	
	def isBoomerang(self):
		return False
	
	def isPot(self):
		return False
	
	def collided(self):
		self.collision = False

class Link(Sprite):
	def __init__(self, x, y, w, h, image_url):
		super().__init__(x, y, w, h, image_url)
		self.speed = 10                     # Link's movement speed
		self.downside = True                # Starts True to draw to initial link before any user input.
		self.upside = False
		self.rightside = False
		self.leftside = False
		self.movement = False

		self.downImages = ["Images/Image0.png", "Images/Image1.png", "Images/Image2.png", "Images/Image3.png"]                #List that holds down link's down images
		self.upImages = ["Images/Image12.png", "Images/Image13.png", "Images/Image14.png", "Images/Image15.png"]
		self.rightImages = ["Images/Image4.png", "Images/Image5.png", "Images/Image6.png", "Images/Image7.png"]
		self.leftimages = ["Images/Image8.png", "Images/Image9.png", "Images/Image10.png", "Images/Image11.png"]
		self.loadDownImages()
		self.loadUpImages()
		self.loadRightImages()
		self.loadLeftImages()

		self.animationCounter = 0
		self.index = 0
		self.previousX = 0
		self.previousY = 0
	
	def loadDownImages(self):                                  # Loads link's downward movement images
		for element in range(4):
			pygame.image.load(self.downImages[element])
	
	def loadUpImages(self):
		for element in range(4):
			pygame.image.load(self.upImages[element])

	def loadRightImages(self):
		for element in range(4):
			pygame.image.load(self.rightImages[element])
	
	def loadLeftImages(self):
		for element in range(4):
			pygame.image.load(self.leftimages[element])

	def counter(self):                                         # Slows down the animation speed of every image and restarts index to 0
		self.animationCounter += 1
		if self.animationCounter >= 10:
			self.index += 1
			if self.index >= 4:
				self.index = 0
			self.animationCounter = 0

	def animation(self):
		#--------------------------------DOWNWARDS ANIMATION----------------------
		if self.downside:
			self.spriteImage = self.downImages[0]
			if self.movement:
				for element in range(4):
					self.counter()
					self.spriteImage = self.downImages[self.index]
				
		#--------------------------------UPWARDS ANIMATION------------------------
		if self.upside:
			self.spriteImage = self.upImages[1]
			if self.movement:
				for element in range(4):
					self.counter()
					self.spriteImage = self.upImages[self.index]
		#--------------------------------RIGHTWARD ANIMATION----------------------
		if self.rightside:
			self.spriteImage = self.rightImages[1]
			if self.movement:
				for element in range(4):
					self.counter()
					self.spriteImage = self.rightImages[self.index]
		#--------------------------------LEFTWARDS ANIMATION----------------------
		if self.leftside:
			self.spriteImage = self.leftimages[0]
			if self.movement:
				for element in range(4):
					self.counter()
					self.spriteImage = self.leftimages[self.index]
		#-------------------------------------------------------------------------
	
	def getOutOfSprite(self, sprite):            
		if self.x + self.w >= sprite.x and self.previousX <= sprite.x and self.rightside == True:
			self.x = sprite.x - self.w
		if self.x <= sprite.x + sprite.w and self.previousX >= sprite.x + sprite.w and self.leftside == True:
			self.x = sprite.x + sprite.w
		if self.y <= sprite.y + sprite.h and self.previousY >= sprite.y + sprite.h and self.upside == True:
			self.y = sprite.y + sprite.h
		if self.y + self.h >= sprite.y and self.previousY <= sprite.y and self.downside == True:
			self.y = sprite.y - self.h
	
	def previousLocation(self):                 # Keeps track of link's previous location. 
		self.previousX = self.x
		self.previousY = self.y

	def isLink(self):            # Overwrite the method from sprite class
		return True


class Brick(Sprite):
	def __init__(self, x, y, w, h, image_url):
		super().__init__(x, y, w, h, image_url)

	def isBrick(self):										# Overwrite the method from sprite class
		return True


class Boomerang(Sprite):
	def __init__(self, x, y, w, h, image_url):
		super().__init__(x, y, w, h, image_url)
		self.up = False                     # The directions up,down,left and right that the boomerang flies to
		self.down = False
		self.left = False
		self.right = False
		self.speed = 20

	
	def update(self):
		if self.up:
			self.y -= self.speed
		elif self.down:
			self.y += self.speed
		elif self.left:
			self.x -= self.speed
		elif self.right:
			self.x += self.speed
		
		return self.collision

	
	def setDirection(self, up, down, right, left):          #Sets the direction that the boomerang will fly to.
		self.up = up
		self.down = down
		self.right = right
		self.left = left
	
	def collided(self):
		self.collision = True
	
	def isBoomerang(self):
		return True

class Pot(Sprite):
	def __init__(self, x, y, w, h, image_url):
		super().__init__(x, y, w, h, image_url)
		self.up = False                     # The directions up,down,left and right that the boomerang flies to
		self.down = False
		self.left = False
		self.right = False
		self.speed = 5
	
	def collided(self):
		self.collision = True
	
	def update(self):                                       # Pot's movement when it is hit by link 
		if self.up:
			self.y -= self.speed
		elif self.down:
			self.y += self.speed
		elif self.left:
			self.x -= self.speed
		elif self.right:
			self.x += self.speed
		
		return self.collision
	
	def setDirection(self, up, down, right, left):          #Sets the direction that the pot will slides to.
		self.up = up
		self.down = down
		self.right = right
		self.left = left

	def isPot(self):										# Overwrite the method from sprite class
		return True
	
	def breakAnimation(self):                               # loads pot breaking image to be used 
		self.spriteImage = "Images/pot_broken.png"


print("Use the arrow keys to move. Press Esc to quit.")
pygame.init()
m = Model()
v = View(m)
c = Controller(m)
while c.keep_going:
	v.mapScrolling()      
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")

