import cv2
import numpy as np
import os

# Wczytanie obrazu

sciezka = os.getcwd()

image = cv2.imread(sciezka + "//img.png")

dx = 1920
dy = 1080

# Inicjalizacja detektora ArUco
arucoParams = cv2.aruco.DetectorParameters()
arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50)

# Detekcja markerów ArUco
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

# Przygotowanie listy narożników
rogi = [corner for marker in corners for corner in marker[0]]
rogi = np.array(rogi)

# Przypisanie narożników do zmiennych
ld = rogi[0]
pd = rogi[1]
pg = rogi[2]
lg = rogi[3]

print(rogi)

# Parametry do rysowania punktów
color = (0, 255, 0)  # Zielony
radius = 5
thickness = -1  # Wypełniony okrąg

# Rysowanie punktów na obrazie
cv2.circle(image, (int(ld[0]), int(ld[1])), radius, color, thickness)
cv2.circle(image, (int(pd[0]), int(pd[1])), radius, color, thickness)
cv2.circle(image, (int(pg[0]), int(pg[1])), radius, color, thickness)
cv2.circle(image, (int(lg[0]), int(lg[1])), radius, color, thickness)


# Wyświetlenie obrazu z narożnikami
cv2.imshow('ob', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
