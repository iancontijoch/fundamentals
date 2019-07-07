# This file contains the fundamental sorts, implemented in python.

def selection_sort(arr):
    # Implement the selection sort algorithm
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    length = len(arr)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped: break
    return arr
