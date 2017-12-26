#!/usr/bin/env python

from PIL import Image

__version__ = "1.0.1"
__author__ = "Shaunak Raha"
__maintainer__ = "Shaunak Raha"
__status__ = "Development"
__email__ = "shaunakraha@gmail.com"


def decode_image(img_file, passkey, version=1):
    read_text = ""
    if version == 1:
        #TODO Incorporate passkey usage in decrypt
        im = Image.open(img_file)
        pix = im.load()
        x = 0
        y = 0
        x_max = im.size[0]
        y_max = im.size[1]
        for y in range(0, y_max):
            for x in range(0, x_max):
                col = im.getpixel((x, y))
                if col[0] == 0:
                    col = (64, col[1], col[2])
                if col[1] == 0:
                    col = (col[0], 64, col[2])
                if col[2] == 0:
                    col = (col[0], col[1], 64)
                read_text = read_text + chr(col[0]/2) + chr(col[1]/2) + chr(col[2]/2)
    return read_text
