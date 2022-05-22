# musings with cairo by Kubilay Tsil Kara, almost nfts :-)
import cairo
import math
import random
import itertools
import numpy as np

n = 450
x = 800
y = 800
WIDTH = x
HEIGHT = y
PIXEL_SCALE = 1

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                             WIDTH*PIXEL_SCALE,
                             HEIGHT*PIXEL_SCALE)
ctx = cairo.Context(surface)
ctx.scale(PIXEL_SCALE, PIXEL_SCALE)

ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.set_source_rgb(0, 0, 0)
ctx.fill()

# drawing code with loops
c1 = range(0,n,1)
c0 = list(itertools.chain.from_iterable(itertools.repeat(c1, n)))
print('c0 is:',c0)
d2 = np.array(range(0,n,1))
d0 = np.repeat(d2, n)
print('d0 is:',d0)

df = list(set(zip(d0,c0)))
print('df is: ',df)

def circle(xc,yc):
    ctx.set_source_rgb(1, 1, 1)
    ctx.arc(xc+0.5, yc+0.5,0.5, 0, 2 * math.pi)
  

def box(xc,yc):
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(xc, yc, 1, 1)
  

for xc,yc in df:
    mylist = [circle,box]
    ctx.move_to(xc, xc)
    np.random.choice(mylist,p=[0.4, 0.6])(xc,yc)
    if circle in mylist:
        ctx.close_path()
        ctx.fill_preserve()
        ctx.fill()
    else:
        ctx.close_path()
        ctx.fill_preserve()
        ctx.fill()

# End of drawing code
surface.write_to_png('/home/kubilay/repo/abstract3.png')