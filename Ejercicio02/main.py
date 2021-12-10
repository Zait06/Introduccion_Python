from PIL import Image
import numpy as np
import image_edite as imed

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

if __name__ == '__main__':
    img = Image.open('img/Quetzal-2.jpg')
    print(f'{img.format}, {img.size}, {img.mode}')
    # img.show()
    img_arr = np.array(img)
    # get_chanels(img_arr)
    negative(img_arr)
    img.show()