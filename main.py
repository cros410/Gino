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

        self.bg = pg.image.load("./assets/bg2.jpg")

        self.sol = pg.image.load("./assets/key_sol.png")
        self.la = pg.image.load("./assets/key_la.png")
        self.sib = pg.image.load("./assets/key_sib.png")
        self.si = pg.image.load("./assets/key_si.png")
        self.do = pg.image.load("./assets/key_do.png")
        self.re = pg.image.load("./assets/key_re.png")
        self.mib = pg.image.load("./assets/key_mib.png")
        self.fa = pg.image.load("./assets/key_fa.png")

        self.panel = pg.image.load("./assets/notes.png")
        self.panel_1 = pg.image.load("./assets/notes_1.png")
        self.panel_2 = pg.image.load("./assets/notes_2.png")
        self.panel_3 = pg.image.load("./assets/notes_3.png")
        self.panel_4 = pg.image.load("./assets/notes_4.png")
        

        self.SOL = pg.mixer.Sound("./sounds/SOL.wav")
        self.LA = pg.mixer.Sound("./sounds/LA.wav")
        self.SIB = pg.mixer.Sound("./sounds/SIB.wav")
        self.SI = pg.mixer.Sound("./sounds/SI.wav")
        self.DO = pg.mixer.Sound("./sounds/DO.wav")
        self.RE = pg.mixer.Sound("./sounds/RE.wav")
        self.MIB = pg.mixer.Sound("./sounds/MIB.wav")
        self.FA = pg.mixer.Sound("./sounds/FA.wav")
        
        self.SONG_1 = pg.mixer.Sound("./sounds/SONGP1.wav")
        self.notes_1 = ["SOL", "SOL", "SOL",
                        "SOL", "LA", "SI", "DO", "DO", "DO"]
        self.SONG_2 = pg.mixer.Sound("./sounds/SONGP2.wav")
        self.notes_2 = ["RE", "MIB", "DO", "DO", "DO", "RE", "MIB", "DO"]
        
        self.SONG_3 = pg.mixer.Sound("./sounds/SONGP3.wav")
        self.notes_3 = ["SOL", "SOL", "SOL", "SOL", "LA", "SI",
                        "DO", "DO", "DO", "DO", "DO", "SIB", "SOL", "SIB", "SOL"]
        
        self.SONG_4 = pg.mixer.Sound("./sounds/SONGP4.wav")
        self.notes_4 = ["DO", "DO", "SIB", "DO", "SOL", "DO",
                        "SIB", "DO", "SIB", "SOL", "FA", "MI", "RE"]
        
        self.actual = 1
        self.in_song = False
        self.in_playing = False
        self.key_now = "DO"
        self.time_key = 0

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
        if not (pg.mixer.get_busy()):
            if self.in_song:
                self.in_song = False
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                b, note = self.get_note(mouse[0], mouse[1])
                if b:
                    if (note == "SOL"):
                        pg.mixer.Sound.play(self.SOL)
                    if (note == "LA"):
                        pg.mixer.Sound.play(self.LA)
                    if (note == "SIB"):
                        pg.mixer.Sound.play(self.SIB)
                    if (note == "SI"):
                        pg.mixer.Sound.play(self.SI)
                    if (note == "DO"):
                        pg.mixer.Sound.play(self.DO)
                    if (note == "RE"):
                        pg.mixer.Sound.play(self.RE)
                    if (note == "MIB"):
                        pg.mixer.Sound.play(self.MIB)
                    if (note == "FA"):
                        pg.mixer.Sound.play(self.FA)

                    if (note == "PLAY"):
                        self.in_song = True
                        pg.mixer.Sound.play(self.get_song())
            if event.type == pg.QUIT:
                self.running = False

    def draw(self):
        
        self.win.blit(self.bg, (0, 0))
        self.draw_panel()
        self.draw_keys(self.in_song, self.key_now)
        self.draw_s()
        pg.display.flip()

    def get_note(self, x, y):

        if(365 < x < 465 and 50 < y < 150):
            return True, "PLAY"

        if (249 < y < 600):
            if(50 < x < 140):
                return True, "SOL"
            if(140 < x < 230):
                return True, "LA"
            if(230 < x < 320):
                return True, "SIB"
            if(320 < x < 410):
                return True, "SI"
            if(410 < x < 500):
                return True, "DO"
            if(500 < x < 590):
                return True, "RE"
            if(590 < x < 680):
                return True, "MIB"
            if(680 < x < 770):
                return True, "FA"

        return False, ""

    def get_song(self):
        if(self.actual == 1):
            return self.SONG_1
        if(self.actual == 2):
            return self.SONG_2
        if(self.actual == 3):
            return self.SONG_3
        if(self.actual == 4):
            return self.SONG_4

    def draw_s(self):
        s = pg.image.load("./assets/s.png")
        self.win.blit(s, (210, 249))
        self.win.blit(s, (300, 249))
        self.win.blit(s, (480, 249))
        self.win.blit(s, (570, 249))
        self.win.blit(s, (660, 249))
        play = pg.image.load("./assets/play.png")
        self.win.blit(play, (365, 50))

    def draw_keys(self, b, press):

        self.win.blit(self.sol, (50, 249))  # sol
        self.win.blit(self.la, (140, 249))  # la
        self.win.blit(self.sib, (230, 249))  # sib
        self.win.blit(self.si, (320, 249))  # si
        self.win.blit(self.do, (410, 249))  # do
        self.win.blit(self.re, (500, 249))  # re
        self.win.blit(self.mib, (590, 249))  # mib
        self.win.blit(self.fa, (680, 249))  # fa
        
    def next(self):
        self.actual = self.actual + 1
        if self.actual > 4:
            self.actual = 1

    def draw_panel(self):
        if self.in_song:
            if self.actual == 1:
                self.win.blit(self.panel_1, (50, 50))
            if self.actual == 2:
                self.win.blit(self.panel_2, (50, 50))
            if self.actual == 3:
                self.win.blit(self.panel_3, (50, 50))
            if self.actual == 4:
                self.win.blit(self.panel_4, (50, 50))
        else:
            self.win.blit(self.panel, (50, 50))

g = Game()
while g.running:
    g.new()

pg.quit()
sys.exit()
