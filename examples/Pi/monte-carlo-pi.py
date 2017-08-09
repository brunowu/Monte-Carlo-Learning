# print("Hey JacquesSept!")
# print("Hello Bruno!")
# print("You can compute Pi here with monte carlo")
# print("OK")
print("Let's do it")

# ==================================================
# Start of the classical example with Monte Carlo

import random as rd


NUM_SAMPLING = 1000000


def main():
    counting = 0

    # two randoms [0, 1)
    for _ in range(NUM_SAMPLING):
        x = rd.random()
        y = rd.random()
        d = x**2 + y**2
        if d <= 1.0:
            counting += 1

    # area of circle / square = (pi * r^2 / 4) / r^2 = pi / 4
    # so pi = 4*counting/NUM_SAMPLING
    print 'After', NUM_SAMPLING, 'examples, the estimated value of PI is', 4.0*counting/NUM_SAMPLING


if __name__ == "__main__":
    main()









print("Let's do it")

