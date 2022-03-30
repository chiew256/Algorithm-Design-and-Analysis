"""
Given the following array A = [16, 30, 95, 51, 84, 23, 62, 44], implement a program to sort the array using the following algorithm:

a)	Counting Sort
b)	Radix Sort
c)	Shell Sort

Provide the pseudocode, implement the algorithm using Python, explain the codes/algorithm, and explain running time complexity of each algorithm.

"""

A: list[int] = [16, 30, 95, 51, 84, 23, 62, 44]

B = [1, 5, 7, 8, 6, 4, 7, 4, 4, 6, 2]


def counting_sort(array: list[int]):
    output = [0] * len(array)
    count = [0] * (max(array) + 1)

    for i in range(1, len(array)):
        count[array[i]] += 1

    print(count)


counting_sort(B)
