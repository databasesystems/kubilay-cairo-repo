import cairo
import math
import random
import itertools
import numpy as np

n = 52
x = 52
y = 52
WIDTH = x
HEIGHT = y
PIXEL_SCALE = 50

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             WIDTH*PIXEL_SCALE,
                             HEIGHT*PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

ctx.rectangle(0, 0, WIDTH, HEIGHT)
br = random.uniform(0, 1)
bg = random.uniform(0, 1)
bb = random.uniform(0, 1)
ctx.set_source_rgb(br, bg, bb)
ctx.fill()

# drawing code with loops
c1 = range(1,n,2)
c0 = list(itertools.chain.from_iterable(itertools.repeat(c1, n)))
print(c0)
d2 = np.array(range(1,n,2))
d0 = np.repeat(d2, n)
print('d0 is:',d0)

df = list(zip(c0,d0))
print(df)

for xc, yc in zip(c0, d0):
    r = random.uniform(0, 9)
    g = random.uniform(0, 19)
    b = random.uniform(0, 19)
    ctx.arc(xc, yc, 0.9, 0, 2*math.pi)
    ctx.close_path()
    ctx.set_source_rgb(r,g,b)
    #ctx.stroke()
    ctx.fill()

# End of drawing code
surface.write_to_png('/home/kubilay/repo/circles-1.png')