import sys

import numpy as np
from glm import ivec2, ivec3

from gdpc import __url__, Editor, Block, Box, Transform
from gdpc.exceptions import InterfaceConnectionError, BuildAreaNotSetError
from gdpc.vector_tools import Y, addY, dropY, line3D, circle, fittingCylinder
from gdpc.transform import rotatedBoxTransform, flippedBoxTransform
from gdpc.geometry import placeBox, placeCheckeredBox
from gdpc.vector_tools import X, Y, Z, XZ, addY, dropY, loop2D, loop3D, perpendicular, toAxisVector2D

LANTERN_TYPE = [Block("lantern", {"hanging": "true"}), Block("soul_lantern", {"hanging": "true"})]
LANTERN_NAME = ["lantern", "soul_lantern"]
BOX_NAME = ["barrel", "chest", "bookshelf", "loom"]
BOX_WITHOUT_SHELF_NAME = ["barrel", "chest", "loom"]
TRAPDOOR_NAME = ["iron_trapdoor", "jungle_trapdoor", "acacia_trapdoor", "crimson_trapdoor", "warped_trapdoor"]
WALL_BANNER_NAME = ["white_wall_banner", "gray_wall_banner", "light_gray_wall_banner", "cyan_wall_banner", "brown_wall_banner",
                    "light_blue_wall_banner", "orange_wall_banner"]

PRISMARINE_NAME = ["prismarine", "prismarine_bricks", "dark_prismarine"]

def build_japanese_house(editor, point):
    """
    input:
        editor: object of our world
        point: the initial point of sakura tree
    """
    x = point.x
    y = point.y
    z = point.z

    ## build foundation

    placeBox(editor, Box((x, y + 1, z), (20, 1, 14)), Block("oak_planks"))
    placeBox(editor, Box((x + 3, y + 1, z + 3), (14, 1, 8)), Block("stone"))
    placeBox(editor, Box((x + 4, y + 1, z + 4), (12, 1, 6)), Block("stripped_oak_log"))

    for i in [0, 7, 12, 19]:
        for j in [0, 4, 9, 13]:
            if i == 7 or i == 12:
                if j == 4 or j == 9:
                    continue
            editor.placeBlock((x + i, y + 0, z + j), Block("dark_oak_log"))
            editor.placeBlock((x + i, y + 1, z + j), Block("dark_oak_log"))

    placeBox(editor, Box((x - 1, y + 1, z - 1), (1, 1, 16)), Block("polished_andesite_stairs", {"facing": "east"}))
    placeBox(editor, Box((x + 20, y + 1, z - 1), (1, 1, 16)), Block("polished_andesite_stairs", {"facing": "west"}))
    placeBox(editor, Box((x, y + 1, z - 1), (20, 1, 1)), Block("polished_andesite_stairs", {"facing": "south"}))
    placeBox(editor, Box((x, y + 1, z + 14), (20, 1, 1)), Block("polished_andesite_stairs", {"facing": "north"}))

    placeBox(editor, Box((x - 2, y + 0, z - 2), (1, 1, 18)), Block("polished_andesite_stairs", {"facing": "east"}))
    placeBox(editor, Box((x + 21, y + 0, z - 2), (1, 1, 18)), Block("polished_andesite_stairs", {"facing": "west"}))
    placeBox(editor, Box((x - 1, y + 0, z - 2), (22, 1, 1)), Block("polished_andesite_stairs", {"facing": "south"}))
    placeBox(editor, Box((x - 1, y + 0, z + 15), (22, 1, 1)), Block("polished_andesite_stairs", {"facing": "north"}))

    placeBox(editor, Box((x + 7, y + 1, z + 14), (6, 1, 1)), Block("air"))
    placeBox(editor, Box((x + 7, y + 0, z + 15), (6, 1, 1)), Block("air"))

    editor.placeBlock((x + 7, y + 1, z + 14), Block("polished_andesite"))
    editor.placeBlock((x + 7, y + 0, z + 15), Block("polished_andesite"))
    editor.placeBlock((x + 12, y + 1, z + 14), Block("polished_andesite"))
    editor.placeBlock((x + 12, y + 0, z + 15), Block("polished_andesite"))

    editor.placeBlock((x + 7, y + 0, z + 16), Block("polished_andesite_stairs", {"facing": "north"}))
    editor.placeBlock((x + 7, y + 1, z + 15), Block("polished_andesite_stairs", {"facing": "north"}))
    editor.placeBlock((x + 7, y + 2, z + 14), Block("polished_andesite_stairs", {"facing": "north"}))

    editor.placeBlock((x + 12, y + 0, z + 16), Block("polished_andesite_stairs", {"facing": "north"}))
    editor.placeBlock((x + 12, y + 1, z + 15), Block("polished_andesite_stairs", {"facing": "north"}))
    editor.placeBlock((x + 12, y + 2, z + 14), Block("polished_andesite_stairs", {"facing": "north"}))

    placeBox(editor, Box((x + 8, y + 1, z + 14), (4, 1, 1)), Block("oak_stairs", {"facing": "north"}))
    placeBox(editor, Box((x + 8, y + 0, z + 15), (4, 1, 1)), Block("oak_slab", {"type": "top"}))
    placeBox(editor, Box((x + 8, y + 0, z + 16), (4, 1, 1)), Block("oak_slab", {"type": "bottom"}))

    ## build framework
    placeBox(editor, Box((x + 3, y + 2, z + 3), (1, 14, 8)), Block("smooth_sandstone"))
    placeBox(editor, Box((x + 3, y + 2, z + 3), (14, 14, 1)), Block("smooth_sandstone"))
    placeBox(editor, Box((x + 16, y + 2, z + 3), (1, 14, 8)), Block("smooth_sandstone"))
    placeBox(editor, Box((x + 3, y + 2, z + 10), (14, 14, 1)), Block("smooth_sandstone"))

    placeBox(editor, Box((x + 3, y + 2, z + 3), (1, 14, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 7, y + 2, z + 3), (1, 14, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 12, y + 2, z + 3), (1, 14, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 16, y + 2, z + 3), (1, 14, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 3, y + 2, z + 10), (1, 14, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 7, y + 2, z + 10), (1, 14, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 12, y + 2, z + 10), (1, 14, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 16, y + 2, z + 10), (1, 14, 1)), Block("dark_oak_log"))

    placeBox(editor, Box((x + 3, y + 9, z + 3), (14, 1, 8)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 4, y + 9, z + 4), (12, 1, 6)), Block("air"))
    placeBox(editor, Box((x + 3, y + 15, z + 3), (14, 1, 8)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 4, y + 15, z + 4), (12, 1, 6)), Block("air"))

    ## build door
    # door of floor 1
    placeBox(editor, Box((x + 8, y + 2, z + 10), (4, 5, 1)), Block("air"))
    placeBox(editor, Box((x + 8, y + 6, z + 10), (4, 1, 1)), Block("dark_oak_log"))

    placeBox(editor, Box((x + 8, y + 5, z + 10), (1, 1, 1)),
             Block("dark_oak_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 11, y + 5, z + 10), (1, 1, 1)),
             Block("dark_oak_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 8, y + 2, z + 10), (1, 1, 1)), Block("dark_oak_stairs", {"facing": "west"}))
    placeBox(editor, Box((x + 11, y + 2, z + 10), (1, 1, 1)), Block("dark_oak_stairs", {"facing": "east"}))

    # decoration of the door
    placeBox(editor, Box((x + 9, y + 2, z + 10), (2, 1, 1)), Block("dark_oak_trapdoor"))
    placeBox(editor, Box((x + 9, y + 5, z + 10), (2, 1, 1)), Block("dark_oak_trapdoor", {"half": "top"}))

    placeBox(editor, Box((x + 8, y + 3, z + 10), (1, 2, 1)),
             Block("dark_oak_trapdoor", {"facing": "east", "open": "true"}))
    placeBox(editor, Box((x + 11, y + 3, z + 10), (1, 2, 1)),
             Block("dark_oak_trapdoor", {"facing": "west", "open": "true"}))

    # windows of floor 0
    placeBox(editor, Box((x + 5, y + 3, z + 10), (1, 2, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 14, y + 3, z + 10), (1, 2, 1)), Block("spruce_fence"))

    placeBox(editor, Box((x + 5, y + 3, z + 2), (1, 2, 1)),
             Block("spruce_trapdoor", {"facing": "north", "open": "true"}))
    placeBox(editor, Box((x + 14, y + 3, z + 2), (1, 2, 1)),
             Block("spruce_trapdoor", {"facing": "north", "open": "true"}))

    # door of floor 1

    placeBox(editor, Box((x + 9, y + 10, z + 10), (2, 3, 1)), Block("air"))

    placeBox(editor, Box((x + 9, y + 12, z + 10), (1, 1, 1)),
             Block("dark_oak_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 10, y + 12, z + 10), (1, 1, 1)),
             Block("dark_oak_stairs", {"facing": "east", "half": "top"}))

    placeBox(editor, Box((x + 9, y + 10, z + 10), (1, 2, 1)),
             Block("dark_oak_trapdoor", {"facing": "east", "open": "true"}))
    placeBox(editor, Box((x + 10, y + 10, z + 10), (1, 2, 1)),
             Block("dark_oak_trapdoor", {"facing": "west", "open": "true"}))

    placeBox(editor, Box((x + 5, y + 11, z + 10), (1, 2, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 14, y + 11, z + 10), (1, 2, 1)), Block("spruce_fence"))

    placeBox(editor, Box((x + 9, y + 10, z + 3), (2, 3, 1)), Block("air"))

    placeBox(editor, Box((x + 9, y + 12, z + 3), (1, 1, 1)),
             Block("dark_oak_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 10, y + 12, z + 3), (1, 1, 1)),
             Block("dark_oak_stairs", {"facing": "east", "half": "top"}))

    placeBox(editor, Box((x + 9, y + 10, z + 3), (1, 2, 1)),
             Block("dark_oak_trapdoor", {"facing": "east", "open": "true"}))
    placeBox(editor, Box((x + 10, y + 10, z + 3), (1, 2, 1)),
             Block("dark_oak_trapdoor", {"facing": "west", "open": "true"}))

    placeBox(editor, Box((x + 5, y + 11, z + 3), (1, 2, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 14, y + 11, z + 3), (1, 2, 1)), Block("spruce_fence"))

    ## eaves of floor 1
    placeBox(editor, Box((x + 2, y + 14, z + 2), (1, 1, 10)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 17, y + 14, z + 2), (1, 1, 10)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 2, y + 14, z + 2), (16, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "top"}))
    placeBox(editor, Box((x + 2, y + 14, z + 11), (16, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 9, y + 14, z + 11), (2, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 9, y + 14, z + 2), (2, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))

    ## eaves of roof

    placeBox(editor, Box((x + 2, y + 15, z + 2), (1, 1, 10)),
             Block("dark_prismarine_stairs", {"facing": "east", "half": "bottom"}))
    placeBox(editor, Box((x + 17, y + 15, z + 2), (1, 1, 10)),
             Block("dark_prismarine_stairs", {"facing": "west", "half": "bottom"}))
    placeBox(editor, Box((x + 2, y + 15, z + 2), (16, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 2, y + 15, z + 11), (16, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))

    placeBox(editor, Box((x + 2, y + 15, z + 2), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 3, y + 15, z + 2), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 2, y + 15, z + 3), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x + 17, y + 15, z + 2), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 16, y + 15, z + 2), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 17, y + 15, z + 3), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x + 2, y + 15, z + 11), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 3, y + 15, z + 11), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 2, y + 15, z + 10), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x + 17, y + 15, z + 11), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 16, y + 15, z + 11), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 17, y + 15, z + 10), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x + 2, y + 16, z + 2), (1, 1, 1)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 17, y + 16, z + 2), (1, 1, 1)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 2, y + 16, z + 11), (1, 1, 1)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 17, y + 16, z + 11), (1, 1, 1)), Block("dark_prismarine_slab"))

    ## ceiling of floor 1
    placeBox(editor, Box((x + 4, y + 15, z + 4), (12, 1, 6)), Block("spruce_planks"))

    ## eaves of roof
    ## 西边飞檐

    placeBox(editor, Box((x + 16, y + 16, z + 10), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 16, y + 16, z + 9), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))

    placeBox(editor, Box((x + 16, y + 17, z + 9), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 16, y + 17, z + 8), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))

    placeBox(editor, Box((x + 16, y + 18, z + 8), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 16, y + 18, z + 7), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))

    #### 镶花
    placeBox(editor, Box((x + 16, y + 16, z + 7), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))
    placeBox(editor, Box((x + 16, y + 17, z + 6), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))
    placeBox(editor, Box((x + 16, y + 16, z + 6), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x + 16, y + 17, z + 7), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 16, y + 19, z + 7), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "bottom"}))

    placeBox(editor, Box((x + 16, y + 16, z + 3), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 16, y + 16, z + 4), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 16, y + 17, z + 4), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 16, y + 17, z + 5), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 16, y + 18, z + 5), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 16, y + 18, z + 6), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 16, y + 19, z + 6), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "bottom"}))

    placeBox(editor, Box((x + 17, y + 19, z + 7), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 17, y + 19, z + 6), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))

    placeBox(editor, Box((x + 15, y + 16, z + 4), (1, 1, 6)), Block("smooth_sandstone"))
    placeBox(editor, Box((x + 15, y + 17, z + 5), (1, 1, 4)), Block("smooth_sandstone"))
    placeBox(editor, Box((x + 15, y + 18, z + 6), (1, 1, 2)), Block("smooth_sandstone"))

    ## 东边飞檐

    placeBox(editor, Box((x + 3, y + 16, z + 10), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 3, y + 16, z + 9), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))

    placeBox(editor, Box((x + 3, y + 17, z + 9), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 3, y + 17, z + 8), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))

    placeBox(editor, Box((x + 3, y + 18, z + 8), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 3, y + 18, z + 7), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))

    #### 镶花
    placeBox(editor, Box((x + 3, y + 16, z + 7), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))
    placeBox(editor, Box((x + 3, y + 17, z + 6), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "top"}))
    placeBox(editor, Box((x + 3, y + 16, z + 6), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x + 3, y + 17, z + 7), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 3, y + 19, z + 7), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "bottom"}))

    placeBox(editor, Box((x + 3, y + 16, z + 3), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 3, y + 16, z + 4), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 3, y + 17, z + 4), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 3, y + 17, z + 5), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 3, y + 18, z + 5), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 3, y + 18, z + 6), (1, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "top"}))

    placeBox(editor, Box((x + 3, y + 19, z + 6), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "bottom"}))

    placeBox(editor, Box((x + 2, y + 19, z + 7), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 2, y + 19, z + 6), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))

    placeBox(editor, Box((x + 4, y + 16, z + 4), (1, 1, 6)), Block("smooth_sandstone"))
    placeBox(editor, Box((x + 4, y + 17, z + 5), (1, 1, 4)), Block("smooth_sandstone"))
    placeBox(editor, Box((x + 4, y + 18, z + 6), (1, 1, 2)), Block("smooth_sandstone"))

    ## house top
    placeBox(editor, Box((x + 4, y + 16, z + 10), (12, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 4, y + 17, z + 9), (12, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x + 4, y + 18, z + 8), (12, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))

    placeBox(editor, Box((x + 4, y + 16, z + 3), (12, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 4, y + 17, z + 4), (12, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 4, y + 18, z + 5), (12, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))

    placeBox(editor, Box((x + 4, y + 19, z + 6), (12, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "bottom"}))
    placeBox(editor, Box((x + 4, y + 19, z + 7), (12, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "bottom"}))

    ## 精致的屋檐 北边
    placeBox(editor, Box((x + 1, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 16, z + 12), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 2, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 2, y + 14, z + 12), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 2, y + 13, z + 12), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 2, y + 12, z + 12), (1, 1, 1)), np.random.choice(LANTERN_TYPE))

    placeBox(editor, Box((x + 3, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 3, y + 14, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 4, y + 14, z + 12), (3, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 7, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 7, y + 14, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 8, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 9, y + 15, z + 12), (2, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x + 9, y + 16, z + 12), (2, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 11, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 12, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 12, y + 14, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 13, y + 14, z + 12), (3, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 16, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 16, y + 14, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 17, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 17, y + 14, z + 12), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 17, y + 13, z + 12), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 17, y + 12, z + 12), (1, 1, 1)), np.random.choice(LANTERN_TYPE))

    placeBox(editor, Box((x + 18, y + 15, z + 12), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 18, y + 16, z + 12), (1, 1, 1)), Block("polished_andesite"))

    ## 精致的屋檐 南边
    placeBox(editor, Box((x + 1, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 16, z + 1), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 2, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 2, y + 14, z + 1), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 2, y + 13, z + 1), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 2, y + 12, z + 1), (1, 1, 1)), np.random.choice(LANTERN_TYPE))

    placeBox(editor, Box((x + 3, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 3, y + 14, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 4, y + 14, z + 1), (3, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 7, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 7, y + 14, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 8, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 9, y + 15, z + 1), (2, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "top"}))
    placeBox(editor, Box((x + 9, y + 16, z + 1), (2, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 11, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 12, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 12, y + 14, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 13, y + 14, z + 1), (3, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 16, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 16, y + 14, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 17, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 17, y + 14, z + 1), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 17, y + 13, z + 1), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 17, y + 12, z + 1), (1, 1, 1)), np.random.choice(LANTERN_TYPE))

    placeBox(editor, Box((x + 18, y + 15, z + 1), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 18, y + 16, z + 1), (1, 1, 1)), Block("polished_andesite"))

    ## 精致的屋檐 东边

    placeBox(editor, Box((x + 1, y + 15, z + 2), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 1, y + 15, z + 3), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 1, y + 14, z + 3), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 14, z + 4), (1, 1, 6)), Block("polished_andesite"))
    placeBox(editor, Box((x + 1, y + 15, z + 10), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 1, y + 14, z + 10), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 15, z + 11), (1, 1, 1)), Block("polished_andesite"))

    ## 精致的屋檐 西边
    placeBox(editor, Box((x + 18, y + 15, z + 2), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 18, y + 15, z + 3), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 18, y + 14, z + 3), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 18, y + 14, z + 4), (1, 1, 6)), Block("polished_andesite"))
    placeBox(editor, Box((x + 18, y + 15, z + 10), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 18, y + 14, z + 10), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 18, y + 15, z + 11), (1, 1, 1)), Block("polished_andesite"))


    # second roof

    for i in [0, 7, 12, 19]:
        for j in [0, 4, 9, 13]:
            if i == 7 or i == 12:
                if j == 4 or j == 9:
                    continue
            placeBox(editor, Box((x + i, y + 2, z + j), (1, 6, 1)), Block("dark_oak_log"))

    placeBox(editor, Box((x, y + 7, z), (20, 1, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x, y + 7, z), (1, 1, 14)), Block("dark_oak_log"))
    placeBox(editor, Box((x, y + 7, z + 13), (20, 1, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 19, y + 7, z), (1, 1, 14)), Block("dark_oak_log"))

    placeBox(editor, Box((x - 1, y + 6, z - 1), (1, 1, 16)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 20, y + 6, z - 1), (1, 1, 16)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x - 1, y + 6, z - 1), (22, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x - 1, y + 6, z + 14), (22, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))

    placeBox(editor, Box((x - 1, y + 6, z), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x - 1, y + 6, z - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x - 1, y + 6, z + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))

    placeBox(editor, Box((x + 1, y + 6, z), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 1, y + 6, z - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 1, y + 6, z + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))

    placeBox(editor, Box((x, y + 6, z + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x, y + 6, z - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "top"}))

    placeBox(editor, Box((x + 19 - 1, y + 6, z), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 19 - 1, y + 6, z - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 19 - 1, y + 6, z + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))

    placeBox(editor, Box((x + 19 + 1, y + 6, z), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 19 + 1, y + 6, z - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 19 + 1, y + 6, z + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))

    placeBox(editor, Box((x + 19, y + 6, z + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x + 19, y + 6, z - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "top"}))

    placeBox(editor, Box((x - 1, y + 6, z + 13), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x - 1, y + 6, z + 13 - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x - 1, y + 6, z + 13 + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))

    placeBox(editor, Box((x + 1, y + 6, z + 13), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 1, y + 6, z + 13 - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 1, y + 6, z + 13 + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))

    placeBox(editor, Box((x, y + 6, z + 13 + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x, y + 6, z + 13 - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "top"}))

    placeBox(editor, Box((x + 19 - 1, y + 6, z + 13), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 19 - 1, y + 6, z + 13 - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 19 - 1, y + 6, z + 13 + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "east", "half": "top"}))

    placeBox(editor, Box((x + 19 + 1, y + 6, z + 13), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 19 + 1, y + 6, z + 13 - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 19 + 1, y + 6, z + 13 + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "west", "half": "top"}))

    placeBox(editor, Box((x + 19, y + 6, z + 13 + 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x + 19, y + 6, z + 13 - 1), (1, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "top"}))

    ## 一层屋顶屋檐

    placeBox(editor, Box((x - 1, y + 7, z - 1), (1, 1, 16)),
             Block("dark_prismarine_stairs", {"facing": "east", "half": "bottom"}))
    placeBox(editor, Box((x + 20, y + 7, z - 1), (1, 1, 16)),
             Block("dark_prismarine_stairs", {"facing": "west", "half": "bottom"}))
    placeBox(editor, Box((x - 1, y + 7, z + 14), (22, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "north", "half": "bottom"}))
    placeBox(editor, Box((x - 1, y + 7, z - 1), (22, 1, 1)),
             Block("dark_prismarine_stairs", {"facing": "south", "half": "bottom"}))

    placeBox(editor, Box((x - 1, y + 7, z - 1), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x, y + 7, z - 1), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x - 1, y + 7, z), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x + 20, y + 7, z - 1), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 19, y + 7, z - 1), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 20, y + 7, z), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x - 1, y + 7, z + 14), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x, y + 7, z + 14), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x - 1, y + 7, z + 13), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x + 20, y + 7, z + 14), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 19, y + 7, z + 14), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 20, y + 7, z + 13), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x - 1, y + 8, z - 1), (1, 1, 1)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 20, y + 8, z - 1), (1, 1, 1)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x - 1, y + 8, z + 14), (1, 1, 1)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 20, y + 8, z + 14), (1, 1, 1)), Block("dark_prismarine_slab"))

    placeBox(editor, Box((x, y + 7, z), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 19, y + 7, z), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x, y + 7, z + 13), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 19, y + 7, z + 13), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x, y + 8, z + 1), (1, 1, 12)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 19, y + 8, z + 1), (1, 1, 12)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 1, y + 8, z), (18, 1, 1)), Block("dark_prismarine_slab"))
    placeBox(editor, Box((x + 1, y + 8, z + 13), (18, 1, 1)), Block("dark_prismarine_slab"))

    placeBox(editor, Box((x + 1, y + 7, z + 1), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 18, y + 7, z + 1), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 18, y + 7, z + 12), (1, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 1, y + 7, z + 12), (1, 1, 1)), Block("dark_prismarine"))

    placeBox(editor, Box((x + 1, y + 8, z + 1), (1, 1, 12)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 18, y + 8, z + 1), (1, 1, 12)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 1, y + 8, z + 1), (18, 1, 1)), Block("dark_prismarine"))
    placeBox(editor, Box((x + 1, y + 8, z + 12), (18, 1, 1)), Block("dark_prismarine"))

    # 二楼围栏

    placeBox(editor, Box((x + 2, y + 9, z + 2), (1, 1, 10)), Block("spruce_planks"))
    placeBox(editor, Box((x + 17, y + 9, z + 2), (1, 1, 10)), Block("spruce_planks"))
    placeBox(editor, Box((x + 2, y + 9, z + 2), (16, 1, 1)), Block("spruce_planks"))
    placeBox(editor, Box((x + 2, y + 9, z + 11), (16, 1, 1)), Block("spruce_planks"))

    placeBox(editor, Box((x + 1, y + 9, z + 1), (1, 1, 12)), Block("spruce_slab", {"type": "top"}))
    placeBox(editor, Box((x + 18, y + 9, z + 1), (1, 1, 12)), Block("spruce_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 9, z + 1), (18, 1, 1)), Block("spruce_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 9, z + 12), (18, 1, 1)), Block("spruce_slab", {"type": "top"}))

    placeBox(editor, Box((x + 1, y + 10, z + 1), (1, 1, 12)), Block("lectern", {"facing": "east"}))
    placeBox(editor, Box((x + 18, y + 10, z + 1), (1, 1, 12)), Block("lectern", {"facing": "west"}))
    placeBox(editor, Box((x + 1, y + 10, z + 1), (18, 1, 1)), Block("lectern", {"facing": "south"}))
    placeBox(editor, Box((x + 1, y + 10, z + 12), (18, 1, 1)), Block("lectern", {"facing": "north"}))

    placeBox(editor, Box((x + 1, y + 11, z + 1), (1, 1, 12)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x + 18, y + 11, z + 1), (1, 1, 12)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x + 1, y + 11, z + 1), (18, 1, 1)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x + 1, y + 11, z + 12), (18, 1, 1)), Block("spruce_trapdoor"))

    placeBox(editor, Box((x + 1, y + 9, z + 1), (1, 1, 1)), Block("spruce_trapdoor", {"half": "top"}))
    placeBox(editor, Box((x + 18, y + 9, z + 1), (1, 1, 1)), Block("spruce_trapdoor", {"half": "top"}))
    placeBox(editor, Box((x + 18, y + 9, z + 12), (1, 1, 1)), Block("spruce_trapdoor", {"half": "top"}))
    placeBox(editor, Box((x + 1, y + 9, z + 12), (1, 1, 1)), Block("spruce_trapdoor", {"half": "top"}))

    placeBox(editor, Box((x + 1, y + 10, z + 1), (1, 1, 1)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x + 18, y + 10, z + 1), (1, 1, 1)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x + 18, y + 10, z + 12), (1, 1, 1)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x + 1, y + 10, z + 12), (1, 1, 1)), Block("spruce_trapdoor"))

    placeBox(editor, Box((x + 1, y + 11, z + 1), (1, 1, 1)), Block("air"))
    placeBox(editor, Box((x + 18, y + 11, z + 1), (1, 1, 1)), Block("air"))
    placeBox(editor, Box((x + 18, y + 11, z + 12), (1, 1, 1)), Block("air"))
    placeBox(editor, Box((x + 1, y + 11, z + 12), (1, 1, 1)), Block("air"))

    # 一楼围栏
    placeBox(editor, Box((x, y + 2, z), (1, 1, 14)), Block("lectern", {"facing": "east"}))
    placeBox(editor, Box((x + 19, y + 2, z), (1, 1, 14)), Block("lectern", {"facing": "west"}))
    placeBox(editor, Box((x, y + 2, z), (20, 1, 1)), Block("lectern", {"facing": "south"}))
    placeBox(editor, Box((x, y + 2, z + 13), (20, 1, 1)), Block("lectern", {"facing": "north"}))

    placeBox(editor, Box((x, y + 3, z), (1, 1, 14)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x + 19, y + 3, z), (1, 1, 14)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x, y + 3, z), (20, 1, 1)), Block("spruce_trapdoor"))
    placeBox(editor, Box((x, y + 3, z + 13), (20, 1, 1)), Block("spruce_trapdoor"))

    for i in [0, 7, 12, 19]:
        for j in [0, 4, 9, 13]:
            if i == 7 or i == 12:
                if j == 4 or j == 9:
                    continue
            placeBox(editor, Box((x + i, y + 2, z + j), (1, 2, 1)), Block("dark_oak_log"))

    placeBox(editor, Box((x + 8, y + 2, z + 13), (4, 1, 1)), Block("air"))
    placeBox(editor, Box((x + 8, y + 3, z + 13), (4, 1, 1)), Block("air"))

    ## 一楼屋檐 北面（正面）
    placeBox(editor, Box((x - 2, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x - 2, y + 8, z + 15), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x - 1, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x - 1, y + 6, z + 15), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x - 1, y + 5, z + 15), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x - 1, y + 4, z + 15), (1, 1, 1)), np.random.choice(LANTERN_TYPE))
    placeBox(editor, Box((x, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x, y + 6, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 6, z + 15), (6, 1, 1)), Block("polished_andesite"))

    placeBox(editor, Box((x + 7, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 7, y + 6, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 8, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite"))

    placeBox(editor, Box((x + 9, y + 7, z + 15), (2, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "north", "half": "top"}))
    placeBox(editor, Box((x + 9, y + 8, z + 15), (2, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 11, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 12, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 12, y + 6, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 13, y + 6, z + 15), (6, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 19, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 19, y + 6, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 20, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 20, y + 6, z + 15), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 20, y + 5, z + 15), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 20, y + 4, z + 15), (1, 1, 1)), np.random.choice(LANTERN_TYPE))

    placeBox(editor, Box((x + 21, y + 7, z + 15), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 21, y + 8, z + 15), (1, 1, 1)), Block("polished_andesite"))

    ## 一楼精致的屋檐 南面
    placeBox(editor, Box((x - 2, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x - 2, y + 8, z - 2), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x - 1, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x - 1, y + 6, z - 2), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x - 1, y + 5, z - 2), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x - 1, y + 4, z - 2), (1, 1, 1)), np.random.choice(LANTERN_TYPE))
    placeBox(editor, Box((x, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x, y + 6, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 1, y + 6, z - 2), (6, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 7, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 7, y + 6, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 8, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite"))

    placeBox(editor, Box((x + 9, y + 7, z - 2), (2, 1, 1)),
             Block("polished_andesite_stairs", {"facing": "south", "half": "top"}))
    placeBox(editor, Box((x + 9, y + 8, z - 2), (2, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 11, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 12, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 12, y + 6, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 13, y + 6, z - 2), (6, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 19, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 19, y + 6, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 20, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 20, y + 6, z - 2), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 20, y + 5, z - 2), (1, 1, 1)), Block("chain"))
    placeBox(editor, Box((x + 20, y + 4, z - 2), (1, 1, 1)), np.random.choice(LANTERN_TYPE))

    placeBox(editor, Box((x + 21, y + 7, z - 2), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 21, y + 8, z - 2), (1, 1, 1)), Block("polished_andesite"))

    ## 一楼精致的屋檐 东边

    placeBox(editor, Box((x - 2, y + 7, z - 1), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x - 2, y + 7, z), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x - 2, y + 6, z), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x - 2, y + 6, z + 1), (1, 1, 12)), Block("polished_andesite"))
    placeBox(editor, Box((x - 2, y + 7, z + 13), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x - 2, y + 6, z + 13), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x - 2, y + 7, z + 14), (1, 1, 1)), Block("polished_andesite"))

    ## 一楼精致的屋檐 西边
    placeBox(editor, Box((x + 21, y + 7, z - 1), (1, 1, 1)), Block("polished_andesite"))
    placeBox(editor, Box((x + 21, y + 7, z), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 21, y + 6, z), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 21, y + 6, z + 1), (1, 1, 12)), Block("polished_andesite"))
    placeBox(editor, Box((x + 21, y + 7, z + 13), (1, 1, 1)), Block("polished_andesite_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 21, y + 6, z + 13), (1, 1, 1)), Block("polished_andesite_slab", {"type": "top"}))
    placeBox(editor, Box((x + 21, y + 7, z + 14), (1, 1, 1)), Block("polished_andesite"))


    # interior decoration

    placeBox(editor, Box((x + 4, y + 4, z + 8), (1, 1, 1)), Block("wall_torch", {"facing": "east"}))

    placeBox(editor, Box((x + 13, y + 1, z + 5), (2, 1, 4)), Block("air"))
    placeBox(editor, Box((x + 13, y, z + 5), (2, 1, 1)), Block("stripped_oak_log"))

    # 座位
    placeBox(editor, Box((x + 13, y + 1, z + 5), (1, 1, 1)), Block("snow", {"layers": "5"}))
    placeBox(editor, Box((x + 14, y + 1, z + 5), (1, 1, 1)), Block("snow", {"layers": "4"}))

    placeBox(editor, Box((x + 13, y + 1, z + 8), (1, 1, 1)), Block("snow", {"layers": "4"}))
    placeBox(editor, Box((x + 14, y + 1, z + 8), (1, 1, 1)), Block("snow", {"layers": "5"}))

    placeBox(editor, Box((x + 14, y + 2, z + 9), (1, 1, 1)), Block("snow", {"layers": "1"}))
    placeBox(editor, Box((x + 15, y + 2, z + 9), (1, 1, 1)), Block("snow", {"layers": "3"}))

    placeBox(editor, Box((x + 13, y, z + 8), (2, 1, 1)), Block("stripped_oak_log"))
    placeBox(editor, Box((x + 13, y, z + 6), (2, 1, 2)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 13, y + 1, z + 6), (2, 1, 2)), Block("spruce_trapdoor", {"half": "top"}))

    # 橱柜
    placeBox(editor, Box((x + 15, y + 2, z + 5), (1, 1, 4)), Block("spruce_trapdoor", {"half": "top"}))
    placeBox(editor, Box((x + 15, y + 3, z + 5), (1, 1, 1)), Block(np.random.choice(LANTERN_NAME)))
    placeBox(editor, Box((x + 15, y + 3, z + 6), (1, 1, 1)), Block("heavy_weighted_pressure_plate"))
    placeBox(editor, Box((x + 15, y + 3, z + 7), (1, 1, 1)), Block("flower_pot"))
    placeBox(editor, Box((x + 15, y + 3, z + 8), (1, 1, 1)), Block(np.random.choice(LANTERN_NAME)))

    placeBox(editor, Box((x + 12, y + 2, z + 9), (1, 3, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 12, y + 2, z + 4), (1, 3, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 12, y + 5, z + 4), (1, 1, 6)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 12, y + 6, z + 4), (1, 1, 6)), Block("spruce_fence"))
    placeBox(editor, Box((x + 13, y + 5, z + 4), (3, 1, 6)), Block("spruce_slab", {"type": "top"}))
    placeBox(editor, Box((x + 14, y + 2, z + 4), (1, 4, 1)), Block("ladder", {"facing": "south"}))

    # 一楼夹层
    placeBox(editor, Box((x + 13, y + 6, z + 9), (1, 3, 1)), Block(np.random.choice(BOX_NAME)))
    placeBox(editor, Box((x + 14, y + 6, z + 9), (1, 2, 1)), Block(np.random.choice(BOX_NAME)))
    placeBox(editor, Box((x + 15, y + 6, z + 9), (1, 2, 1)), Block(np.random.choice(BOX_NAME)))

    placeBox(editor, Box((x + 15, y + 7, z + 8), (1, 1, 1)), Block("spruce_stairs", {"half": "top", "facing": "south"}))
    placeBox(editor, Box((x + 15, y + 7, z + 7), (1, 1, 1)), Block("spruce_trapdoor", {"half": "top"}))
    placeBox(editor, Box((x + 15, y + 6, z + 6), (1, 3, 1)), Block(np.random.choice(BOX_WITHOUT_SHELF_NAME), {"facing": "west"}))
    placeBox(editor, Box((x + 15, y + 7, z + 5), (1, 1, 1)), Block("spruce_trapdoor", {"half": "top"}))
    placeBox(editor, Box((x + 15, y + 8, z + 9), (1, 1, 1)), Block(np.random.choice(LANTERN_NAME)))
    placeBox(editor, Box((x + 15, y + 6, z + 5), (1, 1, 1)), Block("furnace"))
    placeBox(editor, Box((x + 15, y + 7, z + 4), (1, 1, 1)), Block("spruce_stairs", {"half": "top", "facing": "north"}))
    placeBox(editor, Box((x + 15, y + 8, z + 4), (1, 1, 1)), Block(np.random.choice(BOX_WITHOUT_SHELF_NAME), {"facing": "west"}))

    ## 二楼地板
    placeBox(editor, Box((x + 4, y + 9, z + 4), (12, 1, 6)), Block("spruce_slab", {"type": "top"}))
    placeBox(editor, Box((x + 4, y + 9, z + 8), (4, 1, 2)), Block("air"))

    ## 楼梯
    placeBox(editor, Box((x + 6, y + 2, z + 4), (1, 1, 2)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 4, y + 3, z + 4), (2, 1, 2)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 4, y + 4, z + 6), (2, 1, 1)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 4, y + 5, z + 7), (2, 1, 1)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 4, y + 6, z + 8), (2, 1, 2)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 6, y + 7, z + 8), (1, 1, 2)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 7, y + 8, z + 8), (1, 1, 2)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 8, y + 9, z + 8), (1, 1, 2)), Block("spruce_slab", {"type": "bottom"}))

    placeBox(editor, Box((x + 4, y + 2, z + 4), (2, 1, 2)), Block("spruce_fence_gate"))
    placeBox(editor, Box((x + 4, y + 3, z + 6), (2, 1, 1)), Block("spruce_fence_gate"))
    placeBox(editor, Box((x + 4, y + 4, z + 7), (2, 1, 1)), Block("spruce_fence_gate"))
    placeBox(editor, Box((x + 4, y + 5, z + 8), (2, 1, 2)), Block("spruce_fence_gate"))
    placeBox(editor, Box((x + 6, y + 6, z + 8), (1, 1, 2)), Block("spruce_fence_gate"))
    placeBox(editor, Box((x + 7, y + 7, z + 8), (1, 1, 2)), Block("spruce_fence_gate"))
    placeBox(editor, Box((x + 8, y + 8, z + 8), (1, 1, 2)), Block("spruce_fence_gate"))

    ## 二楼卧室

    placeBox(editor, Box((x + 15, y + 10, z + 4), (1, 1, 6)), Block("spruce_planks"))
    placeBox(editor, Box((x + 13, y + 10, z + 4), (2, 1, 1)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 12, y + 10, z + 4), (1, 1, 1)), Block("spruce_planks"))
    placeBox(editor, Box((x + 12, y + 11, z + 4), (1, 3, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 12, y + 14, z + 4), (1, 1, 1)), Block("spruce_planks"))
    placeBox(editor, Box((x + 13, y + 10, z + 9), (2, 1, 1)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 12, y + 10, z + 9), (1, 1, 1)), Block("spruce_planks"))
    placeBox(editor, Box((x + 12, y + 11, z + 9), (1, 3, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 12, y + 10, z + 5), (1, 1, 4)), Block("spruce_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 12, y + 14, z + 5), (1, 1, 4)), Block("spruce_slab", {"type": "top"}))
    placeBox(editor, Box((x + 12, y + 14, z + 9), (1, 1, 1)), Block("spruce_planks"))
    placeBox(editor, Box((x + 13, y + 10, z + 5), (1, 1, 4)), Block("light_gray_bed", {"facing": "east"}))

    placeBox(editor, Box((x + 14, y + 13, z + 9), (1, 1, 1)), Block("wall_torch", {"facing": "north"}))
    placeBox(editor, Box((x + 14, y + 13, z + 4), (1, 1, 1)), Block("wall_torch", {"facing": "south"}))
    placeBox(editor, Box((x + 15, y + 11, z + 4), (1, 4, 6)),
             Block(np.random.choice(TRAPDOOR_NAME), {"half": "bottom", "facing": "west", "open": "true"}))
    placeBox(editor, Box((x + 15, y + 11, z + 5), (1, 2, 4)), Block("air"))
    placeBox(editor, Box((x + 15, y + 12, z + 5), (1, 1, 4)), Block(np.random.choice(WALL_BANNER_NAME), {"facing": "west"}))

    ## 二楼到三楼的楼梯处修建

    placeBox(editor, Box((x + 4, y + 10, z + 7), (5, 1, 1)), Block("spruce_fence"))
    placeBox(editor, Box((x + 4, y + 10, z + 6), (1, 5, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 5, y + 15, z + 6), (1, 1, 1)), Block("air"))
    placeBox(editor, Box((x + 5, y + 10, z + 6), (1, 5, 1)), Block("ladder", {"facing": "east"}))

    ## 二楼小书房
    placeBox(editor, Box((x + 9, y + 14, z + 9), (2, 1, 1)), Block(np.random.choice(WALL_BANNER_NAME), {"facing": "north"}))
    placeBox(editor, Box((x + 9, y + 14, z + 4), (2, 1, 1)), Block(np.random.choice(WALL_BANNER_NAME), {"facing": "south"}))
    placeBox(editor, Box((x + 4, y + 10, z + 4), (1, 1, 1)), Block("scaffolding"))
    placeBox(editor, Box((x + 4, y + 11, z + 4), (1, 1, 1)), Block(np.random.choice(LANTERN_NAME)))
    placeBox(editor, Box((x + 4, y + 12, z + 4), (1, 1, 2)),
             Block("spruce_trapdoor", {"half": "bottom", "open": "false", "facing": "south"}))
    placeBox(editor, Box((x + 4, y + 10, z + 5), (1, 1, 1)), Block(np.random.choice(BOX_NAME)))
    placeBox(editor, Box((x + 5, y + 10, z + 4), (3, 1, 1)),
             Block("spruce_trapdoor", {"half": "top", "open": "false", "facing": "north"}))
    placeBox(editor, Box((x + 8, y + 10, z + 4), (1, 1, 1)), Block("dark_oak_log"))
    placeBox(editor, Box((x + 8, y + 11, z + 4), (1, 1, 1)), Block(np.random.choice(BOX_NAME)))
    placeBox(editor, Box((x + 6, y + 11, z + 4), (1, 1, 1)), Block("heavy_weighted_pressure_plate"))
    placeBox(editor, Box((x + 5, y + 11, z + 4), (1, 1, 1)), Block("sea_pickle", {"waterlogged": "false"}))
    placeBox(editor, Box((x + 6, y + 10, z + 5), (1, 1, 1)), Block("white_carpet"))
    placeBox(editor, Box((x + 6, y + 10, z + 6), (1, 1, 1)),
             Block(np.random.choice(TRAPDOOR_NAME), {"half": "bottom", "open": "true", "facing": "south"}))

    ## 阁楼
    placeBox(editor, Box((x + 5, y + 18, z + 7), (1, 1, 1)), np.random.choice(LANTERN_TYPE))
    placeBox(editor, Box((x + 5, y + 18, z + 6), (1, 1, 1)), np.random.choice(LANTERN_TYPE))
    placeBox(editor, Box((x + 14, y + 18, z + 7), (1, 1, 1)), np.random.choice(LANTERN_TYPE))
    placeBox(editor, Box((x + 14, y + 18, z + 6), (1, 1, 1)), np.random.choice(LANTERN_TYPE))

    placeBox(editor, Box((x + 14, y + 16, z + 4), (1, 1, 6)), Block(np.random.choice(BOX_NAME)))
    placeBox(editor, Box((x + 14, y + 17, z + 5), (1, 1, 4)), Block(np.random.choice(BOX_WITHOUT_SHELF_NAME), {"facing": "west"}))
    placeBox(editor, Box((x + 10, y + 16, z + 4), (4, 1, 1)), Block(np.random.choice(BOX_WITHOUT_SHELF_NAME), {"facing": "north"}))
    placeBox(editor, Box((x + 7, y + 16, z + 4), (3, 1, 1)), Block(np.random.choice(BOX_NAME)))
    placeBox(editor, Box((x + 9, y + 16, z + 8), (5, 1, 1)), Block(np.random.choice(BOX_NAME)))
    placeBox(editor, Box((x + 5, y + 16, z + 8), (4, 1, 1)), Block("spruce_fence"))

    placeBox(editor, Box((x + 5, y + 2, z + 7), (2, 1, 2)), Block("dark_oak_slab", {"waterlogged": "true"}))
    placeBox(editor, Box((x + 5, y + 2, z + 6), (2, 1, 1)), Block("spruce_trapdoor", {"half": "top", "open": "true"}))
    placeBox(editor, Box((x + 7, y + 2, z + 7), (1, 1, 2)),
             Block("spruce_trapdoor", {"half": "bottom", "open": "true", "facing": "east"}))
    placeBox(editor, Box((x + 4, y + 2, z + 7), (1, 1, 2)),
             Block("spruce_trapdoor", {"half": "bottom", "open": "true", "facing": "west"}))
    placeBox(editor, Box((x + 5, y + 2, z + 9), (2, 1, 1)),
             Block("spruce_trapdoor", {"half": "top", "open": "true", "facing": "south"}))

    placeBox(editor, Box((x + 4, y + 4, z + 9), (1, 1, 1)), Block("white_wall_banner", {"facing": "east"}))
    placeBox(editor, Box((x + 6, y + 4, z + 9), (1, 1, 1)),
             Block("bell", {"facing": "south", "attachment": "single_wall"}))

    placeBox(editor, Box((x + 9, y + 2, z + 4), (2, 1, 2)), Block("stripped_birch_wood"))
    placeBox(editor, Box((x + 8, y + 2, z + 4), (1, 4, 1)),
             Block("dark_oak_trapdoor", {"half": "top", "open": "true", "facing": "west"}))
    placeBox(editor, Box((x + 8, y + 3, z + 5), (1, 3, 1)),
             Block("dark_oak_trapdoor", {"half": "bottom", "open": "true", "facing": "south"}))
    placeBox(editor, Box((x + 11, y + 2, z + 4), (1, 4, 1)),
             Block("dark_oak_trapdoor", {"half": "top", "open": "true", "facing": "east"}))
    placeBox(editor, Box((x + 11, y + 3, z + 5), (1, 3, 1)),
             Block("dark_oak_trapdoor", {"half": "bottom", "open": "true", "facing": "south"}))
    placeBox(editor, Box((x + 9, y + 6, z + 4), (2, 1, 1)), Block("dark_oak_slab", {"type": "bottom"}))
    placeBox(editor, Box((x + 9, y + 5, z + 4), (2, 1, 1)), np.random.choice(LANTERN_TYPE))
    placeBox(editor, Box((x + 9, y + 3, z + 4), (2, 1, 1)), Block("end_rod"))
    placeBox(editor, Box((x + 9, y + 4, z + 4), (2, 1, 1)), Block(np.random.choice(WALL_BANNER_NAME), {"facing": "south"}))

    # 日式开关门
    pinfeng_bottom = np.random.choice(TRAPDOOR_NAME)
    pinfeng_top = np.random.choice(TRAPDOOR_NAME)
    placeBox(editor, Box((x + 12, y + 2, z + 5), (1, 1, 2)),
             Block(pinfeng_bottom, {"half": "bottom", "facing": "east", "open": "true"}))
    placeBox(editor, Box((x + 12, y + 3, z + 5), (1, 2, 2)),
             Block(pinfeng_top, {"half": "bottom", "facing": "east", "open": "true"}))
    placeBox(editor, Box((x + 11, y + 2, z + 6), (1, 1, 2)),
             Block(pinfeng_bottom, {"half": "bottom", "facing": "west", "open": "true"}))
    placeBox(editor, Box((x + 11, y + 3, z + 6), (1, 2, 2)),
             Block(pinfeng_top, {"half": "bottom", "facing": "west", "open": "true"}))


def build_torii(editor, point):
    """
    input:
        editor: object of our world
        point: the initial point of sakura tree
    """
    x = point.x
    y = point.y
    z = point.z

    placeBox(editor, Box((x, y, z), (1, 3, 1)), Block("nether_bricks"))
    placeBox(editor, Box((x - 1, y, z), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "east"}))
    placeBox(editor, Box((x + 1, y, z), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "west"}))
    placeBox(editor, Box((x, y, z - 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "south"}))
    placeBox(editor, Box((x, y, z + 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "north"}))

    placeBox(editor, Box((x + 8, y, z), (1, 3, 1)), Block("nether_bricks"))
    placeBox(editor, Box((x + 8 - 1, y, z), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "east"}))
    placeBox(editor, Box((x + 8 + 1, y, z), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "west"}))
    placeBox(editor, Box((x + 8, y, z - 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "south"}))
    placeBox(editor, Box((x + 8, y, z + 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "north"}))

    placeBox(editor, Box((x, y + 3, z), (1, 6, 1)), Block("red_nether_bricks"))
    placeBox(editor, Box((x + 8, y + 3, z), (1, 6, 1)), Block("red_nether_bricks"))

    placeBox(editor, Box((x - 2, y + 9, z), (13, 1, 1)), Block("red_nether_bricks"))
    placeBox(editor, Box((x + 8 - 1, y + 8, z), (1, 1, 1)), Block("red_nether_brick_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 8 + 1, y + 8, z), (1, 1, 1)), Block("red_nether_brick_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x - 1, y + 8, z), (1, 1, 1)), Block("red_nether_brick_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 1, y + 8, z), (1, 1, 1)), Block("red_nether_brick_stairs", {"facing": "west", "half": "top"}))

    placeBox(editor, Box((x, y + 10, z), (1, 1, 1)), Block("red_nether_bricks"))
    placeBox(editor, Box((x + 4, y + 10, z), (1, 1, 1)), Block("red_nether_bricks"))
    placeBox(editor, Box((x + 8, y + 10, z), (1, 1, 1)), Block("red_nether_bricks"))

    placeBox(editor, Box((x - 3, y + 11, z), (15, 1, 1)), Block("red_nether_bricks"))
    placeBox(editor, Box((x - 4, y + 12, z), (17, 1, 1)), Block("nether_bricks"))

    placeBox(editor, Box((x - 4, y + 13, z), (1, 1, 1)), Block("nether_bricks"))
    placeBox(editor, Box((x + 12, y + 13, z), (1, 1, 1)), Block("nether_bricks"))

    placeBox(editor, Box((x - 4, y + 12, z + 1), (17, 1, 1)), Block("nether_brick_stairs"))
    placeBox(editor, Box((x - 4, y + 12, z - 1), (17, 1, 1)), Block("nether_brick_stairs", {"facing": "south"}))

    placeBox(editor, Box((x - 4, y + 12, z + 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "east"}))
    placeBox(editor, Box((x - 4, y + 12, z - 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "east"}))
    placeBox(editor, Box((x + 12, y + 12, z - 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "west"}))
    placeBox(editor, Box((x + 12, y + 12, z + 1), (1, 1, 1)), Block("nether_brick_stairs", {"facing": "west"}))

    placeBox(editor, Box((x - 4, y + 11, z), (1, 1, 1)),
             Block("red_nether_brick_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x + 12, y + 11, z), (1, 1, 1)),
             Block("red_nether_brick_stairs", {"facing": "west", "half": "top"}))

    placeBox(editor, Box((x - 4, y + 11, z - 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x, y + 11, z - 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x + 4, y + 11, z - 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x + 8, y + 11, z - 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x + 12, y + 11, z - 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))

    placeBox(editor, Box((x - 4, y + 11, z + 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x, y + 11, z + 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x + 4, y + 11, z + 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x + 8, y + 11, z + 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))
    placeBox(editor, Box((x + 12, y + 11, z + 1), (1, 1, 1)), Block("soul_lantern", {"hanging": "true"}))

    placeBox(editor, Box((x - 5, y + 13, z), (1, 1, 1)),
             Block("nether_brick_stairs", {"facing": "east", "half": "top"}))
    placeBox(editor, Box((x - 5, y + 14, z), (1, 1, 1)),
             Block("nether_brick_stairs", {"facing": "west", "half": "bottom"}))
    placeBox(editor, Box((x - 3, y + 13, z), (4, 1, 1)), Block("nether_bricks"))
    placeBox(editor, Box((x + 1, y + 13, z), (2, 1, 1)), Block("nether_brick_slab"))
    placeBox(editor, Box((x - 4, y + 14, z), (2, 1, 1)), Block("nether_brick_slab"))

    placeBox(editor, Box((x + 13, y + 13, z), (1, 1, 1)),
             Block("nether_brick_stairs", {"facing": "west", "half": "top"}))
    placeBox(editor, Box((x + 13, y + 14, z), (1, 1, 1)),
             Block("nether_brick_stairs", {"facing": "east", "half": "bottom"}))
    placeBox(editor, Box((x + 8, y + 13, z), (4, 1, 1)), Block("nether_bricks"))
    placeBox(editor, Box((x + 6, y + 13, z), (2, 1, 1)), Block("nether_brick_slab"))
    placeBox(editor, Box((x + 11, y + 14, z), (2, 1, 1)), Block("nether_brick_slab"))

    placeBox(editor, Box((x + 4, y + 10, z - 1), (1, 1, 1)), Block("light_gray_wall_banner", {"facing": "north"}))
    placeBox(editor, Box((x + 4, y + 10, z + 1), (1, 1, 1)), Block("light_gray_wall_banner", {"facing": "south"}))




def build_sakura(editor, point):
    """
    input:
        editor: object of our world
        point: the initial point of sakura tree
    """
    x = point.x
    y = point.y
    z = point.z

    placeBox(editor, Box((x,y,z), (2,5,2)), Block("dark_oak_log"))
    placeBox(editor, Box((x+1,y+5,z+1), (1,3,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+1,y+7,z+2), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+2,y,z+1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+2,y+1,z+1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+2,y,z+2), (1,1,1)), Block("dark_oak_log"))

    placeBox(editor, Box((x,y,z+2), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+1,y+1,z+2), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+1,y,z+2), (1,1,1)), Block("dark_oak_log"))

    placeBox(editor, Box((x+2,y,z), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+2,y+1,z), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+2,y+2,z), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+3,y,z), (1,1,1)), Block("dark_oak_log"))

    placeBox(editor, Box((x,y,z-1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x,y+1,z-1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+1,y,z-1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+2,y,z-1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x,y,z-2), (1,1,1)), Block("dark_oak_log"))

    placeBox(editor, Box((x-1,y,z-1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-1,y,z), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-1,y+1,z), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-1,y,z+1), (1,1,1)), Block("dark_oak_log"))

    placeBox(editor, Box((x,y+6,z), (1,3,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+1,y+5,z+2), (1,1,1)), Block("dark_oak_log"))


    ## branch
    placeBox(editor, Box((x-3,y+5,z-1), (4,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-3,y+6,z-3), (1,1,2)), Block("dark_oak_log"))
    placeBox(editor, Box((x-4,y+7,z-3), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-4,y+8,z-4), (1,1,1)), Block("dark_oak_log"))

    placeBox(editor, Box((x+2,y+5,z+1), (2,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+3,y+6,z+1), (2,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+4,y+7,z+1), (2,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+5,y+8,z+1), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x+6,y+9,z+1), (1,1,1)), Block("dark_oak_log"))

    placeBox(editor, Box((x-1,y+5,z+2), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-2,y+5,z+3), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-3,y+5,z+4), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-4,y+5,z+5), (1,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-4,y+6,z+3), (1,1,2)), Block("dark_oak_log"))
    placeBox(editor, Box((x-4,y+7,z+1), (1,1,2)), Block("dark_oak_log"))
    placeBox(editor, Box((x-2,y+6,z+3), (1,1,2)), Block("dark_oak_log"))
    placeBox(editor, Box((x-2,y+7,z+4), (2,1,1)), Block("dark_oak_log"))
    placeBox(editor, Box((x-6,y+7,z+5), (2,1,1)), Block("dark_oak_log"))


    def if_branch(vector):
        if editor.getBlock(vector) == Block('minecraft:dark_oak_log',states={'axis': 'y'}):
            return True
        return False

    def if_close_branch(vector):
        '''
        evaluate whether this location close the branch, if it is, then place sakura
        Note, the block cannot be branch itself
        '''
        if if_branch(vector):
            return False
        for vec in loop3D((vector.x-1,vector.y-1,vector.z-1), (vector.x+2,vector.y+2,vector.z+2)):
            if if_branch(vec):
                return True
        return False

    def if_air(vector):
        return editor.getBlock(vector) == Block('minecraft:air')

    def if_close_sakura(vector):
        # if if_air(vector):
        #     return False
        for vec in loop3D((vector.x-1,vector.y-1,vector.z-1), (vector.x+2,vector.y+2,vector.z+2)):
            if not if_air(vec):
                return True
        return False

    leaves = [Block("pink_glazed_terracotta"), Block("pink_stained_glass"),
              Block("stripped_crimson_stem"),
              Block("pink_terracotta"), Block("pink_wool")]
    prob = [0.1, 0.1, 0.1, 0.1, 0.6]

    for vec in loop3D((x-7,y+4,z-5), (x+8,y+11,z+7)):
        # editor.placeBlock(vec, Block("air"))
        if if_close_branch(vec):
            if vec.y < y + 8:
                if np.random.random() < 0.5:
                    continue
            else:
                if np.random.random() < 0.3:
                    continue
            block = np.random.choice(leaves, p=prob)
            editor.placeBlock(vec, block)
    for vec in loop3D((x-9,y+10,z-7), (x+10,y+13,z+9)):
        # editor.placeBlock(vec, Block("air"))
        if if_close_sakura(vec):
            if np.random.random() < 0.8:
                continue
            block = np.random.choice(leaves, p=prob)
            editor.placeBlock(vec, block)

    for vec in loop3D((x-9,y+3,z-7), (x+10,y+13,z+9)):
        # editor.placeBlock(vec, Block("air"))
        if if_air(vec):
            top_block = ivec3(vec.x, vec.y+1, vec.z)
            if if_air(top_block):
                continue
            else:
                # editor.placeBlock(vec, Block("air"))
                if vec.y < y + 5:
                    if np.random.random() < 0.05:
                        editor.placeBlock(vec, np.random.choice(LANTERN_TYPE))
                else:
                    if np.random.random() < 0.03:
                        editor.placeBlock(vec, np.random.choice(LANTERN_TYPE))



if __name__ == '__main__':
    editor = Editor()
    editor.checkConnection()
    buildArea = editor.getBuildArea()
    buildRect = buildArea.toRect()

    BUILD_AREA_SIZE = ivec2(100, 100)  # build area size must be 100 * 100

    if dropY(buildArea.size) != BUILD_AREA_SIZE:
        print("Build Area must be 100 X 100")

    editor.transform @= Transform(translation=addY(buildRect.offset))

    house_point = ivec3(20, 0, 10)
    torii_point = ivec3(20, 0, 40)
    sakura_point = ivec3(20, 0, 60)

    build_japanese_house(editor, house_point)
    build_torii(editor, torii_point)
    build_sakura(editor, sakura_point)

