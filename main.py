import pygame as pg
import random

#random.seed(0)

TITLE = "Grid"
TILES_HORIZONTAL = 10
TILES_VERTICAL = 10
TILE_SIZE = 80
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

class Player:
    def __init__(self, surface, pos=(40,40)):
        self.surface = surface
        self.pos = pos
        self.image = pg.image.load("assets/lime.png")
        self.image = pg.transform.scale(self.image, (TILE_SIZE,TILE_SIZE))
        self.font = pg.font.Font("assets/HoonWhitecatR.ttf", 40)
        self.text = self.font.render(f'{random.randint(1,9)}', True, (0,0,0))
        self.draw()


    def draw(self):
        #pg.draw.circle(self.surface, (255, 255, 255), self.pos, TILE_SIZE/3)
        imageArea = self.image.get_rect()
        imageArea.center = self.pos
        self.surface.blit(self.image, imageArea)

        
        myTextArea = self.text.get_rect()
        myTextArea.center = self.pos
        self.surface.blit(self.text, myTextArea)


    def move(self, target):
        x = (80 * (target[0] // 80)) + 40
        y = (80 * (target[1] // 80)) + 40

        self.pos = (x, y)
        #print(self.pos)


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.loop = True
        #self.player = Player(self.surface)
        self.players = []

    def main(self):
        self.add_players()
        while self.loop:
            self.grid_loop()
        pg.quit()



    def add_players(self):
        for x in range(TILE_SIZE//2, WINDOW_WIDTH, TILE_SIZE):
            for y in range(TILE_SIZE//2, WINDOW_HEIGHT, TILE_SIZE):
                pos = (x,y)
                self.players.append(Player(self.surface, pos))


    def grid_loop(self):
        self.surface.fill((0, 0, 0))
        for row in range(TILES_HORIZONTAL):
            for col in range(row % 2, TILES_HORIZONTAL, 2):
                pg.draw.rect(
                    self.surface,
                    (40, 40, 40),
                    (row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                )


        for player in self.players:
            player.draw()


        #self.player.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.loop = False
            #elif event.type == pg.MOUSEBUTTONUP:
            #    pos = pg.mouse.get_pos()
            #    self.player.move(pos)
        pg.display.update()


if __name__ == "__main__":
    mygame = Game()
    mygame.main()