from numpy import sin, cos

def translatepoints(x,y,xt,yt):
    xr = x+xt
    yr = y+yt
    return xr,yr

def rotatepoints(x,y,theta):
    xr = cos(theta)*x - sin(theta)*y 
    yr = sin(theta)*x + cos(theta)*y 
    return xr,yr

def scalepoints(x,y,scale):
    xr = scale*x
    yr = scale*y
    return xr,yr

