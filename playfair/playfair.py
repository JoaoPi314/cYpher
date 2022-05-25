import numpy as np
import string

class Playfair:
	def __init__(self, key):
		self.key = np.zeros((25, 1), dtype='<U1')
		self.__gen_key(key.upper())
	def get_key(self):
		return self.key

	def __gen_key(self, key):
		# Removes repeated characters from key
		key_without_repetitions = ''.join(dict.fromkeys(key))
		key_len = len(key_without_repetitions)
		# Creates a string with the alphabet in uppercase
		alphabet = string.ascii_uppercase
		alphabet = alphabet.replace('IJ', 'J')


		# Removes key letters from alphabet
		for letter in key_without_repetitions:
			if letter in alphabet:
				alphabet = alphabet.replace(letter, '')
		
		# Fills beginning of key
		for i in range(key_len):
			self.key[i] = key_without_repetitions[i]


		# Fills rest of the key
		for i in range(len(alphabet)):
			self.key[key_len + i] = alphabet[i]

		self.key = np.reshape(self.key, (5, 5))



	def format_text(self, plain_text):

		# Removes spaces
		removed_spaces = plain_text.replace(' ', '')

		# UpperCase
		uppercase_text = removed_spaces.upper()

		# Replaces I by J
		ij_replaced = uppercase_text.replace('I', 'J')

		# Inserts X between repeated characters
		x_between_repeated = ''
		for i in range(len(ij_replaced) - 1):
			if ij_replaced[i] == ij_replaced[i+1]:
				x_between_repeated = x_between_repeated + ij_replaced[i] + 'X'
			else:
				x_between_repeated += ij_replaced[i]

		x_between_repeated += ij_replaced[-1]
	
		# Inserts X if len of string is odd
		if len(x_between_repeated) % 2 == 1:
			x_between_repeated += 'X'

		return x_between_repeated		

	



