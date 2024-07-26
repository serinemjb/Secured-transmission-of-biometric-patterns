import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt 
from PIL import Image 
from Watermarking_LSB import loadImage, watermarkProcessing


def recoverLSB(watermarked, size, n_LSB):
    watermarkBack = np.zeros(size)

    match n_LSB:
        case 1:
            for i in range(size[0]):
                for j in range(size[1]):
                    watermarkBack[i][j] = int(bin(watermarked[i][j])[-1])

        case 2:
            for i in range(size[0]):
                for j in range(size[1]):
                    try:
                        watermarkBack[i][j] = int(bin(watermarked[i][j])[-2])
                    except ValueError:
                        watermarkBack[i][j] = 0

        case 3:
            for i in range(size[0]):
                for j in range(size[1]):
                    watermarkBack[i][j] = int(bin(watermarked[i][j])[-3])

        case 4:
            for i in range(size[0]):
                for j in range(size[1]):
                    watermarkBack[i][j] = int(bin(watermarked[i][j])[-4])

    return watermarkBack


def main():
    watermarked_path = "watermarked_LSB2.png"
    watermark_path = "ID.png"
    fingerprint_path = "Finger.bmp"
    watermarked = loadImage(watermarked_path)
    watermark = loadImage(watermark_path)
    watermark = watermarkProcessing(watermark)
    fingerprint = loadImage(fingerprint_path)
    size = watermarked.shape
    #print(size)
    n_LSB = 2
    print(len(bin(watermarked[50][50])))

    watermarkBack = recoverLSB(watermarked, size, n_LSB)


    #print(watermarkBack[50][50])

    plt.figure()
    plt.imshow(watermarkBack, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()