# Parallel Computing Lab 1
# Ricardo Sillas
import time


# This is where it multiplies two square matrices where they are of equal size.
def multiply_matrices(arr, arr_one):
    final_arr = [[0 for i in range(len(arr))] for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            x = 0
            for k in range(len(arr)):
                x += (arr[i][k]*arr_one[k][j])
            final_arr[i][j] = x
    return final_arr


# This is where it crates a square matrix where each index contains a different number.
# Has 2 parameters, one to get the size, and one set your starting number.
# The array starts with the starting number you set, and sets the next number to the previous number +1.
def matrix_creator(size, number):
    arr = [[0 for i in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(size):
            arr[i][j] = number
            number += 1
    return arr


def main():
    ##############################################################
    # Test to check if the multiplying method was working.
    list_c = []
    c = [1, 2, 3]
    c_ = [5, 6, 6]
    _c = [9, 12, 18]
    b = [3, 4, 0]
    b_ = [7, 8, -1]
    _b = [-2, -3, -4]
    list_b = []
    list_b.append(b)
    list_b.append(b_)
    list_b.append(_b)
    list_c.append(c)
    list_c.append(c_)
    list_c.append(_c)
    # print(list_c)
    # print(list_b)
    ################################################################
# Allows the user to input the size and the two starting numbers for the two matrices.
# The size must be greater than 400, or it will not take longer than 10 seconds.
    size = input("Please enter a size for the array. The array must be greater than 400. ")
    while int(size) < 400:
        size = input("Please try again. ")
    starting_one = input("Please enter a starting number for the first array. ")
    starting_two = input("Please enter a starting number for the second array. ")
    array_one = matrix_creator(int(size), float(starting_one))
    array_two = matrix_creator(int(size), float(starting_two))
    start_time = time.time()
    multiply_matrices(array_one, array_two)
    print(time.time()-start_time)


main()
