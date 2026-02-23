# sisd_matrix_add.py
import numpy as np
import time

size = 1000

A = np.random.rand(size, size)
B = np.random.rand(size, size)

start = time.time()

C = np.zeros((size, size))

for i in range(size):
    for j in range(size):
        C[i][j] = A[i][j] + B[i][j]

end = time.time()

print("SISD Time:", end - start)