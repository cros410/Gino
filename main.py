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
        sol = pg.image.load("./assets/key.png")
        self.win.blit(sol, (50, 249))
        la = pg.image.load("./assets/key.png")
        self.win.blit(la, (140, 249))
        sib = pg.image.load("./assets/key.png")
        self.win.blit(sib, (230, 249))
        si = pg.image.load("./assets/key.png")
        self.win.blit(si, (320, 249))
        do = pg.image.load("./assets/key_p.png")
        self.win.blit(do, (410, 249))
        re = pg.image.load("./assets/key.png")
        self.win.blit(re, (500, 249))
        mib = pg.image.load("./assets/key.png")
        self.win.blit(mib, (590, 249))
        fa = pg.image.load("./assets/key.png")
        self.win.blit(fa, (680, 249))


        s = pg.image.load("./assets/s.png")
        self.win.blit(s, (115, 249))
        self.win.blit(s, (210, 249))
        self.win.blit(s, (300, 249))
        self.win.blit(s, (390, 249))
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
