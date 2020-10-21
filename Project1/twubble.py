# P-6 MCS 275 Mon 3 May 2010 : twubble.py

# By "twubble" we abbreviate the twubblesome circles problem.

# The data is taken from
# http://demonstrations.wolfram.com/TheTroublesomeTwelveCircleProblem/.
# The list circles are the radii of twelve circles.
# The initial centers of the circles are in the list centers.
# In table are the center and the radius of the table.
# The goal of the puzzle is to place all circles inside the disk defined
# by the table so that none of the circles overlap each other.

# This scripts shows the initial configuration of the circles.
# The circles is shown in green, the table is red.
# Observe the magnification factor s to scale the given data.

circles = [ 0.5943, 0.7290, 0.8365, 1.1315, 1.2576, 1.4497, 
            1.3067, 1.2151, 0.8788, 0.7941, 0.6383, 0.5495 ]

centers = [ ( -3.2208, -3.1614) , (-4.1287, -2.0767), (-4.7716, -0.5377),
            ( -4.733, 1.5501) , ( -3.6333, 3.7502) , (-1.2111, 5.2049),
            (1.6755, 5.0078), ( 3.7798, 3.4196), (4.6523, 1.3853),
            (4.6523, -0.3790), (4.1574, -1.8336), (3.3871, -2.8653) ]

table = [(0,0), 3.8149]

from Tkinter import *

# d is number of pixels on canvas, s is multiplication factor
(d,s) = (400,30)     # for small windows
# (d,s) = (500,37.5) # for medium windows
# (d,s) = (600,45) # for large windows
o = (d/2,d/2-s)      # origin on canvas
w = Tk()
w.title('the troublesome twelve circle problem')
c = Canvas(w,width=d,height=d,bg='white')
c.pack()
R = table[1]*s
c.create_oval(o[0]-R,o[1]-R,o[0]+R,o[1]+R,fill='red')
for i in range(0,12):
   r = s*circles[i]; p = centers[i]
   X = (o[0] + p[0]*s, o[1] + p[1]*s)
   c.create_oval(X[0]-r,X[1]-r,X[0]+r,X[1]+r,fill='green')
w.mainloop()
