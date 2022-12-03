import time
import numpy as np
a = np.random.rand(1000000)
b = np.random.rand(1000000)
print("a is: ", a)
print("b is: ", b)
tic = time.time()
c = np.dot(a, b)
toc = time.time()
print(c)
print("Vectorized Version: " + str(1000 * (toc - tic)) + " ms")
print("## Non Vectorized ##")
tic = time.time()
for i in range(1000000):
    c += a[i] * b[i]
toc = time.time()
print(c)
print("for loop: " + str(1000 * (toc - tic)) + " ms")
