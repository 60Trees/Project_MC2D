import pygame
import generateChunk as Chunk
import blocks as BLOCKS
import pickle
import os

pygame.init()
def darken_image(image, factor=0.5):
    # Ensure factor is between 0 and 1
    factor = max(0, min(factor, 1))
    
    # Create a darkening surface
    dark_surface = pygame.Surface(image.get_size()).convert_alpha()
    dark_surface.fill((0, 0, 0, int(255 * (1 - factor))))  # Black with alpha to darken
    
    # Copy the original image and apply the dark surface
    darkened_image = image.copy()
    darkened_image.blit(dark_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
    
    return darkened_image
# -----WINDOW CLASS-----
class Window:
    def __init__(self) -> None:
        self.width = 1000
        self.height = 500
        self.size = self.width, self.height
        self.WIN = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self.gameGUI = pygame.Surface(self.size)
        self.chunksRendered = pygame.Surface(self.size)
        self.WIN.fill((100, 100, 100))
        self.gameGUI.fill((100, 100, 100))
        self.chunksRendered.fill((100, 100, 100))
    def update(self):
        self.size = self.WIN.get_size()
        self.width, self.height = self.size
        self.gameGUI = pygame.Surface(self.size)

w = Window()

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
                self.pos = pygame.mouse.get_pos()
                self.x, self.y = self.pos
                self.left = self.mouse[0]
                self.middle = self.mouse[1]
                self.right = self.mouse[2]
        self.keyboard = Keyboard()
        self.mouse = Mouse()
    def update(self, e):
        self.isPushed = pygame.key.get_pressed()
        if e.type == pygame.QUIT:
            done = True
input = Input()
# -----GAME CLASS-----
class Game:
    def __init__(self) -> None:
        self.clock = pygame.time.Clock()
        self.done = False
        self.activeWorld = "World_1"
        class Map:
            def __init__(self) -> None:
                self.chunkCache = {}
                self.chunksRendered = []
                
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
                chunkOperations.render(cx, cy)
                            
            def generateChunk(self, cx, cy):
                print(f"Generating chunk ({cx}, {cy})")
                c = Chunk.generate_chunk(cx, cy)
                with open(self.getRegionStrFromCCoords(cx, cy), 'wb') as file:
                    pickle.dump(c, file)
                self.loadChunk(cx, cy)
                
            def getChunk(self, cx, cy):
                if not (cx, cy) in self.chunkCache:
                    self.loadChunk(cx, cy)
                return self.chunkCache[(cx, cy)]
            
        self.map = Map()
    def doGlobalUpdates(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.done = True
            input.update(event)
        w.WIN.fill((255, 0, 0))
        w.gameGUI.fill((0, 0, 0))
        w.gameGUI.blit(w.chunksRendered, (player.x, player.y))
        w.WIN.blit(w.gameGUI, (0, 0))

        pygame.display.update()

game = Game()

# -----CHUNK CLASS-----
class Chunks:
    def __init__(self) -> None:
        self.chunkSize = 8
    def render(cx, cy):
        #print(f"Rendering chunk ({cx}, {cy})")
        if (cx, cy) in game.map.chunksRendered:
            pass
        else:
            game.map.chunksRendered.append((cx, cy))
            for z in range(3):
                for backwardsx in range(8):
                    for y in range(8):
                        x = 7 - backwardsx
                        try:
                            blockToLeft = game.map.chunkCache[(cx, cy)][z][y][x-1]
                        except:
                            blockToLeft = BLOCKS.air

                        if game.map.chunkCache[(cx, cy)][z][y][x] != BLOCKS.air:
                            w.chunksRendered.blit(
                                pygame.transform.scale(
                                    BLOCKS.ID_toImage(game.map.chunkCache[(cx, cy)][z][y][x]),
                                    (32, 32)
                                ),
                                (
                                    (cx * 8 * 32) + x * 32 + z * 16,
                                    (cy * 8 * 32) + y * 32
                                )
                            )
                            if blockToLeft != BLOCKS.air:
                                w.chunksRendered.blit(
                                    pygame.transform.scale(
                                        BLOCKS.ID_toImage(game.map.chunkCache[(cx, cy)][z][y][x]),
                                        (16, 32)
                                    ),
                                    (
                                        (cx * 8 * 32) + x * 32 + z * 16 - 16,
                                        (cy * 8 * 32) + y * 32
                                    )
                                )
                                w.chunksRendered.blit(
                                    pygame.transform.scale(
                                        BLOCKS.shadow,
                                        (16, 32)
                                    ),
                                    (
                                        (cx * 8 * 32) + x * 32 + z * 16 - 16,
                                        (cy * 8 * 32) + y * 32
                                    )
                                )
                            if z < 2:
                                w.chunksRendered.blit(
                                    pygame.transform.scale(
                                        BLOCKS.shadow,
                                        (48, 32)
                                    ),
                                    (
                                        (cx * 8 * 32) + x * 32 + z * 16 - 16,
                                        (cy * 8 * 32) + y * 32
                                    )
                                )
                                if z < 1:
                                    w.chunksRendered.blit(
                                        pygame.transform.scale(
                                            BLOCKS.shadow,
                                            (48, 32)
                                        ),
                                        (
                                            (cx * 8 * 32) + x * 32 + z * 16 - 16,
                                            (cy * 8 * 32) + y * 32
                                        )
                                    )

    def setblock(bcoords, block): # [z][y][x]
        bx, by, bz = bcoords
        game.map.loadChunk(bx // 8, by // 8)
        game.map.chunkCache[(bx // 8, by // 8)][bz][by][bx] = block

    def getblock(bcoords): # [z][y][x]
        bx, by, bz = bcoords
        game.map.loadChunk(bx // 8, by // 8)
        return game.map.chunkCache[(bx // 8, by // 8)][bz][by][bx]

chunkOperations = Chunks

class Player:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.speed = 4

    def tick(self):
        if pygame.key.get_pressed()[pygame.K_w]:
            self.vy += self.speed
        if pygame.key.get_pressed()[pygame.K_s]:
            self.vy -= self.speed
        if pygame.key.get_pressed()[pygame.K_a]:
            self.vx += self.speed
        if pygame.key.get_pressed()[pygame.K_d]:
            self.vx -= self.speed
        self.x += self.vx
        self.y += self.vy
        if self.vx != 0:
            self.vx /= 2
        if self.vy != 0:
            self.vy /= 2
        if (self.x // 32, self.y // 32) in game.map.chunkCache:
            game.map.loadChunk(self.x // 32 // 8, self.y // 32 // 8)
        print(f"PX: {self.x // 32}, PY: {self.y // 32}")
player = Player()

game.map.getChunk(0, 1)
game.map.getChunk(0, 0)
game.map.generateChunk(1, 1)
game.map.generateChunk(1, 0)
game.map.generateChunk(2, 1)
game.map.generateChunk(2, 0)

while not game.done:
    game.doGlobalUpdates()
    player.tick()

    game.clock.tick(60)
        
print("Game is finished")