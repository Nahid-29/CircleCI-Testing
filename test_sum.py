import pytest
from sum import summation  # Replace 'your_module' with the actual module name

def test_summation():
    # Test case 1: Check summation of a list of positive numbers
    assert summation([1, 2, 3, 4, 5]) == 15
    
    # Test case 2: Check summation with negative numbers
    assert summation([-1, -2, -3, -4, -5]) == -15
    
    # Test case 3: Check summation with mixed numbers
    assert summation([1, -2, 3, -4, 5]) == 3
    
    # Test case 4: Check summation with an empty list
    assert summation([]) == 0
