# import pytest
import pytest

# import the function from your file
from session import add_numbers
from session import sub_numbers

# Check if properly adds positive numbers
def test_add_positive():
    assert add_numbers(1,2) == 3

# Check if properly adds zero
def test_add_zero():
    assert add_numbers(1,0) == 1

# Check with negative numbers
def test_add_negative():
    assert add_numbers(4, -100) == -96

# Now check if it correctly produces error when provided so
def test_add_string_expect_exception():
    with pytest.raises(TypeError):
        add_numbers(4, 'I do not belong here')
        
        
# Check if properly adds positive numbers
def test_sub_positive():
    assert sub_numbers(2,1) == 1

# Check if properly subtracts zero
def test_sub_zero():
    assert sub_numbers(1,0) == 1

# Check with negative numbers
def test_sub_negative():
    assert add_numbers(100,-4) == 104

# Now check if it correctly produces error when provided so
def test_sub_string_expect_exception():
    with pytest.raises(TypeError):
        sub_numbers(4, 'I do not belong here')
