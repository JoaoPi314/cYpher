import pytest
import numpy as np
from vigenere import *



@pytest.fixture
def generic_vigenere():
	key = np.array([2, 4, 6, 10, 23, 13, 56, 34, 123, 10, 345, 5, 22])
	return Vigenere(key)




def test_create_vigenere_key(generic_vigenere):
	''' Tests if the Vigenere object fixes the key passed as argument'''

	expected_key = np.array([2, 4, 6, 10, 23, 13, 4, 8, 19, 10, 7, 5, 22])

	assert generic_vigenere.get_key() == expected_key