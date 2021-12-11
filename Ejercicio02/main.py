from PIL import Image
import numpy as np
import image_edite as imed

def seeDetails(img):
    print(f'{img.format}, {img.size}, {img.mode}')

def get_chanels(img_arr):
    r,g,b = imed.get_chanels(img_arr)
    img_r = Image.fromarray(r)
    img_g = Image.fromarray(g)
    img_b = Image.fromarray(b)
    img_r.show()
    img_g.show()
    img_b.show()

def negative(img_arr):
    neg = imed.negative(img_arr)
    Image.fromarray(neg).show()

def sumImgs(img_arr0, img_arr1):
    mat = imed.sumImgs(img_arr0, img_arr1)
    Image.fromarray(mat).show()

def operadorAnd(img_arr0, img_arr1):
    mat = imed.operadorAnd(img_arr0, img_arr1)
    Image.fromarray(mat).show()

if __name__ == '__main__':
    img0 = Image.open('img/Quetzal-2.jpg')
    img_arr0 = np.array(img0)
    img1 = Image.open('img/orilla_mar.jpg')
    img_arr1 = np.array(img1)
    operadorAnd(img_arr0, img_arr1)
    img0.show()
    img1.show()