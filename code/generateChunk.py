import pygame, pickle, copy, perlin_noise, random
import blocks as BLOCKS

def generateBlock(blockCoords, cx, cy, seed):
    bx, by, bz = blockCoords
    decimalVal = 0.25
    noise = perlin_noise.PerlinNoise(octaves=1,seed=9121209)
    
    secondDecimalVal = 0.25
    
    secondNoise = perlin_noise.PerlinNoise(octaves=1,seed=1324897)

    noise_val = noise([(bx + cx * 8) * secondDecimalVal, (by + cy * 8) * secondDecimalVal, bz * secondDecimalVal])

    second_noise_val = secondNoise([(bx + cx * 8) * decimalVal, (by + cy * 8) * decimalVal, bz * decimalVal])

    return BLOCKS.air if noise_val > 0 else (BLOCKS.dirt_block if second_noise_val > 0 else BLOCKS.coarse_dirt)
def generate_chunk(cx, cy):
    """
    map = [
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 3, 3, 3, 3],
            [3, 3, 3, 3, 3, 3, 3, 3],
        ],
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 1],
            [1, 1, 1, 1, 2, 2, 2, 2],
            [2, 2, 2, 2, 2, 2, 2, 2],
            [2, 2, 2, 2, 3, 3, 3, 3],
        ],
    ]
    """
    map = []
    if True:
        for z in range(3):
            map.append([])
            for y in range(8):
                map[z].append([])
                for x in range(8):
                    map[z][y].append(generateBlock((x, y, z), cx, cy, 3))
                
    return map