import cairo
import math
import random
import itertools
import numpy as np

n = 700
x = 350
y = 350
WIDTH = x
HEIGHT = y
PIXEL_SCALE = 2

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
    #ctx.rectangle(xc, yc, 1, 1)
    #ctx.arc(2, 1, 0.5, 0, 2 * math.pi)

def box(xc,yc):
    ctx.set_source_rgb(0, 0, 0)
    ctx.rectangle(xc, yc, 1, 1)
    #ctx.arc(xc, yc, 0.5, 4, 2 * math.pi)

for xc,yc in df:
    mylist = [circle,box]
    ctx.move_to(xc, xc)
    #myfunc = mylist(xc,yc)
    np.random.choice(mylist,p=[0.4, 0.6])(xc,yc)
    if circle in mylist:
    #print(y)
    #circle(xc,yc)
        ctx.close_path()
        ctx.fill_preserve()
        ctx.fill()
    else:
        ctx.close_path()
        ctx.fill_preserve()
        ctx.fill()

 # ctx.stroke()
 # ctx.set_source_rgb(0.1, 0.1, 0.1)

# End of drawing code
surface.write_to_png('/home/kubilay/repo/abstract3.png')