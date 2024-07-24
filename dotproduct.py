# matrix dox product
import numpy as np

A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
B = [[2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]]

u = [2, -5, 6]
v = [8, 2, -3]

u2 = [4, 2, -3, 5, -1]
v2 = [2, 6, -1, -4, 8]

print(np.dot(A, B))
print(np.dot(u, v))
print(np.dot(u2, v2))