import numpy as np
from numpy_exercises import create_array, sum_array, reverse_array, multiply_elements

def test_create_array():
    result = create_array(5)
    assert isinstance(result, np.ndarray), "Output should be a NumPy array"
    assert result.shape == (5,), "Array should have the correct size"
    assert np.all(result == 0), "Array should contain all zeros"

def test_sum_array():
    arr = np.array([1, 2, 3, 4])
    assert sum_array(arr) == 10, "Sum should be the total of all array elements"

def test_reverse_array():
    arr = np.array([1, 2, 3, 4])
    result = reverse_array(arr)
    assert np.array_equal(result, np.array([4, 3, 2, 1])), "Array should be reversed"

def test_multiply_elements():
    arr = np.array([1, 2, 3])
    multiplier = 3
    result = multiply_elements(arr, multiplier)
    assert np.array_equal(result, np.array([3, 6, 9])), "Elements should be multiplied correctly"
