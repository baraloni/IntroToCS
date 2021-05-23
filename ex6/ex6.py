#######################################################################################
# FILE : ex6.py
# WRITER : Bar Aloni
# EXERCISE : intro2cs ex6 2016-2017
# DESCRIPTION :
# A program that creats a mosaic of a chosen image, from a stockpile of images
# (=tiles , all same sized). the program takes sections(in tile size) from the
# image, analayzes it, and finds best match from the tiles.(filtering first by
# comparing the distance between average colour of the image and tile, and
# later filters the smaller group by pixel-pixel compare to find best match).
# (more about mosaic: "https://en.wikipedia.org/wiki/Mosaic").
##########################################################################################
from copy import deepcopy
from mosaic import *
import sys
NUM_ARGS = 5


def compare_pixel(pixel1, pixel2):
    """
    :param pixel1: tup (red, green, blue) representing pixel colour
    :param pixel2: tup (red, green, blue) representing pixel colour
    :return: int, representing the distance between both pixel's colours
    """
    r1, g1, b1 = pixel1
    r2, g2, b2 = pixel2
    pixels_distance = abs(r1-r2) + abs(g1-g2) + abs(b1-b2)   # def. of distance between pixels
    return pixels_distance


def compare(image1, image2):
    """
    compare colors of 2 images, by pixel comparing
    :param image1: a list of image1-height size, when each item is a list of image1-width
    size of pixels:(r,g,b) int tuples
    :param image2: a list of image2-height size, when each item is a list of image2-width
    size of pixels:(r,g,b) int tuples
    :return: int representing the distance between the images
    """
    height = min(len(image1), len(image2))
    width = min(len(image1[0]), len(image2[0]))  # we assume all lists aren't empty
    img_distance = 0
    for row_idx in range(height):
        for col_idx in range(width):
            pixel1 = image1[row_idx][col_idx]
            pixel2 = image2[row_idx][col_idx]
            pixels_distance = compare_pixel(pixel1, pixel2)
            img_distance += pixels_distance
    return img_distance


def get_piece(image, upper_left, size):
    """
    :param image: a list of image1-height size, when each item is a int list of image1-width
    size of pixels:(r,g,b) int tuples
    :param upper_left: tuple of ints representing a pixel's location : (row, col)
    :param size: tuple of ints representing the size of the taken section: (height, width)
    :return: an image (a list of image1-height size, when each item is a int list of image1-width
    size of pixels:(r,g,b) int tuples) : a section of the image of the given size, starting at the
    location given in the parameter upper_left. if the size extend the image boundaries: will
    return the image bounded inside.
    """
    row_idx, col_idx = upper_left
    height, width = size
    row_end_idx = min(row_idx + height, len(image))   # left: apx. sec end, right: original img bound
    col_end_idx = min(col_idx + width, len(image[0]))
    section = []
    for row in range(row_idx, row_end_idx):
        new_row = []
        for col in range(col_idx, col_end_idx):
            pixel = image[row][col]
            new_row.append(pixel)
        section.append(new_row)
    return section


def set_piece(image, upper_left, piece):
    """
    :param image: a list of image1-height size, when each item is a int list of image1-width
    size of pixels:(r,g,b) int tuples
    :param upper_left: tuple of ints representing a pixel's location : (row, col)
    :param piece: another image of the same format
    :return: replaces the image's section starts at upper_left, in the image named piece
    """
    row_idx, col_idx = upper_left
    piece_height, piece_width = len(piece), len(piece[0])
    # expressions in min:  on left: apx. piece end, on right: original img bound
    row_end_idx = min(piece_height + row_idx, len(image))
    col_end_idx = min(piece_width + col_idx, len(image[0]))
    for row in range(row_idx, row_end_idx):  # bounds the section the piece should go on
        for col in range(col_idx, col_end_idx):
            # the matching piece's pixel, subtracting the upper_left factor:
            piece_pixel = piece[row-row_idx][col-col_idx]
            image[row][col] = piece_pixel


def average(image):
    """
    :param image: a list of image1-height size, when each item is a int list of image1-width
    size of pixels:(r,g,b) int tuples
    :return: tuple, the average color of the image's pixels divided by (red, green, blue)
    """
    red_sum, green_sum, blue_sum = 0, 0, 0
    pixels = 0
    for row in range(len(image)):
        for col in range(len(image[0])):
            r, g, b = image[row][col]
            red_sum += r
            green_sum += g
            blue_sum += b
            pixels += 1
    return red_sum/pixels, green_sum/pixels, blue_sum/pixels  # def of average


def preprocess_tiles(tiles):
    """
    :param tiles: list of images (of image format)
    :return: a list of tuples where the i'th item of list ia the average values of the i'th tile
    """
    averages_of_tiles = []
    for tile in tiles:
        average_tile = average(tile)
        averages_of_tiles.append(average_tile)
    return averages_of_tiles


def get_best_tiles(objective, tiles, averages, num_candidates):
    """
    :param objective: the destination image (of image format)
    :param tiles: list of images (of image format)
    :param averages: a list of the tile's averages: tuples (red_val, green_val, blue_val)
    :param num_candidates: int, num of tiles that are closer to objective
    :return: a num_candidate sized list of tiles whom average values are closest to the objective's
    """
    best_tiles = []
    distances = []
    distances_to_modify = []
    obj_avr = average(objective)
    for tile_avr in averages:
        distance = compare_pixel(obj_avr, tile_avr)  # avr dis. computed same way as comparing pixels
        distances.append(distance)
        distances_to_modify.append(distance)  # creating deep copy
    for tile_choose in range(num_candidates):
        min_dis_val = min(distances_to_modify)
        min_dis_idx = distances.index(min_dis_val)
        min_tile = tiles[min_dis_idx]
        best_tiles.append(min_tile)
        distances_to_modify.remove(min_dis_val)
    return best_tiles


def choose_tile(piece, tiles):
    """
    :param piece: an image(of image format), a segment of the original image
    :param tiles: list of images (of image format), all sized as piece
    :return: the tile of the shortest distance to piece
    """
    comparing = []
    for tile in tiles:
        compare_val = compare(piece, tile)
        comparing.append(compare_val)
    min_compare_val = min(comparing)
    min_compare_idx = comparing.index(min_compare_val)
    return tiles[min_compare_idx]


def make_mosaic(image, tiles, num_candidates):
    """
    :param image: a list of image1-height size, when each item is a int list of image1-width
    size of pixels:(r,g,b) int tuples
    :param tiles: list of images (of image format)
    :param num_candidates: int, num of tiles that are closer to objective
    :return: a mosaic of image made from tiles items
    """

    objective = deepcopy(image)
    img_height, img_width = len(image), len(image[0])
    tile_height, tile_width = len(tiles[0]), len(tiles[0][0])
    row_start, col_start = 0, 0
    avr_lst = preprocess_tiles(tiles)
    while (row_start, col_start) != (img_height, img_width):
        # getting the piece we want to replace
        img_segment = get_piece(objective, (row_start, col_start), (tile_height, tile_width))
        # "diagnose" the piece and find the best tile to replace it
        best_tiles = get_best_tiles(img_segment, tiles, avr_lst, num_candidates)
        best_tile = choose_tile(img_segment, best_tiles)
        # place the tile in piece's place
        set_piece(objective, (row_start, col_start), best_tile)
        # change index
        row_end = min(tile_height + row_start, img_height)
        col_end = min(tile_width + col_start, img_width)
        if col_end != img_width:
            col_start = col_end
        elif (col_end == img_width) & (row_end != img_height):
            row_start = row_end
            col_start = 0
        else:
            row_start, col_start = img_height, img_width
    return objective


if __name__ == '__main__':
    if len(sys.argv) == NUM_ARGS + 1:
        image_source = sys.argv[1]
        images_dir = sys.argv[2]
        output_name = sys.argv[3]
        tile_height = int(sys.argv[4])
        num_candidates = int(sys.argv[5])
        lst_image = load_image(image_source)
        tiles = build_tile_base(images_dir, tile_height)
        mosaic_image = make_mosaic(lst_image, tiles, num_candidates)
        save(mosaic_image, output_name)
    else:
        print("Wrong number of parameters. The correct usage is:\nex6.py"
              " <image_source> <images_dir> <output_name> <tile_height>"
              " <num_candidates>")
