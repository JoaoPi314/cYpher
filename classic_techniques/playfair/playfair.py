import numpy as np
import string

'''
PlayFair Cipher is a classic technique that uses a
5x5 matrix to encrypt data.
'''
class Playfair:
	
	def __init__(self, key):
		'''
		The key is passed as string, the constructor will fill the
		5x5 matrix with the given key
		'''
		self.key = np.zeros((25, 1), dtype='<U1')
		self.__gen_key(key.upper())


	def get_key(self):
		return self.key

	def __gen_key(self, key):
		'''
		Private method to generate the 5x5 matrix. It is private
		because it is not supposed to be called by the user, only by the
		class constructor
		'''

		# Removes repeated characters from key
		key_without_repetitions = ''.join(dict.fromkeys(key))
		key_len = len(key_without_repetitions)


		# Creates a string with the alphabet in uppercase
		alphabet = string.ascii_uppercase
		alphabet = alphabet.replace('IJ', 'I')
		key_without_repetitions = key_without_repetitions.replace('J', 'I')

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



	def __format_text(self, plain_text):
		'''
		This private method will format the plain text considering the playfair
		rules.
		'''

		# Removes spaces
		removed_spaces = plain_text.replace(' ', '')

		# removes punctuation
		removed_punctuation = removed_spaces.translate(str.maketrans('', '', string.punctuation))

		# UpperCase
		uppercase_text = removed_punctuation.upper()

		# Replaces I by J
		ij_replaced = uppercase_text.replace('J', 'I')

		x_fill = ''
		i = 0

		# Fills with 'X' between repeated digrams and at end of plain text is
		# necessary
		while(i < len(ij_replaced)):
			digram = ij_replaced[i:i+2]

			if(len(digram) == 2):
				# Checks repeated
				if(digram[0] == digram[1]):
					x_fill += digram[0] + 'X'
					i -= 1
				else:
					x_fill += digram

			else:
				x_fill += digram + 'X'
			i += 2
	
		return x_fill	

	
	def crypt(self, plain_text):
		'''
		The main method. It will encrypt a given plain text
		'''
		formated_text = self.__format_text(plain_text)

		# Iterates two by two
		cipher_message = ''

		for i in range(0, len(formated_text) - 1, 2):
			actual_digram = formated_text[i:i+2]
			
			# Get rows and collumns of each digram in key
			r_first_digram = np.where(self.key == actual_digram[0])[0][0]
			c_first_digram = np.where(self.key == actual_digram[0])[1][0]

			r_sec_digram = np.where(self.key == actual_digram[1])[0][0]
			c_sec_digram = np.where(self.key == actual_digram[1])[1][0]

			first_cipher_char = ''
			sec_cipher_char = ''

			# Rules of playfair
			if r_first_digram == r_sec_digram:
				# Cipher character is one to the right
				first_cipher_char = self.key[r_first_digram][(c_first_digram+1)%5]
				sec_cipher_char = self.key[r_sec_digram][(c_sec_digram+1)%5]

				cipher_message += first_cipher_char + sec_cipher_char
			elif c_first_digram == c_sec_digram:
				# Cipher character is one down
				first_cipher_char = self.key[(r_first_digram+1)%5][c_first_digram]
				sec_cipher_char = self.key[(r_sec_digram+1)%5][c_sec_digram]

				cipher_message += first_cipher_char + sec_cipher_char
			else:
				# Cipher character is the collumn of the other digram
				first_cipher_char = self.key[r_first_digram][c_sec_digram]
				sec_cipher_char = self.key[r_sec_digram][c_first_digram]

				cipher_message += first_cipher_char + sec_cipher_char

		return cipher_message



	def decrypt(self, cipher_message):
		'''
		This method will decrypt a given cipher message
		'''

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



