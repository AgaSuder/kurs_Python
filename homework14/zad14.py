import random
from numba import njit
import time
random.seed()

def monte_carlo_pi(n: int) -> float:
    p = 0.0
    k = 0;
    for j in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            k += 1
    p = 4 * k / n
    return p

@njit
def nb_monte_carlo_pi(n: int) -> float:
    p = 0.0
    k = 0;
    for j in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            k += 1
    p = 4 * k / n
    return p

starttime = time.time()
pi = monte_carlo_pi(10)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method with 10 input time: " + str(endtime-starttime))

starttime = time.time()
pi = monte_carlo_pi(100)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method with 100 input time: " + str(endtime-starttime))

starttime = time.time()
pi = monte_carlo_pi(1000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method with 1000 input time: " + str(endtime-starttime))

starttime = time.time()
pi = monte_carlo_pi(10000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method with 10000 input time: " + str(endtime-starttime))

starttime = time.time()
pi = monte_carlo_pi(100000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method with 100000 input time: " + str(endtime-starttime))

starttime = time.time()
pi = monte_carlo_pi(1000000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method with 1000000 input time: " + str(endtime-starttime))

starttime = time.time()
pi = monte_carlo_pi(10000000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method with 10000000 input time: " + str(endtime-starttime))

print("\nMonte carlo method for pi using numba\n")

starttime = time.time()
pi = nb_monte_carlo_pi(10)
endtime = time.time()
print("\nFirst run\n")
print("pi = " + str(pi) + " using monte carlo method(numba) with 10 input time: " + str(endtime-starttime))
print("\nSecond run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(10)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 10 input time: " + str(endtime-starttime))
print("\nFirst run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(100)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 100 input time: " + str(endtime-starttime))
print("\nSecond run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(100)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 100 input time: " + str(endtime-starttime))
print("\nFirst run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(1000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 1000 input time: " + str(endtime-starttime))
print("\nSecond run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(1000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 1000 input time: " + str(endtime-starttime))
print("\nFirst run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(10000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 10000 input time: " + str(endtime-starttime))
print("\nSecond run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(10000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 10000 input time: " + str(endtime-starttime))
print("\nFirst run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(100000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 100000 input time: " + str(endtime-starttime))
print("\nSecond run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(100000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 100000 input time: " + str(endtime-starttime))
print("\nFirst run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(1000000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 1000000 input time: " + str(endtime-starttime))
print("\nSecond run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(1000000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 1000000 input time: " + str(endtime-starttime))
print("\nFirst run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(10000000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 10000000 input time: " + str(endtime-starttime))
print("\nSecond run\n")
starttime = time.time()
pi = nb_monte_carlo_pi(10000000)
endtime = time.time()
print("pi = " + str(pi) + " using monte carlo method(numba) with 10000000 input time: " + str(endtime-starttime))