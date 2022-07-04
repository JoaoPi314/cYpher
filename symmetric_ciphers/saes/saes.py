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
		# Excludes the most significant nibble (Trash)
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
		ms_nibble = output_byte >> 4
		ls_nibble = output_byte & 0x0F

		ms_output_nibble = self.__sub_unit_nibble(ms_nibble)
		ls_output_nibble = self.__sub_unit_nibble(ls_nibble)

		output_byte =  (ms_output_nibble << 4) ^ (ls_output_nibble)

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


	def __add_round_key(self, state, round_key):
		'''
		Method to add the round key to current state
		'''
		
		output_state = state.copy()
		
		for idx, x in np.ndenumerate(state):
			output_state[idx[0]][idx[1]] ^= round_key[idx[0]][idx[1]]

		return output_state

	def __gf16_mult(self, n1, n2):
		'''
		This method will implement a finite field multiplication (GF16) with
		a LUT
		'''
					  	 #1   #2  #3    #4   #5   #6   #7   #8   #9   #A   #B   #C   #D   #E   #F  
		LUT = np.array([[0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9, 0xA, 0xB, 0xC, 0xD, 0xE, 0xF], #1
						[0x2, 0x4, 0x6, 0x8, 0xA, 0xC, 0xE, 0x3, 0x1, 0x7, 0x5, 0xB, 0x9, 0xF, 0xD], #2
 						[0x3, 0x6, 0x5, 0xC, 0xF, 0xA, 0x9, 0xB, 0x8, 0xD, 0xE, 0x7, 0x4, 0x1, 0x2], #3
						[0x4, 0x8, 0xC, 0x3, 0x7, 0xB, 0xF, 0x6, 0x2, 0xE, 0xA, 0x5, 0x1, 0xD, 0x9], #4
						[0x5, 0xA, 0xF, 0x7, 0x2, 0xD, 0x8, 0xE, 0xB, 0x4, 0x1, 0x9, 0xC, 0x3, 0x6], #5
						[0x6, 0xC, 0xA, 0xB, 0xD, 0x7, 0x1, 0x5, 0x3, 0x9, 0xF, 0xE, 0x8, 0x2, 0x4], #6
						[0x7, 0xE, 0x9, 0xF, 0x8, 0x1, 0x6, 0xD, 0xA, 0x3, 0x4, 0x2, 0x5, 0xC, 0xB], #7
						[0x8, 0x3, 0xB, 0x6, 0xE, 0x5, 0xD, 0xC, 0x4, 0xF, 0x7, 0xA, 0x2, 0x9, 0x1], #8
						[0x9, 0x1, 0x8, 0x2, 0xB, 0x3, 0xA, 0x4, 0xD, 0x5, 0xC, 0x6, 0xF, 0x7, 0xE], #9
						[0xA, 0x7, 0xD, 0xE, 0x4, 0x9, 0x3, 0xF, 0x5, 0x8, 0x2, 0x1, 0xB, 0x6, 0xC], #A
						[0xB, 0x5, 0xE, 0xA, 0x1, 0xF, 0x4, 0x7, 0xC, 0x2, 0x9, 0xD, 0x6, 0x8, 0x3], #B
						[0xC, 0xB, 0x7, 0x5, 0x9, 0xE, 0x2, 0xA, 0x6, 0x1, 0xD, 0xF, 0x3, 0x4, 0x8], #C
						[0xD, 0x9, 0x4, 0x1, 0xC, 0x8, 0x5, 0x2, 0xF, 0xB, 0x6, 0x3, 0xE, 0xA, 0x7], #D
						[0xE, 0xF, 0x1, 0xD, 0x3, 0x2, 0xC, 0x9, 0x7, 0x6, 0x8, 0x4, 0xA, 0xB, 0x5], #E
						[0xF, 0xD, 0x2, 0x9, 0x6, 0x4, 0xB, 0x1, 0xE, 0xC, 0x3, 0x8, 0x7, 0x5, 0xA]], #F
						dtype=np.uint8)

		if (not n1 or not n2):
			return 0x0
		else:
			return LUT[n1-1][n2-1]


	def __mix_columns(self, state):
		'''
		Method to perform the mixColumn algorithm of SAES. It is a matrix multiplication
		in GF16
		'''

		output_state = np.zeros((2,2), dtype=np.uint8)
		output_state[0][0] = state[0][0] ^ self.__gf16_mult(4, state[1][0])
		output_state[1][0] = self.__gf16_mult(4, state[0][0]) ^ state[1][0]
		output_state[0][1] = state[0][1] ^ self.__gf16_mult(4, state[1][1])
		output_state[1][1] = self.__gf16_mult(4, state[0][1]) ^ state[1][1]

		return output_state


	def __format_state(self, i_data):
		'''
		Method to convert the data into the 2x2 matrix
		'''
		state = np.zeros((2, 2), dtype=np.uint8)

		state[0][0] = i_data[0] >> 4   #b0b1b2b3
		state[1][0] = i_data[0] & 0x0F #b4b5b6b7
		state[0][1] = i_data[1] >> 4   #b8b9bAbB
		state[1][1] = i_data[1] & 0x0F #bCbDbEbF

		return state


	def __revert_state(self, state):
		'''
		Method to convert back the state into an array
		'''
		o_data = np.zeros((2,), dtype=np.uint8)

		o_data[0] = (state[0][0] << 4) ^ state[1][0]
		o_data[1] = (state[0][1] << 4) ^ state[1][1]

		return o_data

	def __inv_sub_unit_nibble(self, nibble):
		'''
		Method to substitute a nibble by a value of inverse S-Box
		'''
						   #00  #01  #10  #11
		s_box = np.array([[0xA, 0x5, 0x9, 0xB],  #00
						  [0x1, 0x7, 0x8, 0xF],  #01
						  [0x6, 0x0, 0x2, 0x3],  #10 
						  [0xC, 0x4, 0xD, 0xE]]) #11

		r_index = nibble >> 2
		c_index = nibble & 0x3

		return s_box[r_index][c_index]


	def __inv_sub_nibble(self, state):
		'''
		Method that will apply the inverse s-box in a given state os S-AES
		'''
		sub_nibbles = np.vectorize(self.__inv_sub_unit_nibble)
		output_state = sub_nibbles(state)

		return output_state

	def __inv_mix_columns(self, state):
		'''
		Method to perform the iMixColumn algorithm of SAES. It is a matrix multiplication
		in GF16
		'''

		output_state = np.zeros((2,2), dtype=np.uint8)
		output_state[0][0] = self.__gf16_mult(9, state[0][0]) ^ self.__gf16_mult(2, state[1][0])
		output_state[1][0] = self.__gf16_mult(2, state[0][0]) ^ self.__gf16_mult(9, state[1][0])
		output_state[0][1] = self.__gf16_mult(9, state[0][1]) ^ self.__gf16_mult(2, state[1][1])
		output_state[1][1] = self.__gf16_mult(2, state[0][1]) ^ self.__gf16_mult(9, state[1][1])

		return output_state

	def crypt(self, i_data):
		'''
		Main method. It will receive a 16 bit stream (already in format of an array
		of 2 bytes) and perform the algorithm. The output will be an array of two bytes.
		The user must decodificate this array into a bitstream or whatever the message should
		be.
		'''

		# Format into state
		state = self.__format_state(i_data)

		# Round 0
		round_key = self.__format_state(self.expanded_key[0:2])
		state = self.__add_round_key(state, round_key)

		# Round 1
		state = self.__sub_nibble(state)
		state = self.__shift_rows(state)
		state = self.__mix_columns(state)
		round_key = self.__format_state(self.expanded_key[2:4])
		state = self.__add_round_key(state, round_key)

		# Round 2
		state = self.__sub_nibble(state)
		state = self.__shift_rows(state)
		round_key = self.__format_state(self.expanded_key[4:6])
		state = self.__add_round_key(state, round_key)

		o_data = self.__revert_state(state)

		return o_data

	def decrypt(self, cipher):
		'''
		Method to decrypt a given message
		'''

		# Format into state
		state = self.__format_state(cipher)

		# Round 0
		round_key = self.__format_state(self.expanded_key[4:6])
		state = self.__add_round_key(state, round_key)

		# Round 1
		state = self.__inv_sub_nibble(state)
		state = self.__shift_rows(state)
		state = self.__inv_mix_columns(state)
		round_key = self.__format_state(self.expanded_key[2:4])
		round_key = self.__inv_mix_columns(round_key)
		state = self.__add_round_key(state, round_key)

		# Round 2
		state = self.__inv_sub_nibble(state)
		state = self.__shift_rows(state)
		round_key = self.__format_state(self.expanded_key[0:2])
		state = self.__add_round_key(state, round_key)

		o_data = self.__revert_state(state)

		return o_data





		

