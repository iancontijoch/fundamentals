from sorts import bubble_sort, selection_sort, quicksort, insertion_sort
import numpy as np

# # custom array
# l = [6, 5, 3, 1, 8, 7, 2, 4]


# number of random arrays to be tested
n = 3
test_arrays_orig = [list(np.random.randint(-100, 100, 10)) for _ in range(n)]
test_arrays_copy = test_arrays_orig

def test_function(func, test_data):
    return all([func(l) == sorted(l) for l in test_data])

# Test Sorts
if test_function(bubble_sort, test_arrays_copy):
    print('Bubble sort works as expected.')
if test_function(selection_sort, test_arrays_copy):
    print('Selection sort works as expected.')
if test_function(quicksort, test_arrays_copy):
    print('Quicksort works as expected.')
if test_function(insertion_sort, test_arrays_orig):
    print('Insertion Sort works as expected.')
else:
    print("Insertion Sort is buggy.")