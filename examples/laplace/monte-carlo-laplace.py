import random as rd
import math as mt

NUM_SAMPLING = 100000
STEP  = 0.1
K = 50
def main():
	SUM = 0.0
	count = 0
	for _ in range(NUM_SAMPLING):
		x = 2.0
		y = 0.0
		for _ in range(K):
			a = 2*rd.randint(0,1) - 1
			b = 2*rd.randint(0,1) - 1
			x = x + STEP*a
			y = y + STEP*b
			r = mt.sqrt(x**2+y**2)
			if r <= 1.0:
				count = count + 1
				SUM = SUM + 4
				break
			if r >= 3.0:
				count = count + 1
				SUM = SUM + 6
				break  
	print SUM					
	print SUM/count

if __name__ == "__main__":
	main()
