import os 
import sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sub import sub


def test_sub_positive_numbers():
    assert sub(10,20) == -10


def test_sub_negative_numbers():
    assert sub(-10,-20) == 10

def test_sub_mixed_numbers():
    assert sub(10,-20) == 30