import pygame
import generateChunk as Chunk
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
            def __init__(self) -> None:
                self.chunkCache = {}
                
            def getRegionStrFromCCoords(self, cx, cy):
                return "code/saves/"+game.activeWorld+"/region/"+"2dmcchunk_"+str(cx)+str(cy)+".mc2dchunk"
            
            def loadChunk(self, cx, cy):
                print(f"Loading chunk ({cx}, {cy}) into cache")
                if (cx, cy) in self.chunkCache:
                    print(f"Chunk ({cx}, {cy}) in cache already exists!")
                else:
                    if not os.path.isfile(self.getRegionStrFromCCoords(cx, cy)):
                        self.generateChunk(cx, cy)
                        with open(self.getRegionStrFromCCoords(cx, cy), 'rb') as file:
                            self.chunkCache[(cx, cy)] = pickle.load(file)
                    else:
                        with open(self.getRegionStrFromCCoords(cx, cy), 'rb') as file:
                            self.chunkCache[(cx, cy)] = pickle.load(file)
                            
            def generateChunk(self, cx, cy):
                print(f"Generating chunk ({cx}, {cy})")
                c = Chunk.generate_chunk(cx, cy)
                with open(self.getRegionStrFromCCoords(cx, cy), 'wb') as file:
                    pickle.dump(c, file)
                self.loadChunk(cx, cy)
                
            def getChunk(self, cx, cy):
                self.loadChunk(cx, cy)
                return self.chunkCache[(cx, cy)]
            
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

print(game.map.getChunk(0, 1))

while not game.done:
    game.doGlobalUpdates()
print("Game is finished")