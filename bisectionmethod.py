import math as m
def Bisection(f, bracket, abs_tol):
    xL, xU = bracket
    iters = m.cell(m.log((xU - xL)/abs_tol)/m.log(2) - 1)
    fxL = f(xL)
    fxu = f(xU)
    for i in range(iters):
        xR = (xL + xU)/2
        fxR= f(xR)
        if fxr == 0:
            break
        elif fxR*fxL < 0:
            xU = xR
            fxU = fxR
        else:
            xL = xR
            fxL = fxR
    return(xL + xU)/2