import random as rd
import math as mt

NUM_SAMPLING = 1000
STEP  = 0.10

def main():
	SUM  = 0.0
	x = 2.0
	y = 0.0
	for _ in range(NUM_SAMPLING):
             	a = 2*rd.randint(0,1) - 1
		b = 2*rd.randint(0,1) - 1
		x = x + STEP*a
		y = y + STEP*b
		r = mt.sqrt(x**2+y**2)
		if r <= 1.0:
			SUM = SUM + 4
		elif r >= 3.0:
			SUM = SUM + 6

	val = SUM/NUM_SAMPLING

	print SUM					
	print val

if __name__ == "__main__":
	main()
