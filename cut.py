from PIL import Image

def cut_pic(name, l, u, r, b):
    crop = l, u, r, b
    im = Image.open(name)
    im = im.crop(crop)
    im.save(f'cut_{name}')