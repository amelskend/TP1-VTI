import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread("images/image2.jpg")  # Charger l'image en BGR

if image is None:
    print("Erreur")
    exit()

image_RGB = cv.cvtColor(image, cv.COLOR_BGR2RGB) # Conversion de BGR vers RGB

h, l, c= image_RGB.shape # Recuperer les dimensions
image_CMY = np.zeros_like(image_RGB, dtype=np.uint8) # Creer une image vide

# Conversion RGB vers CMY
for x in range(h):
    for y in range(l):
        pixel = image_RGB[x, y] / 255  
        image_CMY[x, y] = [(1 - pixel[0]) * 255, (1 - pixel[1]) * 255, (1 - pixel[2]) * 255]

# Affichage des deux images
plt.figure(figsize=(10, 5))

# Image originale (RGB)
plt.subplot(1, 2, 1)
plt.imshow(image_RGB)
plt.title("Image originale (en RGB)")
plt.axis("off")

# Image convertie (CMY)
plt.subplot(1, 2, 2)
plt.imshow(image_CMY)
plt.title("Image convertie (en CMY)")
plt.axis("off")

plt.show()