import math
from vpython import *
import numpy as np


def E(x, z, b, t):
    mi0 = np.power(4 * np.pi, -7)
    m0 = np.pi * 1 * b**2
    omega = 3 * np.power(10, 8)
    c = 300 * np.power(10, 6)

    E = (mi0*m0*(omega**2))/(4*np.pi*(c**2)) * (x/(x**2 + z**2)) * np.cos(omega*(t - np.sqrt(x**2 + z**2)/c))
    return E * 10**9


ring(pos=vector(0,0,0), axis=vector(0,1,0))

coords = []

for w in range(-4, 5):
    for h in range(-4, 5):
        if(w == 0 or h ==0): continue
        coords.append([w, h])



arrowsE = []
arrowsB = []
b = 1

def createEArrow(x, z):
    pos = vector(-x, z, 0)
    ar = arrow(pos=pos, axis=vector(0,0,E(x, z, b, 0)), color=color.yellow, shaftwidth=0.1)
    return ar

def createBArrow(x, z):
    pos = vector(-x, z, 0)
    r = np.sqrt(x**2 + z**2)

    Bx = (z/r)*-E(x,z,b,0)
    Bz = (x/r)*-E(x,z,b,0) 

    ar = arrow(pos=pos, axis=vector(Bx,Bz,0), color=color.red, shaftwidth=0.1)
    return ar


for e in coords:
    arrowsE.append(createEArrow(*e))
    arrowsB.append(createBArrow(*e))


def updateEArrow(arrow, pos, t):
    arrow.axis.z = E(pos[0], pos[1], b, t)

def updateBArrow(arrow, pos, t):

    x, z = pos
    
    r = np.sqrt(x**2 + z**2)

    Bx = (z/r)*-E(x,z,b,t)
    Bz = (x/r)*-E(x,z,b,t) 

    arrow.axis.x = Bx
    arrow.axis.y = Bz


t = 0

while(True):
    rate(2)

    for i in range(len(coords)):
        updateEArrow(arrowsE[i], coords[i], t)
        updateBArrow(arrowsB[i], coords[i], t)

    t = t + 1
