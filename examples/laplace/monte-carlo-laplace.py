'''
This is first implemention of laplace equation by monte carlo algorithm.

Equation:

	PDE: laplace(u) = 0, with 0<r<3 and 0<theta<2*pi
	Bound condition: u(1,theta) = 4, u(3,theta) = 6

Question:
	what's the value u of position: X_POSITION, Y_POSITION

Monte Carlo method:

	discretization of lapalce equation:

	u_i,j = (u_i-1,j + u_i+1,j + u_i,j-1 + u_i.j+1) / 4 

	from a start point 0, it will randomly walk to either of four position near 
	it with same probility, we note this point m, thus u_0 = u_m, then from point
	m, random walk will go to another point n, with u_0 = u_m = u_n ... until the 
	bounder u = 4 or u = 6, thus u_0 = 4 or 6, with N times random walk like
	this, u_0 = averge(sum of N times u_0). The more times random walk, the preciser 
	the solution will be.

Exact Solution for validation:

	The exact solution of this problem is u(r) = 4 + 2log(r)/log3.

	Thus in position (x = 2.0,y = 0.0), u = 4 + 2log(2)/log3 ~ = 5.261. 

'''
import random as rd
import math as mt

NUM_SAMPLING = 1000	#total simulation number
STEP  = 0.1 	#random walk step length
K = 60 	#fix iteration number for each time random walk, thus in fixed number, the random walk maybe cannot reach the bound
X_POSITION = 2.0 # x coordonne
Y_POSITION = 0.0 # y coordonne
VAL_LOW = 4 # low bound val
VAL_UP = 6 # up bound val
LOW = 1.0 #low bound
UP = 3.0 #up bound

def laplace():
	SUM = 0.0
	count = 0
	for _ in range(NUM_SAMPLING):
		x = X_POSITION
		y = Y_POSITION
		for _ in range(K):
			a = 2*rd.randint(0,1) - 1 
			b = 2*rd.randint(0,1) - 1 # a,b get random direction for next step of transition
			x = x + STEP*a 
			y = y + STEP*b # next step position
			r = mt.sqrt(x**2+y**2) # rayon 
			if r <= LOW: # reach the low bound
				count = count + 1
				SUM = SUM + VAL_LOW
				break
			if r >= UP: # reach the high bound
				count = count + 1
				SUM = SUM + VAL_UP
				break  					
	val = SUM/count #resolution

	print 'After',NUM_SAMPLING, 'examples, the value in point x=', X_POSITION,' y=', Y_POSITION, 'is', val, 'the exact resolution is 5.261.'

if __name__ == "__main__":
	laplace()
