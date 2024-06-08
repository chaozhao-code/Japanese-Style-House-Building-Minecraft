import sys

import numpy as np
from glm import ivec2, ivec3

from gdpc import __url__, Editor, Block, Box, Transform
from gdpc.exceptions import InterfaceConnectionError, BuildAreaNotSetError
from gdpc.vector_tools import Y, addY, dropY, line3D, circle, fittingCylinder
from gdpc.transform import rotatedBoxTransform, flippedBoxTransform
from gdpc.geometry import placeBox, placeCheckeredBox
from gdpc.vector_tools import X, Y, Z, XZ, addY, dropY, loop2D, loop3D, perpendicular, toAxisVector2D
import matplotlib.pyplot as plt

from build_japanese_garden import build_japanese_house
from build_japanese_garden import build_sakura
from build_japanese_garden import build_torii

def if_air(editor, vector):
    '''
    evaluate whether the block is air
    '''
    return editor.getBlock(vector) == Block('minecraft:air')

def if_water(editor, vector):
    '''
    evaluate whether the block is water
    '''
    if editor.getBlock(vector) == Block('minecraft:water',states={'level': '0'}):
        return True
    if editor.getBlock(vector) == Block('minecraft:seagrass'):
        return True
    if editor.getBlock(vector) == Block('minecraft:kelp',states={'age': '22'}):
        return True
    if editor.getBlock(vector) == Block('minecraft:kelp'):
        return True
    return False

if __name__ == '__main__':
    editor = Editor()
    editor.checkConnection()
    buildArea = editor.getBuildArea()
    buildRect = buildArea.toRect()
    editor.transform @= Transform(translation=addY(buildRect.offset))
    worldSlice = editor.loadWorldSlice(buildRect)
    heightmap = worldSlice.heightmaps["MOTION_BLOCKING_NO_LEAVES"]
    # heightmap
    plt.matshow(heightmap)
    plt.savefig("heightmap.png", dpi=500)

    BUILD_AREA_SIZE = ivec2(100, 100)  # build area size must be 100 * 100
    if dropY(buildArea.size) != BUILD_AREA_SIZE:
        print("Build Area must be 100 X 100")
        sys.exit(0)

    editor.buffering = False
    # editor.bufferLimit = 512

    ## find the surface of ocean
    print("Calculating The Surface of Ocean")
    if_ocean = np.zeros(shape=(100, 100))
    for i in range(100):
        for j in range(100):
            if if_water(editor, (i, heightmap[i, j] - 1, j)):
                if_ocean[i, j] = 1
    print("Done")
    ## find a good place of house
    print("Building House")
    candidate = []
    for i in range(5, 100 - 32):
        for j in range(5, 100 - 26):
            start_x = i - 2
            start_z = j - 2
            var = np.var(heightmap[start_x:start_x + 28, start_z:start_z + 23])
            ocean_score = np.sum(if_ocean[start_x:start_x + 28, start_z:start_z + 23])
            candidate.append((ocean_score, var, (i, j)))
    candidate = sorted(candidate)

    if candidate[0][0] > 0 and candidate[0][1] == 0:
        np.random.shuffle(candidate)

    min_height = np.min(
        heightmap[candidate[0][2][0]:candidate[0][2][0] + 24, candidate[0][2][1]:candidate[0][2][1] + 18])
    start_point_house = addY(ivec2(candidate[0][2][0] + 2, candidate[0][2][1] + 2), min_height)

    ## clear the leaves of the ground floor
    placeBox(editor, Box(addY(ivec2(candidate[0][2][0] - 2, candidate[0][2][1] - 2), min_height), (28, 40, 23)),
             Block("air"))

    build_japanese_house(editor, start_point_house)

    if np.sum(if_ocean[candidate[0][2][0]:candidate[0][2][0] + 24, candidate[0][2][1]:candidate[0][2][1] + 18]) > 0:
        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x, height, start_point_house.z)):
            placeBox(editor, Box(ivec3(start_point_house.x, height, start_point_house.z), (1, 1, 1)), Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 7, height, start_point_house.z)):
            placeBox(editor, Box(ivec3(start_point_house.x + 7, height, start_point_house.z), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 12, height, start_point_house.z)):
            placeBox(editor, Box(ivec3(start_point_house.x + 12, height, start_point_house.z), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 19, height, start_point_house.z)):
            placeBox(editor, Box(ivec3(start_point_house.x + 19, height, start_point_house.z), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x, height, start_point_house.z + 4)):
            placeBox(editor, Box(ivec3(start_point_house.x, height, start_point_house.z + 4), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x, height, start_point_house.z + 9)):
            placeBox(editor, Box(ivec3(start_point_house.x, height, start_point_house.z + 9), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x, height, start_point_house.z + 13)):
            placeBox(editor, Box(ivec3(start_point_house.x, height, start_point_house.z + 13), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 7, height, start_point_house.z + 13)):
            placeBox(editor, Box(ivec3(start_point_house.x + 7, height, start_point_house.z + 13), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 12, height, start_point_house.z + 13)):
            placeBox(editor, Box(ivec3(start_point_house.x + 12, height, start_point_house.z + 13), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 19, height, start_point_house.z + 13)):
            placeBox(editor, Box(ivec3(start_point_house.x + 19, height, start_point_house.z + 13), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 19, height, start_point_house.z + 4)):
            placeBox(editor, Box(ivec3(start_point_house.x + 19, height, start_point_house.z + 4), (1, 1, 1)),
                     Block("stone"))
            height -= 1

        height = min_height - 1
        while if_water(editor, ivec3(start_point_house.x + 19, height, start_point_house.z + 9)):
            placeBox(editor, Box(ivec3(start_point_house.x + 19, height, start_point_house.z + 9), (1, 1, 1)),
                     Block("stone"))
            height -= 1

    if_occupied = np.zeros((100, 100))
    if_occupied[start_point_house.x - 2:start_point_house.x + 26, start_point_house.z - 2:start_point_house.z + 21] = 1
    print("Done")


    ## place torii
    print("Building Torii")
    torii_candidate = []
    min_x = 5
    max_x = 75
    min_z = start_point_house.z + 4
    max_z = 90
    if min_z > max_z:
        print("It's impossible to build Torii gate!")
    else:
        for i in range(min_x, max_x):
            for j in range(min_z, max_z):
                start_x = i
                start_z = j
                var = np.var(heightmap[start_x:start_x + 18, start_z:start_z + 3])
                ocean_score = np.sum(if_ocean[start_x:start_x + 18, start_z:start_z + 3])
                if np.sum(if_occupied[start_x:start_x + 18, start_z:start_z + 3]) == 0:
                    torii_candidate.append((ocean_score, var, (i, j)))
        torii_candidate = sorted(torii_candidate)
        if torii_candidate[0][0] > 0 and torii_candidate[0][1] == 0:
            np.random.shuffle(torii_candidate)
        start_point_torii = ivec2(torii_candidate[0][2][0] + 5, torii_candidate[0][2][1] + 1)
        min_height = np.min(
            heightmap[start_point_torii.x - 5:start_point_torii.x + 14, start_point_torii.y - 1:start_point_torii.y + 2])
        start_point_torii = addY(start_point_torii, min_height)
        placeBox(editor, Box((start_point_torii.x - 2, min_height + 4, start_point_torii.z - 2), (18, 10, 4)), Block("air"))
        if np.sum(if_ocean[start_point_torii.x - 5:start_point_torii.x + 14,
                  start_point_torii.z - 1:start_point_torii.z + 2]) > 0:
            height = min_height - 1
            while if_water(editor, ivec3(start_point_torii.x, height, start_point_torii.z)):
                placeBox(editor, Box(ivec3(start_point_torii.x, height, start_point_torii.z), (1, 1, 1)),
                         Block("nether_bricks"))
                height -= 1
            height = min_height - 1
            while if_water(editor, ivec3(start_point_torii.x + 8, height, start_point_torii.z)):
                placeBox(editor, Box(ivec3(start_point_torii.x + 8, height, start_point_torii.z), (1, 1, 1)),
                         Block("nether_bricks"))
                height -= 1

        placeBox(editor, Box((start_point_torii.x - 5, min_height, start_point_torii.z - 1), (18, 1, 3)), Block("air"))
        build_torii(editor, start_point_torii)
        if_occupied[start_point_torii.x - 5:start_point_torii.x + 14, start_point_torii.z - 3:start_point_torii.z + 5] = 1
        print("Done")


    ## place sakura
    print("Building Sakura Tree")
    # sakura_place = []
    while True:
        sakura_candidate = []
        min_x = max(5, start_point_house.x - 30)
        max_x = min(75, start_point_house.x + 24 + 30)
        min_z = max(5, start_point_house.z - 30)
        max_z = min(75, start_point_house.z + 18 + 30)
        for i in range(min_x, max_x):
            for j in range(min_z, max_z):
                start_x = i
                start_z = j
                var = np.var(heightmap[start_x:start_x + 19, start_z:start_z + 16])
                ocean_score = np.sum(if_ocean[start_x:start_x + 19, start_z:start_z + 16])
                if np.sum(if_occupied[start_x:start_x + 19, start_z:start_z + 16]) == 0:
                    sakura_candidate.append((ocean_score, var, (i, j)))
        sakura_candidate = sorted(sakura_candidate)
        if len(sakura_candidate) == 0:
            break
        if sakura_candidate[0][0] > 0 and sakura_candidate[0][1] == 0:
            np.random.shuffle(sakura_candidate)
        start_point_sakura_1 = ivec2(sakura_candidate[0][2][0] + 9, sakura_candidate[0][2][1] + 7)
        min_height = np.min(heightmap[start_point_sakura_1.x:start_point_sakura_1.x + 2,
                            start_point_sakura_1.y:start_point_sakura_1.y + 2])
        start_point_sakura_1 = addY(start_point_sakura_1, min_height)
        if np.sum(if_ocean[start_point_sakura_1.x:start_point_sakura_1.x + 2,
                  start_point_sakura_1.z:start_point_sakura_1.z + 2]) > 0:
            height = min_height - 1
            while if_water(editor, ivec3(start_point_sakura_1.x, height, start_point_sakura_1.z)):
                placeBox(editor, Box(ivec3(start_point_sakura_1.x, height, start_point_sakura_1.z), (1, 1, 1)),
                         Block("dark_oak_log"))
                height -= 1
            height = min_height - 1
            while if_water(editor, ivec3(start_point_sakura_1.x + 1, height, start_point_sakura_1.z)):
                placeBox(editor, Box(ivec3(start_point_sakura_1.x + 1, height, start_point_sakura_1.z), (1, 1, 1)),
                         Block("dark_oak_log"))
                height -= 1
            height = min_height - 1
            while if_water(editor, ivec3(start_point_sakura_1.x, height, start_point_sakura_1.z + 1)):
                placeBox(editor, Box(ivec3(start_point_sakura_1.x, height, start_point_sakura_1.z + 1), (1, 1, 1)),
                         Block("dark_oak_log"))
                height -= 1
            height = min_height - 1
            while if_water(editor, ivec3(start_point_sakura_1.x + 1, height, start_point_sakura_1.z + 1)):
                placeBox(editor, Box(ivec3(start_point_sakura_1.x + 1, height, start_point_sakura_1.z + 1), (1, 1, 1)),
                         Block("dark_oak_log"))
                height -= 1
            height = min_height - 1
        placeBox(editor, Box((start_point_sakura_1.x, min_height, start_point_sakura_1.z), (2, 1, 2)), Block("air"))
        build_sakura(editor, start_point_sakura_1)
        # sakura_place.append(start_point_sakura_1)
        if_occupied[start_point_sakura_1.x - 7:start_point_sakura_1.x + 7,
        start_point_sakura_1.z - 5:start_point_sakura_1.z + 7] = 1

        # if_occupied[start_point_sakura_1.x-9:start_point_sakura_1.x+10, start_point_sakura_1.z-7:start_point_sakura_1.z+9] = 1
    print("Done")


    sign = [Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"佐藤\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"铃木\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"高桥\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"田中\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"渡边\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"伊藤\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"中村\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"小林\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"山本\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"加藤\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"吉田\"}'}"),
            Block("oak_sign", {"rotation": "16", }, data="{Text1: '{\"text\": \"山田\"}'}")]
    sign_pos = ivec2(start_point_house.x + 12, start_point_house.z + 16)
    height = heightmap[tuple(sign_pos)]
    placeBox(editor, Box(addY(sign_pos, height + 1), (1, 1, 1)), np.random.choice(sign))

    ## 如果在水上 步行栈道

    width = start_point_house.z + 17
    while if_water(editor, ivec3(start_point_house.x + 7, start_point_house.y - 1, width)) or \
            if_water(editor, ivec3(start_point_house.x + 8, start_point_house.y - 1, width)) or \
            if_water(editor, ivec3(start_point_house.x + 9, start_point_house.y - 1, width)) or \
            if_water(editor, ivec3(start_point_house.x + 10, start_point_house.y - 1, width)) or \
            if_water(editor, ivec3(start_point_house.x + 11, start_point_house.y - 1, width)) or \
            if_water(editor, ivec3(start_point_house.x + 12, start_point_house.y - 1, width)):
        placeBox(editor, Box(ivec3(start_point_house.x + 7, start_point_house.y, width), (6, 1, 1)),
                 Block("spruce_slab"))
        width += 1


