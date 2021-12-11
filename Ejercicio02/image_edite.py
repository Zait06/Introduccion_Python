import numpy as np

def get_chanels(img_arr):
    red = img_arr * np.array([1, 0, 0], dtype=np.uint8)
    green = img_arr * np.array([0, 1, 0], dtype=np.uint8)
    blue = img_arr * np.array([0, 0, 1], dtype=np.uint8)
    return red, green, blue

def negative(img_arr):
    return 255 - img_arr

def sumImgs(matA, matB):
    rA, cA, _ = matA.shape
    rB, cB, _ = matB.shape

    rows = 0    # Filas padre
    cols = 0    # Columnas padre

    if rA > rB:
        rows = rB
    else:
        rows = rA

    if cA > cB:
        cols = cB
    else:
        cols = cA

    # Finicio:Ffin , Cinicio:Cfin
    return matA[0:rows, 0:cols] + matB[:rows, :cols]

def operadorAnd(matA, matB):
    rA, cA, _ = matA.shape
    rB, cB, _ = matB.shape

    rows = 0    # Filas padre
    cols = 0    # Columnas padre

    if rA > rB:
        rows = rB
    else:
        rows = rA

    if cA > cB:
        cols = cB
    else:
        cols = cA

    return np.bitwise_and(matA[0:rows, 0:cols], matB[:rows, :cols])