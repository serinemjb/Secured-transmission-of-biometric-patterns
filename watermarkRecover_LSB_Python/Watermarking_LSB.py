import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from PIL import Image

# Function that loads images
def loadImage(path):
    with Image.open(path) as img:
        image = np.array(img)
    return image

# Function used for binarization
def watermarkProcessing(watermark):
    watermark_gray = cv.cvtColor(watermark, cv.COLOR_RGB2GRAY)  # Convert to grayscale if needed
    _, watermarkP = cv.threshold(watermark_gray, 127, 1, cv.THRESH_BINARY)
    return watermarkP

# Watermarking function using the LSB method
def watermarking_LSB(image, watermark, n_LSB):
    watermarked = image.copy()  # Make a copy to avoid modifying the original image
    match n_LSB:
        case 1:
            for i in range(watermark.shape[0]):
                for j in range(watermark.shape[1]):
                    # Ensure we use integer values for bin operations
                    watermarked[i][j] = int((bin(image[i][j])[2:-1] + bin(int(watermark[i][j]))[2]), 2)
        case 2:
            for i in range(watermark.shape[0]):
                for j in range(watermark.shape[1]):
                    # Ensure we use integer values for bin operations
                    watermarked[i][j] = int((bin(image[i][j])[2:-2] + bin(int(watermark[i][j]))[2]) + bin(image[i][j])[-1], 2)
        case 3:
            for i in range(watermark.shape[0]):
                for j in range(watermark.shape[1]):
                    # Ensure we use integer values for bin operations
                    watermarked[i][j] = int((bin(image[i][j])[2:-3] + bin(int(watermark[i][j]))[2]) + bin(image[i][j])[8:], 2)
        case 4:
            for i in range(watermark.shape[0]):
                for j in range(watermark.shape[1]):
                    # Ensure we use integer values for bin operations
                    watermarked[i][j] = int((bin(image[i][j])[2:-4] + bin(int(watermark[i][j]))[2]) + bin(image[i][j])[7:], 2)

    return watermarked

def main():
    fingerprint_path = "Finger.bmp"
    watermark_path = "ID.png"
    n_LSB = 4

    fingerprint = loadImage(fingerprint_path)
    watermark = loadImage(watermark_path)
    watermark = watermarkProcessing(watermark)
    watermark = watermark.astype(np.uint8)  # Ensure watermark is of type uint8
    watermarked = watermarking_LSB(fingerprint, watermark, n_LSB)

    plt.figure()
    plt.imshow(watermarked, cmap='gray')
    plt.show()

    save_path = "watermarked_LSB4.png"
    watermarked = np.uint8(watermarked)  # Ensure 'watermarked' array is of type np.uint8
    try:
        if cv.imwrite(save_path, watermarked):
            print(f"Image successfully saved at: {save_path}")
        else:
            print(f"Failed to save image at: {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

if __name__ == "__main__":
    main()
