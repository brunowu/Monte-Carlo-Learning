'''
Metropolis-Hastings algorithm to sample from Cauchy distribution (Markov Chain Monte Carlo Method)
'''

import random
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import math as mt

def cauchy(theta):
    y = 1.0 / (mt.pi*(1.0 + theta ** 2))
    return y

T = 5000
sigma = 1
thetamin = -30
thetamax = 30
theta = [0.0] * (T+1)
theta[0] = random.uniform(thetamin, thetamax)
t = 0
while t < T:
    t = t + 1
    theta_star = norm.rvs(loc=theta[t - 1], scale=sigma, size=1, random_state=None)
    #print theta_star
    alpha = min(1, (cauchy(theta_star[0]) / cauchy(theta[t - 1])))

    u = random.uniform(0, 1)
    if u <= alpha:
        theta[t] = theta_star[0]
    else:
        theta[t] = theta[t - 1]

ax1 = plt.subplot(211)
ax2 = plt.subplot(212) 
plt.sca(ax1)
plt.ylim(thetamin, thetamax)
plt.title("Sampling values")
plt.plot(range(T+1), theta, 'g-')
plt.sca(ax2)
num_bins = 100
plt.hist(theta, num_bins, normed=1, facecolor='red', alpha=0.5)
x = np.arange(-30.0, 30.0, 0.1)
plt.plot(x, 1.0 / (mt.pi*(1.0 + x ** 2)),c='b')
plt.title("Sampling distribution")
plt.show()