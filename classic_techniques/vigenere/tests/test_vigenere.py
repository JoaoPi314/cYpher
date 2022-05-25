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

	np.testing.assert_array_equal(generic_vigenere.get_key(), expected_key)
	assert generic_vigenere.get_key_length() == expected_key.size


def test_expand_key_if_text_is_greater(generic_vigenere):
	''' Tests if the Vigenere object can expand the key for a given text'''

	text_length = 30
	expected_expanded_key = np.array([2, 4, 6, 10, 23, 13, 4, 8, 19, 10, 7, 5, 22, 
					  			      2, 4, 6, 10, 23, 13, 4, 8, 19, 10, 7, 5, 22,
							 		  2, 4, 6, 10])
	
	generic_vigenere.expand_key(text_length)

	np.testing.assert_array_equal(generic_vigenere.get_expanded_key(), expected_expanded_key)
	assert generic_vigenere.get_expanded_key().size == text_length


def test_crypt(generic_vigenere):
	''' Tests if the Vigenere can encrypt a given message'''

	plain_text = 'Truly, if there is evil in this world, it lies within the heart of mankind.'

	expected_output = 'Vvavv, vj baoyj eu ibsi vr basz bktpj, sq ymml gpydkr zrb uiikd vk icrqskq.'

	assert generic_vigenere.crypt(plain_text) == expected_output

def test_decrypt(generic_vigenere):
	''' Tests if the Vigenere can decrypt a given message'''

	cipher_text = 'Vvavv, vj baoyj eu ibsi vr basz bktpj, sq ymml gpydkr zrb uiikd vk icrqskq.'

	expected_output = 'Truly, if there is evil in this world, it lies within the heart of mankind.'

	assert generic_vigenere.crypt(cipher_text, crypt=False) == expected_output
