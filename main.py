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
        self.number = random.randint(1, 9)
        self.text = self.font.render(f'{self.number}', True, (0,0,0))
        self.visible = True
        self.draw()


    def draw(self):
        if self.visible:
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
        self.drawing = False  # Track if user is drawing a rectangle
        self.rect_start = (0, 0)
        self.rect_end = (0, 0)

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

        self.players = [player for player in self.players if player.visible]  # Remove deleted players
        
        for player in self.players:
            player.draw()

        if self.drawing:
            x1, y1 = self.rect_start
            x2, y2 = self.rect_end
            rect_width = x2 - x1
            rect_height = y2 - y1
            pg.draw.rect(self.surface, GREEN, (x1, y1, rect_width, rect_height), 2)


        #self.player.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.loop = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.drawing = True
                self.rect_start = event.pos
                self.rect_end = event.pos
            elif event.type == pg.MOUSEMOTION and self.drawing:
                self.rect_end = event.pos
            elif event.type == pg.MOUSEBUTTONUP:
                self.drawing = False
                self.calculate_sum()
            #elif event.type == pg.MOUSEBUTTONUP:
            #    pos = pg.mouse.get_pos()
            #    self.player.move(pos)
        pg.display.update()


    def calculate_sum(self):
        x1, y1 = self.rect_start
        x2, y2 = self.rect_end
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)

        total_sum = 0
        selected_players = []
        for player in self.players:
            px, py = player.pos  # Get the center position of the player (number)
            if x_min <= px <= x_max and y_min <= py <= y_max:
                total_sum += player.number
                selected_players.append(player)
        
        print(f"Sum of numbers in selected area: {total_sum}")
        
        # Remove players if the sum is exactly 10
        if total_sum == 10:
            for player in selected_players:
                player.visible = False  # ✅ Hide player
            self.players = [player for player in self.players if player.visible] 
    

if __name__ == "__main__":
    mygame = Game()
    mygame.main()