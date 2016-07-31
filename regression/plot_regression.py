from pylab import show, text, imshow, plot
import matplotlib.pyplot as plt
import time

from minimize import *

# Average hourly wage
HOURLY_WAGE = [2.98, 3.09, 3.23, 3.33, 3.46, 3.6, 3.73, 2.91, 4.25, 4.47, 5.04, 5.47, 5.76]
# Number of homicides per 100,000 people
MURDERS = [8.6, 8.9, 8.52, 8.89, 13.07, 14.57, 21.36, 28.03, 31.49, 37.39, 46.26, 47.24, 52.33]

def Cost(B, X=HOURLY_WAGE, Y=MURDERS):
    cost = 0.0
    for i in xrange(0, len(X)):
        cost += (B[0] + B[1] * X[i] - Y[i]) ** 2
    return cost

b1 = np.arange(-60, -14, 1)
b2 = np.arange(5, 26, 1)
C = np.matrix([[0 for j in range(len(b2))] for i in range(len(b1))])

for i in range(len(b1)):
    for j in range(len(b2)):
        C[i, j] = Cost([b1[i], b2[j]])

def heatmap(X, Y, f, trace=None): # trace is a list of [b1, b2] pairs
    imshow(C,
        origin='lower',
        extent=[min(b1), max(b1), min(b2), max(b2)],
        vmax=abs(C).max(), vmin=-abs(C).max()
        )

B0 = [0, 0]
random.seed(int(round(time.time() * 1000)))
B0[0] = random.randrange(-60, -14)
B0[1] = random.randrange(5, 26)

LEARNING_RATE = [80, 40]
h = 0.00001
PRECISION = 0.00000000000001

begin = time.time()
(m,steps,trace) = minimize(Cost, B0, LEARNING_RATE, h, PRECISION)
end = time.time()

heatmap(HOURLY_WAGE, MURDERS, Cost, trace)
plt.title("Trace in heat map")
plt.text(-59.5, 23.5, "Steps: %i" %steps)
for i in range(len(trace)):
    if i == 0:
        plt.plot(trace[i][0], trace[i][1], "ko", markersize=6, color='red')
        plt.text(trace[i][0] - 1.3, trace[i][1] + 0.7, "Start")
    elif i == len(trace) - 1:
        plt.plot(trace[i][0], trace[i][1], "ko", markersize=6, color='red')
        plt.text(trace[i][0] - 1, trace[i][1] + 0.7, "Stop")
    else:
        plt.plot(trace[i][0], trace[i][1], "ko", markersize=2)
show()