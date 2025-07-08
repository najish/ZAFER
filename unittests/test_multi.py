import sys 
import os 


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from multi import multi

def test_multi_positive_numbers():
    assert multi(5, 18) == -90

def test_multi_mixed_numbers():
    assert multi(-5,2) == -10

