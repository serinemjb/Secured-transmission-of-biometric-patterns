import numpy as np
from PIL import Image
import cv2 as cv

def image_to_2d_vector(image_path, type):
    # Load the image
    if type==1:
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img_array = np.array(img)
    if type==2:
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img_array = np.array(img)
        _, img_array = cv.threshold(img_array, 127, 1, cv.THRESH_BINARY)

    return img_array

def save_to_h_file(array, output_file, image_name, type):
    # Get the dimensions of the array
    rows, cols = array.shape

    if type==1:
        # Open the output file
        with open(output_file, 'w') as f:
            # Write the array dimensions
            f.write('#include <stdint.h>\n')
            f.write(f'#define IMAGE_WIDTH_{image_name} {cols}\n')
            f.write(f'#define IMAGE_HEIGHT_{image_name} {rows}\n')
            f.write(f'uint8_t {image_name}[IMAGE_HEIGHT_{image_name}][IMAGE_WIDTH_{image_name}] =' + '{\n')

            # Write the array data
            for row in array:
                f.write('    {')
                f.write(', '.join(map(str, row)))
                f.write('},\n')

            f.write('};\n')
    if type==2:
        # Open the output file
        with open(output_file, 'w') as f:
            # Write the array dimensions
            f.write('#include <stdint.h>\n')
            f.write(f'#define IMAGE_WIDTH_{image_name} {cols}\n')
            f.write(f'#define IMAGE_HEIGHT_{image_name} {rows}\n')
            f.write(f'int {image_name}[IMAGE_HEIGHT_{image_name}][IMAGE_WIDTH_{image_name}] =' + '{\n')

            # Write the array data
            for row in array:
                f.write('    {')
                f.write(', '.join(map(str, row)))
                f.write('},\n')

            f.write('};\n')

def main():
    image_path = input("What's the path to your image? ") # Replace with your image path
    output_file = input("What the output file's name? ")  # Output .h file
    image_name = input("What's the name of your variable? ")
    type = int(input("Type 1 if the image is in grayscale and 2 if it's in binary. "))

    img_array = image_to_2d_vector(image_path, type)
    save_to_h_file(img_array, output_file, image_name, type)

if __name__ == '__main__':
    main()
