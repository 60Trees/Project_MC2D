import pygame
import perlin_noise
import pickle
import os

# -----WINDOW CLASS-----
class Window:
    def __init__(self) -> None:
        self.width = 100
        self.height = 100
        self.size = self.width, self.height
        self.WIN = pygame.display.set_mode(self.size, pygame.RESIZABLE)
window = Window()

# -----INPUT CLASS-----
class Input:
    def __init__(self) -> None:
        class Keyboard:
            def __init__(self) -> None:
                self.isPushed = pygame.key.get_pressed()
                self.isTyped = pygame.key.get_pressed()
        class Mouse:
            def __init__(self) -> None:
                self.mouse = pygame.mouse.get_pressed()
                self.left = self.mouse[0]
                self.middle = self.mouse[1]
                self.right = self.mouse[2]
        self.keyboard = Keyboard()
        self.mouse = Mouse()
    def update(self, e):
        if e.type == pygame.QUIT:
            done = True
input = Input()
# -----GAME CLASS-----
class Game:
    def __init__(self) -> None:
        self.done = False
        self.activeWorld = "World_1"
        class Map:
            def getRegionStrFromCCoords(self, cx, cy):
                return "code/saves/"+game.activeWorld+"/region/"+"2dmcchunk_"+str(cx)+str(cy)+".mc2dchunk"
            def __init__(self) -> None:
                pass
            def loadChunk(self, cx, cy):

                pass
            def generateChunk(self, cx, cy):
                print(f"Generating chunk CX={cx},CY={cy}")
                with open(self.getRegionStrFromCCoords(cx, cy), 'wb') as file:
                    pickle.dump("Hi", file)
            def getChunk(self, cx, cy):
                if not os.path.isfile(self.getRegionStrFromCCoords(cx, cy)):
                    self.generateChunk(cx, cy)
                with open(self.getRegionStrFromCCoords(cx, cy), 'rb') as handle:
                    b = pickle.load(handle)
                return b
        self.map = Map()
    def doGlobalUpdates(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.done = True
            input.update(event)
game = Game()

# -----CHUNK CLASS-----
class Chunks:
    def __init__(self) -> None:
        pass
    def render(self, sx, sy):
        pass

game.map.getChunk(0, 0)

while not game.done:
    game.doGlobalUpdates()
print("Hi")