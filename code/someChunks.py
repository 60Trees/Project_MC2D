import pygame, pickle, copy
import blocks as BLOCKS

cx = input("Chunk x: --->")
cy = input("Chunk y: --->")

dir = "code/saves/World_2/region/2dmcchunk_" + str(cx) + str(cy) + ".mc2dchunk"
if input(f"Path stays as {dir}? (n for no) --->") == "n":
    dir = input("Directory path: --->")



map = []
map2 = [
    [
        [3, 3, 3, 3, 3, 3, 3, 3],
        [3, 3, 1, 3, 1, 3, 1, 3],
        [3, 2, 0, 0, 0, 0, 2, 3],
        [3, 2, 0, 0, 1, 0, 2, 3],
        [3, 2, 0, 1, 2, 0, 2, 3],
        [3, 2, 0, 0, 0, 0, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 3],
        [3, 3, 3, 3, 3, 3, 3, 3],
    ],
    [
        [3, 3, 3, 3, 3, 3, 3, 3],
        [3, 1, 1, 1, 1, 1, 1, 3],
        [3, 2, 0, 0, 0, 0, 2, 3],
        [3, 2, 0, 0, 1, 0, 2, 3],
        [3, 2, 0, 1, 2, 0, 2, 3],
        [3, 2, 0, 0, 0, 0, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 3],
        [3, 3, 3, 3, 3, 3, 3, 3],
    ],
    [
        [3, 3, 3, 3, 3, 3, 3, 3],
        [3, 1, 1, 1, 1, 1, 1, 3],
        [3, 2, 0, 0, 0, 0, 2, 3],
        [3, 2, 0, 3, 3, 0, 2, 3],
        [3, 2, 0, 1, 2, 0, 2, 3],
        [3, 2, 0, 0, 0, 0, 2, 3],
        [3, 2, 2, 2, 2, 2, 2, 3],
        [3, 3, 3, 3, 3, 3, 3, 3],
    ],
]

for i in range(3):
    map.append([])
    for i2 in range(8):
        map[i].append([])
        for _ in range(8):
            map[i][i2].append(0)

print(f"Generating chunk CX={cx},CY={cy}")
with open(dir, 'wb') as file:
    pickle.dump(map2, file)

print(map)
print(map2)