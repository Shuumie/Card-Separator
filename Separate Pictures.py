from PIL import Image
import argparse

parser = argparse.ArgumentParser(
                    prog='Separate Pictures',
                    description='Separate image consisting of pictures in a grid into multiple pictures')

parser.add_argument("filename", help="Filename or path to file that should be separated")
parser.add_argument("--savePath", help="Filename prefix or path ending with filename prefix where to save the images to. The suffix added will be a numbering _0, _1, ... and the file extension type. If omited, result will not be saved")
parser.add_argument("-s", "--show", action="store_true", help="Set to view the images. Shows the images one at a time and waits for closing, before opening the next one")

def save_images(images, path_with_name):
    for index, image in enumerate(images):
        image.save(f"{path_with_name}_{index}.png")

def show_images(images):
    for cropped_image in images:
        cropped_image.show()

def crop_image(image, column_edges, row_edges):
    result = []
    for x_index in range(0, len(column_edges), 2):
        for y_index in range(0, len(row_edges), 2):
            img_crop = image.crop((column_edges[x_index] + 1, row_edges[y_index] + 1, column_edges[x_index + 1] - 1, row_edges[y_index + 1] - 1))
            result.append(img_crop)

    return result

def remove_intermediate_sorted_array_values(array):
    last_value = None
    result = []
    for array_value in array:
        if last_value != array_value - 1:
            if last_value != None and last_value not in result:
                result.append(last_value)
            result.append(array_value)
        last_value = array_value

    result.append(array[-1])
    return result

def find_columns_over_luminance_threshold(threshold, image_luminance_values):
    width, height = len(image_luminance_values), len(image_luminance_values[0])
    image_luminance_over_threshold = check_image_luminance_threshold(threshold, image_luminance_values)
    result = []
    for x in range(width):
        check_passed = True
        for y in range(height):
            check_passed &= image_luminance_over_threshold[x][y]
        if check_passed:
            result.append(x)
    return result

def find_rows_over_luminance_threshold(threshold, image_luminance_values):
    width, height = len(image_luminance_values), len(image_luminance_values[0])
    image_luminance_over_threshold = check_image_luminance_threshold(threshold, image_luminance_values)
    result = []
    for y in range(height):
        check_passed = True
        for x in range(width):
            check_passed &= image_luminance_over_threshold[x][y]
        if check_passed:
            result.append(y)
    return result

def check_image_luminance_threshold(threshold, image_luminance_values):
    width, height = len(image_luminance_values), len(image_luminance_values[0])
    result = [[0] * height for _ in range(width)]
    for x in range(width):
        for y in range(height):
            result[x][y] = check_luminance_threshold(threshold, image_luminance_values[x][y])

    return result

def check_luminance_threshold(threshold, pixel_luminocity):
    return pixel_luminocity >= threshold

def image_to_luminance(image):
    pixels = img.load()
    width, height = img.size
    result = [[0] * height for _ in range(width)]
    for x in range(width):
        for y in range(height):
            result[x][y] = pixel_to_luminance(pixels[x,y])
                
    return result
    

def pixel_to_luminance(pixel):
    red, green, blue = pixel
    return red * 0.2126 + green * 0.7152 + blue * 0.0722


args = parser.parse_args()

input_path = args.filename
save_path = args.savePath
show = args.show
img = Image.open(input_path)

image_luminance_values = image_to_luminance(img)
white_columns = find_columns_over_luminance_threshold(200, image_luminance_values)
white_rows = find_rows_over_luminance_threshold(200, image_luminance_values)
white_column_edges = remove_intermediate_sorted_array_values(white_columns)
white_row_edges = remove_intermediate_sorted_array_values(white_rows)


cropped_images = crop_image(img, white_column_edges[1:-1], white_row_edges[1:-1])

if show:
    show_images(cropped_images)

if save_path:
    save_images(cropped_images, save_path)