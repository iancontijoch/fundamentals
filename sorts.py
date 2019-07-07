# This file contains the fundamental sorts, implemented in python.

def selection_sort(arr):
    pass

def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
        if not swapped: break
    return arr

l = [5, 3, 4, 2, 1]

print(bubble_sort(l))