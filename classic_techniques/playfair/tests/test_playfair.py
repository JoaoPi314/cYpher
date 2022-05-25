import pytest
import numpy as np

from playfair import *

@pytest.fixture
def general_playfair():
    '''Returns a general object with a given key'''
    return Playfair('JoaoPedro')

@pytest.fixture
def general_key():
    '''Returns the general key'''
    key = np.array([['J', 'O', 'A', 'P', 'E'],
                    ['D', 'R', 'B', 'C', 'F'],
                    ['G', 'H', 'K', 'L', 'M'],
                    ['N', 'Q', 'S', 'T', 'U'],
                    ['V', 'W', 'X', 'Y', 'Z']])
    return key


def test_create_key(general_playfair, general_key):
    '''
    Tests if the Playfair object can create the 5x5 array with a
    given key
    '''
    np.testing.assert_array_equal(general_key, general_playfair.get_key())


def test_input_treatment(general_playfair):
    '''
    Tests if the Playfair is formating the plain_text before cipher
    '''

    input_plain_text = 'Hello Joao Pedro'
    formated_text = 'HELXLOJOAOPEDROX'

    assert general_playfair.format_text(input_plain_text) == formated_text

def test_crypt(general_playfair):
    '''
    Tests if the Playfair can encrypt a given plain text
    '''

    plain_text = 'Hello World'
    expected_output = 'MOKYHPORCHBV'

    assert general_playfair.crypt(plain_text) == expected_output

def test_decrypt(general_playfair):
    '''
    Tests if the Playfair can decrypt a given cipher_message
    '''
    cipher_message = 'MOKYHPORCHBV'
    expected_output = 'HELXLOWORLDX'

    assert general_playfair.decrypt(cipher_message) == expected_output
    