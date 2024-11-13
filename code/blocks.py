import pygame
shadow = pygame.image.load("code/mcassets/dark.png")
air = 0
grass_block = 1
dirt_block = 2
stone = 3
cobblestone = 4
coarse_dirt = 5

id_list = [
    "air",
    "grass_block",
    "dirt_block",
    "stone",
    "cobblestone",
    "coarse_dirt",
]
class Images:
    def __init__(self) -> None:
        self.air = pygame.image.load("code/mcassets/textures/item/barrier.png")
        self.grass_block = pygame.image.load("code/mcassets/textures/block/grass_block_side.png")
        self.dirt_block = pygame.image.load("code/mcassets/textures/block/dirt.png")
        self.stone = pygame.image.load("code/mcassets/textures/block/stone.png")
        self.cobblestone = pygame.image.load("code/mcassets/textures/block/cobblestone.png")
        self.coarse_dirt = pygame.image.load("code/mcassets/textures/block/coarse_dirt.png")
images = Images()

def ID_toName(id):
    return id_list[id]
def ID_toImage(id):
    return getattr(images, id_list[id])