
from numba import njit

@njit
def radiusXY(p):
    x, y = p[:2]
    return (x**2 + y**2)**0.5

@njit
def radiusXYZ(p):
    x, y = p[:3]
    return (x**2 + y**2 + z**2)**0.5

@njit
def cuboidOr(p,s):
    x, y, z = p
    w, l, h = s
    d = (min(w-x, w+x, 0)**2 + min(l-y, l+y, 0)**2 + min(h-z, h+z, 0)**2)**0.5
    d += max(min(abs(x),w)-w, min(abs(y),l)-l, min(abs(z),h)-h)
    return d

@njit
def rSphere(p):
    x, y, z = p
    if 0 > x*y+x*z+y*z:
        return 0
    return (x+y+z)/2+((x*y+x*z+y*z)/4)**0.5


@njit
def cuboidIr(p,s,ket=100,m=(0,1,1,1),pp=(0,0,0,0)):
    x, y, z = p
    w, l, h = s
    k = ket
    cm, xm, ym, zm = m
    pc, px, py, pz = pp
    xd = min(w-x, w+x)
    yd = min(l-y, l+y)
    zd = min(h-z, h+z)

    if xd < 0 or yd < 0 or zd < 0:
        return 0

    cd = (pc*xd*yd*zd + xd**0.5 + yd**0.5 + zd**0.5)**2
    edx = (px*zd*yd + zd**0.5 + yd**0.5)**2
    edy = (py*xd*zd + xd**0.5 + zd**0.5)**2
    edz = (pz*yd*xd + xd**0.5 + yd**0.5)**2

    d = 1/(xm/(1+k*edx) + ym/(1+k*edy) + zm/(1+k*edz) + cm/(1+k*cd))/k

    return d

