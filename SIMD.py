import numpy as np
import time

size = 1000

A = np.random.rand(size, size)
B = np.random.rand(size, size)

start = time.time()

C = A + B

end = time.time()

print("SIMD (Vectorized) Time:", end - start)