# 9/10/2024

import numpy as np
import sympy as sp
from sympy import *

def createMatrix(m: int, n: int) -> sp.Matrix:
    matrix_entries = []
    print(f"Enter the entries for a {m}x{n} matrix:")
    for i in range(m):
        row = []
        for j in range(n):
            entry = input(f"Entry (Row: {i + 1}, Column: {j + 1}): ")
            row.append(sp.sympify(entry)) # Convert input to SymPy-compatible type
        matrix_entries.append(row)
    return sp.Matrix(matrix_entries)

def matrix() -> sp.Matrix:
    m:int = input("m")
    n:int = input("n")
    M: sp.Matrix = createMatrix(m,n)
    userInput:int = input("Enter an integer: ")
    match userInput:
        case 0: return
        case 1: M.ref()
        case 2: M.rref()
        case 3: M.det()
        case 4: M.adj()
        case 5: M.transpose()
        case 6: M.inv()
    return M

#pprint(matrix)

# vector space, null space # %%