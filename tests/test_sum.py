import os 
import sys 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sum import sum


def test_sum_positive_numbers():
    assert sum(10,20) == 30


def test_sum_negative_numbers():
    assert sum(-10,-20) == -30

def test_sum_mixed_numbers():
    assert sum(10,-20) == -10