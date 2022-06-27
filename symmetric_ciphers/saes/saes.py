import numpy as np

class Saes:

	def __init__(self, key):
		# Expand Key at constructor
		self.key = key
		self.expanded_key = np.zeros((6,), dtype=np.uint8)
		self.__expand_key()


	def __rot_nible(self, input_byte):
		'''
		Method to rotate a nible (Used int expandKey algorithm)
		'''
		output_byte = input_byte << 4
		output_byte = output_byte ^ (input_byte >> 4)
		# Excludes the MSB nibble (Trash)
		output_byte = output_byte  & 0x0FF

		return output_byte

	def __sub_unit_nibble(self, nibble):
		'''
		Method to substitute a nibble by a value of S-Box
		'''
						   #00  #01  #10  #11
		s_box = np.array([[0x9, 0x4, 0xA, 0xB],  #00
						  [0xD, 0x1, 0x8, 0x5],  #01
						  [0x6, 0x2, 0x0, 0x3],  #10 
						  [0xC, 0xE, 0xF, 0x7]]) #11

		r_index = nibble >> 2
		c_index = nibble & 0x3

		return s_box[r_index][c_index]


	def __g_function(self, input_byte, round):
		'''
		Method used in expandKey algorithm
		'''
		rcon = np.array([0x8, 0x3])
		output_byte = 0x00

		# Rotation
		output_byte = self.__rot_nible(input_byte)

		# Substitution
		msb_nibble = output_byte >> 4
		lsb_nibble = output_byte & 0x0F

		msb_output_nibble =self.__sub_unit_nibble(msb_nibble)
		lsb_output_nibble =self.__sub_unit_nibble(lsb_nibble)

		output_byte = (msb_output_nibble << 4) ^ (lsb_output_nibble)

		# Rcon operation
		output_byte = output_byte ^ (rcon[round] << 4)

		return output_byte


	def __expand_key(self):
		'''
		Method to expand the key into 6 words (bytes)
		'''
		self.expanded_key[0] = self.key[0]
		self.expanded_key[1] = self.key[1]
		self.expanded_key[2] = self.expanded_key[0] ^ (self.__g_function(self.expanded_key[1], 0))
		self.expanded_key[3] = self.expanded_key[2] ^ self.expanded_key[1]
		self.expanded_key[4] = self.expanded_key[2] ^ (self.__g_function(self.expanded_key[3], 1))
		self.expanded_key[5] = self.expanded_key[4] ^ self.expanded_key[3]


	def __sub_nibble(self, state):
		'''
		Method that will apply the s-box in a given state os S-AES
		'''
		sub_nibbles = np.vectorize(self.__sub_unit_nibble)
		output_state = sub_nibbles(state)

		return output_state


	def __shift_rows(self, state):
		'''
		Method to shift rows of state
		'''

		output_state = state.copy()
		output_state[1][0] = state[1][1]
		output_state[1][1] = state[1][0]

		return output_state