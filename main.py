import pygame as pg
import sys


class Game():

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.display.set_caption("PIANO")
        self.win = pg.display.set_mode((830, 600))
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.run()

    def run(self):
        while self.running:
            self.clock.tick(100)
            self.events()
            self.update()
            self.draw()

    def update(self):
        pass

    def events(self):
        mouse = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def draw(self):
        bg = pg.image.load("./assets/bg.jpg")
        self.win.blit(bg, (0, 0))

        key = pg.image.load("./assets/key.png")
        key_press = pg.image.load("./assets/key_p.png")

        
        self.win.blit(key, (50, 249)) #sol 
        self.win.blit(key, (140, 249)) #la
        self.win.blit(key, (230, 249)) #sib
        self.win.blit(key, (320, 249)) #si
        self.win.blit(key, (410, 249)) #do
        self.win.blit(key, (500, 249)) #re
        self.win.blit(key, (590, 249)) #mib
        self.win.blit(key_press, (680, 249)) #fa


        s = pg.image.load("./assets/s.png")
        
        self.win.blit(s, (210, 249))
        self.win.blit(s, (300, 249))
        self.win.blit(s, (480, 249))
        self.win.blit(s, (570, 249))
        self.win.blit(s, (660, 249))

        play = pg.image.load("./assets/play.png")
        self.win.blit(play, (365, 50))

        
        pg.display.flip()


g = Game()
while g.running:
    g.new()

pg.quit()
sys.exit()
