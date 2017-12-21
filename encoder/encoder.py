#!/usr/bin/env python

from PIL import Image

__version__ = "1.0.1"
__author__ = "Shaunak Raha"
__maintainer__ = "Shaunak Raha"
__status__ = "Development"
__email__ = "shaunakraha@gmail.com"


def encode_image(text, version=1, outfile="output.png", img_width=720):
    passkey = "000000"
    if version == 1:
        #TODO: Create Passkey
        img_height = ((1 + (len(text) / 3)) / img_width) + 1
        im = Image.new('RGB', (img_width, img_height))
        i = 0
        col0 = 0
        col1 = 0
        col2 = 0
        for letter in text:
            val = 2 * ord(letter)
            y = 0
            x = i / 3
            if i % 3 == 0:
                col0 = val
            if i % 3 == 1:
                col1 = val
            if i % 3 == 2:
                col2 = val
                while x > (img_width - 1):
                    x = x - img_width
                    y = y + 1
                im.putpixel((x, y), (col0, col1, col2))
            i = i + 1
        im.save(outfile)
    return passkey
