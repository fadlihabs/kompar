import numpy as np

size = 5
data = np.random.rand(size, size)

print("Original Data:\n", data)

def process1(x):
    return x * 2

def process2(x):
    return x + 5

def process3(x):
    return np.sqrt(x)

r1 = process1(data)
r2 = process2(data)
r3 = process3(data)

print("\nProcess 1 (x2):\n", r1)
print("\nProcess 2 (+5):\n", r2)
print("\nProcess 3 (sqrt):\n", r3)