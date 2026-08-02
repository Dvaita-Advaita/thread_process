from multiprocessing import Pool
import time

def sq(n):
    total = 0
    for x in range(n + 1):
        total += x ** 2
    return total

# Parallel
t0 = time.time()

with Pool() as p:
    result = p.map(sq, range(10000))

t1 = time.time()

print("Parallel:", t1 - t0)

# Serial
t2 = time.time()

result = []
for i in range(10000):
    result.append(sq(i))

t3 = time.time()

print("Serial:", t3 - t2)