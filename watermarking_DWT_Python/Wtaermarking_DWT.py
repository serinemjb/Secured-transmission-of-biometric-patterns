import pywt
import numpy as np
import cv2 as cv
from Watermarking_LSB import loadImage, watermarkProcessing
import matplotlib.pyplot as plt


def watermarking_DWT(image, watermark, scale=2):
    # Perform DWT on the original image
    coeffs2 = pywt.dwt2(image, 'haar')
    LL, (LH, HL, HH) = coeffs2

    # Resize the watermark to match the size of the sub-band
    watermark = cv.resize(watermark, (LH.shape[1], LH.shape[0]))

    # Embed the watermark in the LH sub-band
    alpha = scale  # Scaling factor for embedding
    LH_watermarked = LH + alpha * watermark

    # Perform the inverse DWT to get the watermarked image
    watermarked_coeffs = LL, (LH_watermarked, HL, HH)
    watermarked = pywt.idwt2(watermarked_coeffs, 'haar')

    return watermarked, scale

def main():
    fingerprint_path = r"C:\Users\DELL\Documents\Séminaire\DWT\Finger.bmp"
    watermark_path = r"C:\Users\DELL\Documents\Séminaire\DWT\ID.png"

    # Load fingerprint and watermark images
    try:
        fingerprint = loadImage(fingerprint_path)
        watermark = loadImage(watermark_path)
    except FileNotFoundError as e:
        print(e)
        return

    watermark = watermarkProcessing(watermark)

    watermarked, scale = watermarking_DWT(fingerprint, watermark)

    print(watermarked[50][50])

    print(f"Watermarked image shape: {watermarked.shape}")

    # Display the watermarked image
    plt.figure()
    plt.imshow(watermarked, cmap='gray')
    plt.title('Watermarked Image')
    plt.show()

    save_path = r"C:\Users\DELL\Desktop\watermarked_DWT.png"
    #watermarked = np.uint8(watermarked)  # Ensure 'watermarked' array is of type np.uint8
    try:
        if cv.imwrite(save_path, watermarked):
            print(f"Image successfully saved at: {save_path}")
        else:
            print(f"Failed to save image at: {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")


if __name__ == "__main__":
    main()
