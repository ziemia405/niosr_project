import cv2
import numpy as np
import os

# Wczytanie obrazu

sciezka = os.getcwd()
nr_obrazka = 2

image = cv2.imread(sciezka + "//" + str(nr_obrazka) + ".png")

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
# print(pd[0])
# print(0.66*dx)
#
# print(pd[1])
# print(0.66*dy)

if pd[0] < 0.33*dx and pd[1] < 0.33*dy:
    print('lewa gora')
elif ld[0] > 0.33*dx and pg[0] < 0.66*dx and ld[1] < 0.33*dy:
    print('srodek gora')
elif ld[0] > 0.66*dx and ld[1] < 0.33*dy:
    print('prawa gora')
elif pd[1] < 0.66*dy and pg[1] > 0.33*dy and pg[0] < 0.33*dx:
    print('lewo srodek')
elif lg[0] > 0.33 * dx and lg[1] > 0.33 * dy and pd[0] < 0.66 * dx and pd[1] < 0.66*dy:
    print('srodek srodek')
elif pg[0] > 0.66*dx and pd[1] > 0.33*dy and pd[1] < 0.66*dy:
    print('prawo srodek')
elif lg[1] > 0.66*dy and lg[0] < 0.33*dx:
    print('lewo dol')
elif pd[0] > 0.33*dx and pd[0] < 0.66*dx and lg[1] > 0.66*dy:
    print('srodek dol')
elif pg[0] > 0.66*dx and lg[1] > 0.66*dy:
    print('prawo dol')


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
