import os
import sys
from zlib_wrapper import zlib_wrapper

def test_all():
	a.zlib_wrapper.compress()
	data = "Killswitc-gui is a sick handle"
	start_crc32 = a.crc32_data(data)
	print "-Starting str: ", data
	print "-un-compressed data size: ", str(sys.getsizeof(data))
	print "-Start crc32 value: " + str(start_crc32)
	comp_data = a.comp_data(data)
	print "-Compression data size: " + str(sys.getsizeof(comp_data))
	final_comp_data = a.build_header(comp_data, start_crc32)
	print "-Compression data with CRC header built size: " + str(sys.getsizeof(final_comp_data))
	print "-Starting decompress of data!"
	dec_data = a.dec_data(final_comp_data)
	print "-Final return data dict: ", dec_data
	print dec_data['crc32_check']

	assert start_crc32 == 2727504892
	assert sys.getsizeof(data) == 67
	assert comp_data 
	assert sys.getsizeof(final_comp_data) == 75
	assert dec_data['crc32_check'] == True
	assert dec_data['data'] == data
	assert dec_data['header_crc32'] == start_crc32
	assert dec_data['dec_crc32'] == start_crc32

