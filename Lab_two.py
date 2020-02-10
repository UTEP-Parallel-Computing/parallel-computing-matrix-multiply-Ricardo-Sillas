# Parallel Computing Lab 1
# Ricardo Sillas
import pymp
import time
from MatrixUtils import genMatrix, genMatrix2, printSubarray

# This is where it multiplies two square matrices where they are of equal size.
def multiply_matrices(arr):
    final_arr = [[0 for i in range(len(arr))] for i in range(len(arr))]
    with pymp.Parallel(6) as p:
        for i in p.range(len(arr)):
            for j in range(len(arr)):
                x = 0
                for k in range(len(arr)):
                    x += (arr[i][k]*arr[k][j])
                final_arr[i][j] = x
    return final_arr

def main():
    array_one = genMatrix()
    array_two = genMatrix2()
    start_time = time.time()
    arr = multiply_matrices(array_two)
    print((time.time()-start_time))
    printSubarray(arr)

main()
