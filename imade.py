from pygame.locals import *
import pygame
from random import randint
import time

class Apple:
    x=0
    y=0
    step=44

    def __init__(self,x,y):
        self.x=x*self.step
        self.y=y*self.step
        #our one unit is 44 pixels
    def draw(self,surface,image):
        surface.blit(image,(self.x,self.y))


class Player:
    x=[0]
    y=[0]
    step=44
    direction=0
    length=3

    def __init__(self,length):
        self.length=length
        #get 200 parts of snake in list
        for i in range(200):
            self.x.append(-100)
            self.y.append(-100)

        #initial positions,no collision
        for i in range(1,self.length-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        #update position of head of snake
        if self.direction==0:
            self.x[0]=self.x[0]+self.step
        if self.direction==1:
            self.x[]=self.x[]+self.step
        if self.direction==2:
            self.x[]=self.x[]+self.step
        if self.direction==3:
            self.x[]=self.x[]+self.step

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

class App:

    windowWidth=800
    windowHeight=600

    def __init__(self):
        self._running=True
        self._display_surf=None
        self._image_surf=None
        self.player=Player()

    def on_init(self):
        pygame.init()
        self._display_surf=pygame.display.set_mode((self.windowWidth,self.windowHeight)) #creates the main screen

        pygame.display.set_caption('Pygame Snake') #sets the file name on titlebar
        self._running=True
        self._image_surf=pygame.image.load("wssnake.png") #loads the image

    def on_render(self):
        self._display_surf.fill((0,0,0)) #sets the RGB value for background 0 is for black
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y)) #shows the player on the main screen
        pygame.display.flip() #updates the changes like move up move down on the mainscreen and removes the previous one

    def on_execute(self):
        if self.on_init()==False:  #checks if the function on_init is working or not, if its not running the further code will not be executed
            self._running=False

        while (self._running):
            pygame.event.pump()
            keys=pygame.key.get_pressed()

            if(keys[K_RIGHT]):   #don't comment locals if commenting then use pygame.K_RIGHT
                self.player.moveRight()

            if(keys[K_LEFT]):
                self.player.moveLeft()

            if(keys[K_UP]):
                self.player.moveUp()

            if(keys[K_DOWN]):
                self.player.moveDown()

            self.on_render()
        pygame.quit()

if __name__== "__main__":
    theApp=App() #object of class App
    theApp.on_execute() #execute 
