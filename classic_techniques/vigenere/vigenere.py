import numpy as np
import string

'''
The vigenère is a cipher technique that consists in
apply the caesar cipher to each charactere, with a 
different key
'''
class Vigenere:

	def __init__(self, key):
		'''
		The constructor will only get the key passed by the user
		'''
		self.key_length = int(key.size)
		self.key = key % 26
		self.expanded_key = []

	def get_key(self):
		return self.key

	def get_key_length(self):
		return self.key_length

	def get_expanded_key(self):
		return self.expanded_key


	def expand_key(self, text_length):
		'''
		This method will expand the key considering the size of the
		plain text
		'''
		self.expanded_key = np.zeros((text_length,), dtype='int')

		for i in range(text_length):
			self.expanded_key[i] = self.key[i%self.get_key_length()]


	def caesar_single_char(self, charactere, key, crypt=True):
		'''
		This method will apply the caesar cipher in one charactere (encrypt and decrypt)
		'''

		output_char  = charactere
		# Booleans to check overlap in ASCII table (c stands for crypt and d for decrypt)
		overlap_lower_case_c = (str.islower(charactere) and (ord(charactere) + key > 122))
		overlap_upper_case_c = (str.isupper(charactere) and (ord(charactere) + key > 90))
		overlap_lower_case_d = (str.islower(charactere) and (ord(charactere) - key < 97))
		overlap_upper_case_d = (str.isupper(charactere) and (ord(charactere) - key < 65))
		
		if crypt:
			if str.isalpha(charactere):
				output_char = chr(ord(charactere) + key)
				if (overlap_lower_case_c or overlap_upper_case_c):
					output_char = chr(ord(output_char) - 26)
		else:
			if str.isalpha(charactere):
				output_char = chr(ord(charactere) - key)
				if (overlap_lower_case_d or overlap_upper_case_d):
					output_char = chr(ord(output_char) + 26)

		return output_char

	def crypt(self, plain_text, crypt=True):
		'''
		The crypt method can encrypt and decrypt
		'''
		
		# Count text_length without spaces and punctuation
		raw_text = plain_text.replace(' ', '')
		raw_text = raw_text.translate(str.maketrans('', '', string.punctuation))

		text_length = len(raw_text)

		# Expand key
		self.expand_key(text_length)

		# Iterate and apply Caesar
		cipher_message = ''

		key_index = 0
		for i in range(len(plain_text)):
			if(str.isalpha(plain_text[i])):
				cipher_message += self.caesar_single_char(plain_text[i], self.expanded_key[key_index], crypt)
				key_index += 1
			else:
				cipher_message += plain_text[i]

		return cipher_message

		

