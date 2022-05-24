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

		#Removes spaces
		





