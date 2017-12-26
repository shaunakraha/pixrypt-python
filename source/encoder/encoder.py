#!/usr/bin/env python

from PIL import Image
import random
import string

__version__ = "1.0.1"
__author__ = "Shaunak Raha"
__maintainer__ = "Shaunak Raha"
__status__ = "Development"
__email__ = "shaunakraha@gmail.com"


def generate_password(user_password=None, length=6):
    passkey = ""
    if "None" in str(type(user_password)):
        passkey = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                          for _ in range(length))
    return passkey


def encode_image(text, version=1, outfile="output.png", img_width=720):
    passkey = "000000"
    if version == 1:
        passkey = generate_password()
        text = str(len(passkey)).zfill(3) + passkey + text
        img_height = ((1 + (len(text) / 3)) / img_width) + 1
        if img_height == 1:
            img_width = 1 + (len(text) / 3)
        im = Image.new('RGB', (img_width, img_height))
        i = 0
        c0 = 0
        c1 = 0
        c2 = 0
        for letter in text:
            val = 2 * ord(letter)
            y = 0
            x = i / 3
            if i % 3 == 0:
                c0 = val
            if i % 3 == 1:
                c1 = val
            if i % 3 == 2:
                c2 = val
                while x > (img_width - 1):
                    x = x - img_width
                    y = y + 1
                im.putpixel((x, y), (c0, c1, c2))
            i = i + 1
        im.save(outfile)
    return passkey
