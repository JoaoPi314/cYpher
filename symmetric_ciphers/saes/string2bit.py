import bitarray
import numpy as np

def string2bit(i_string):
	ba = bitarray.bitarray()
	ba.frombytes(i_string.encode('utf-8'))
	i_list = ba.tolist()
	o_bitstream = ''.join(map(str, i_list))
	
	return o_bitstream


def bit2bytearray(i_bitstream):

	# Parses into interval of 1 byte
	previous_i = 0
	array_index = 0
	byte_array = ['']*(int(len(i_bitstream) / 8))
	for i in range(1, len(i_bitstream) + 1):
		if (i % 8) == 0:
			byte_array[array_index] = int(i_bitstream[previous_i:i], 2)
			array_index += 1
			previous_i = i



	# There is no need to worry abou the bitstream length
	return np.array(byte_array, dtype=np.uint8)

