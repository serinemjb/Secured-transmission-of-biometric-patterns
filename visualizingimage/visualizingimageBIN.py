import numpy as np 
import matplotlib.pyplot as plt 
import cv2 as cv
import ast



with open('watermark_LSB_C2.txt', 'r') as image:
    content = image.read()

watermarked = ast.literal_eval(content)
watermarked = np.array(watermarked)

for i in range(watermarked.shape[0]):
    for j in range(watermarked.shape[1]):
        if watermarked[i][j] == 1:
            watermarked[i][j] = 255

plt.figure()
plt.imshow(watermarked, cmap='gray')
plt.show

save_path = "watermark_LSB_C2.png"
watermarked = np.uint8(watermarked)  # Ensure 'watermarked' array is of type np.uint8
try:
    if cv.imwrite(save_path, watermarked):
        print(f"Image successfully saved at: {save_path}")
    else:
        print(f"Failed to save image at: {save_path}")
except Exception as e:
    print(f"Error saving image: {e}")