from sorts import bubble_sort, selection_sort, quicksort
import numpy as np

# number of random arrays to be tested
n = 100
test_arrays = [list(np.random.randint(-100, 100, 10)) for _ in range(n)]

def test_function(func, test_data):
    return all([func(l) == sorted(l) for l in test_data])

# Test Bubble Sort
if test_function(bubble_sort, test_arrays):
    print('Bubble sort works as expected.')
if test_function(selection_sort, test_arrays):
    print('Selection sort works as expected.')
if test_function(quicksort, test_arrays):
    print('Quicksort works as expected.')
    