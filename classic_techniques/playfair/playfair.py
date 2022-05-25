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

	
	def crypt(self, plain_text):

		formated_text = self.format_text(plain_text)

		# Iterates two by two
		cipher_message = ''

		for i in range(0, len(formated_text) - 1, 2):
			actual_digram = formated_text[i:i+2]
			
			r_first_digram = np.where(self.key == actual_digram[0])[0][0]
			c_first_digram = np.where(self.key == actual_digram[0])[1][0]

			r_sec_digram = np.where(self.key == actual_digram[1])[0][0]
			c_sec_digram = np.where(self.key == actual_digram[1])[1][0]

			first_cipher_char = ''
			sec_cipher_char = ''

			# Rules of playfair
			if r_first_digram == r_sec_digram:

				first_cipher_char = self.key[r_first_digram][(c_first_digram+1)%5]
				sec_cipher_char = self.key[r_sec_digram][(c_sec_digram+1)%5]

				cipher_message += first_cipher_char + sec_cipher_char
			elif c_first_digram == c_sec_digram:

				first_cipher_char = self.key[(r_first_digram+1)%5][c_first_digram]
				sec_cipher_char = self.key[(r_sec_digram+1)%5][c_sec_digram]

				cipher_message += first_cipher_char + sec_cipher_char
			else:
				first_cipher_char = self.key[r_first_digram][c_sec_digram]
				sec_cipher_char = self.key[r_sec_digram][c_first_digram]

				cipher_message += first_cipher_char + sec_cipher_char

		return cipher_message



	def decrypt(self, cipher_message):

		# Iterates two by two
		decipher_message = ''

		for i in range(0, len(cipher_message) - 1, 2):
			actual_digram = cipher_message[i:i+2]
			
			r_first_digram = np.where(self.key == actual_digram[0])[0][0]
			c_first_digram = np.where(self.key == actual_digram[0])[1][0]

			r_sec_digram = np.where(self.key == actual_digram[1])[0][0]
			c_sec_digram = np.where(self.key == actual_digram[1])[1][0]

			first_decipher_char = ''
			sec_decipher_char = ''

			# Rules of playfair
			if r_first_digram == r_sec_digram:

				first_decipher_char = self.key[r_first_digram][(c_first_digram-1)%5]
				sec_decipher_char = self.key[r_sec_digram][(c_sec_digram-1)%5]

				decipher_message += first_decipher_char + sec_decipher_char
			elif c_first_digram == c_sec_digram:

				first_decipher_char = self.key[(r_first_digram-1)%5][c_first_digram]
				sec_decipher_char = self.key[(r_sec_digram-1)%5][c_sec_digram]

				decipher_message += first_decipher_char + sec_decipher_char
			else:
				first_decipher_char = self.key[r_first_digram][c_sec_digram]
				sec_decipher_char = self.key[r_sec_digram][c_first_digram]

				decipher_message += first_decipher_char + sec_decipher_char

		return decipher_message



