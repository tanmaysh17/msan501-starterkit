import numpy as np
import random

def minimize(f, B0, eta, h, precision):
    trace = []
    B = B0
    steps = 0
    trace.append(B0)

    while True:
        finite_diff = [f([B[0]+h, B[1]]) - f(B), f([B[0], B[1]+h]) - f(B)]
        Bnew = np.subtract(B, np.multiply(eta, finite_diff))
        steps += 1
        if steps % 10 == 0:
            trace.append(Bnew)
        delta = abs(f(Bnew) - f(B))
        if delta < precision: break
        B = Bnew
    return B, steps, trace
