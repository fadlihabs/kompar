import numpy as np
from multiprocessing import Pool
import time
import os

size = 300

A = np.random.rand(size, size)
B = np.random.rand(size, size)

def multiply_row(i):
    return np.dot(A[i], B)

if __name__ == "__main__":
    start = time.time()

    workers = os.cpu_count() // 2

    with Pool(workers) as p:
        result = p.map(multiply_row, range(size))

    C = np.array(result)

    end = time.time()

    print("CPU used:", workers)
    print("Matrix size:", size)
    print("Time:", end - start)