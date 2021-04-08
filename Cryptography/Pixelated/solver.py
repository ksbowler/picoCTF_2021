from PIL import Image, ImageDraw, ImageFilter
import numpy as np
im1 = np.array(Image.open('scrambled1.png'))
im2 = np.array(Image.open('scrambled2.png'))
print(im1.shape)
im1 = im1 + im2
print(type(im1))
im = Image.fromarray(im1)
im.save('sum.png')
