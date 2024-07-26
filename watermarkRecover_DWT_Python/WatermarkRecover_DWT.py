import pywt
import numpy as np
import cv2 as cv
from Watermarking_LSB import loadImage, watermarkProcessing
import matplotlib.pyplot as plt


def recoverDWT(watermarked, original, scale=2):
    coeffs2_watermarked = pywt.dwt2(watermarked, 'haar')
    LL_w, (LH_w, HL_w, HH_w) = coeffs2_watermarked

    coeffs2_original = pywt.dwt2(original, 'haar')
    LL_o, (LH_o, HL_o, HH_o) = coeffs2_original

    extracted_watermark = (LH_w - LH_o) / scale

    return extracted_watermark



def main():
    watermarked_path = r"C:\Users\DELL\Documents\Séminaire\DWT\watermarked_DWT.png"
    original_path = r"C:\Users\DELL\Documents\Séminaire\DWT\Finger.bmp"
    watermarked = loadImage(watermarked_path)
    original = loadImage(original_path)
    print(watermarked[50][50])
    watermarkBack = recoverDWT(watermarked, original)
    _, watermarkBack = cv.threshold(watermarkBack, 0, 1, cv.THRESH_BINARY)



    #print(watermarkBack[50][50])

    plt.figure()
    plt.imshow(watermarkBack, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()