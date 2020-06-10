import math
import numpy as np
import matplotlib.pyplot as plt
from math import ceil, floor

g = -9.81
m = 0
c = 0
tf = 0
vt = 0
r =0
def floatRound(num, places): #rounds a number to a given decimal place
    index = str(num).find('.')
    x = str(num)[int(index)+1:]
    if (len(x)>=places+1):
        y = x[places: places + 1]
        if (int(y)>=5):
            n = ceil(num * (10**places)) / float(10**places)
        else:
            n = floor(num * (10**places)) / float(10**places)
    else:
        n = num
    return n

def getVerticalV(V, theta):
    Vy = floatRound(math.sin(math.radians(theta)),2) * V
    return (Vy)

def getHorizontalV(v, theta):
    Vx = floatRound(math.cos(math.radians(theta)),2)* v
    print(Vx)
    return (Vx)


#values without air drag
def getTime(v, theta, a, h):
    top = (-v)-math.sqrt((v*v)-(4*(0.5*a)*h))
    bottom = 2* (0.5 *a)
    time = top/bottom
    return (time)

def displacement(v, h, a, t):
    d = h + (v*t) +((0.5*a)*(t*t))
    return (d)

def maxHeight(v, g, h):
    top = (v*v)
    bottom = 2*(-g)
    h = h + (top/bottom)
    return (h)

#values with with Air drag
def getTimeAD(vt, vi, g):
    if (vi<vt):
        t = (2 * vi)/-g
    elif (vi> vt):
        t = (vi)/-g
    else:
        t = (3 * vi)/(2 * -g)
    return (t)

def verticalDis(vt, vi, t, h):
    a = (vt)/-g
    b = vi + vt
    e = 1 - np.exp((g*t)/(vt))
    const = h
    dis = (a * b * e) - (vt * t) + const
    return dis

def horizontalDis(vt, vi, t):
    a = ((vt *vi)/-g)
    b = 1 - np.exp((g*t)/vt)
    dis = a * b
    return dis

#user input
print ("Please enter only numeric values greater than 0")
h = -1
while (h<0):
    h = float(input("What is the initial height in meters? ")) #initial height
Vi = -1
while (Vi<0):
    Vi = float(input("What is the initial velocity in meters per second? ")) #iniial velocity
ad = "c"
while (ad!= "y" and ad!= "n"):
        ad= str(input("Is there air drag? (y or n) ")).strip()
if (ad == "y"):
    c=-1
    while(c<0):
        c = float(input("What is the drag coefficient? "))
    m = -1
    while (m < 0):
        m = float(input("What is the mass of the projectile? "))
    vt = (m * -g) / c  # terminal velocity
thetai = float(input("What is the initial angle in degrees? ")) #initial angle
increm = 50

Vyi = getVerticalV(Vi,thetai)
Vx=getHorizontalV(Vi, thetai)



if (ad == "n"):
    tf = (getTime(Vyi, thetai, g, h))
    maxH = maxHeight(Vyi, g, h)
    print("Max Height: " + str(maxH))
    dxf = tf * Vx
elif (ad == "y"):
    tf = getTimeAD(vt, Vyi, g)
    r = horizontalDis(vt, Vx, tf)


print ("Total time: " + str(tf))
print("Range: " + str(r))
change = (tf)/increm
time = 0
tIncrem = []
tIncrem.append(time)

#3D t vs x vs y graph
fig = plt.figure()
ax = plt.axes(projection='3d')
xline = np.linspace(0, tf, increm) #time
print (xline)
if (ad == "y"):
    tempt = tf
    while (verticalDis(vt, Vyi, tempt, h)>0):
        tempt = tempt + (tf*0.01)
    xline = np.linspace(0, tempt, increm)
    yline = horizontalDis(vt, Vx, xline)
    zline = verticalDis(vt, Vyi, xline, h)  # vertical distance
else:
    yline = Vx * xline  # horizontal distance
    zline = displacement(Vyi, h, g, xline) #vertical distance
print (zline)
ax.set_xlabel('Time (sec)')
ax.set_ylabel('Horizontal distance (m)')
ax.set_zlabel('Vertical distance (m)')
ax.plot3D(xline, yline, zline, 'gray')
plt.show()

