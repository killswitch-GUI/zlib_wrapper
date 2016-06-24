# Author: Alexander Rymdeko-Harvey(@Killswitch-GUI)
# License: BSD 3-Clause
# Copyright (c) 2016, Alexander Rymdeko-Harvey 
# All rights reserved. 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met: 
#  * Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer. 
#  * Redistributions in binary form must reproduce the above copyright 
#    notice, this list of conditions and the following disclaimer in the 
#    documentation and/or other materials provided with the distribution. 
#  * Neither the name of  nor the names of its contributors may be used to 
#    endorse or promote products derived from this software without specific 
#    prior written permission. 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.

import zlib
import struct

# 4 byte header
# crc32 uLong 
#
# 0   1
# +---+---+
# |CMF|FLG|
# +---+---+
# bits 0 to 3  CM     Compression method
# bits 4 to 7  CINFO  Compression info

class decompress(object):
    
    '''
    Base clase for init of the package. This will handle
    the initial object creation for conducting basic functions.
    '''

    CRC_HSIZE = 4
    COMP_RATIO = 9

    def __init__(self, verbose=False):
        """
        Populates init.
        """
        pass

    def dec_data(self, data, cheader=True):
        '''
        Takes:
        Custom / standard header data
        data = comp data with zlib header
        BOOL cheader = passing custom crc32 header

        returns:
        dict with crc32 cheack and dec data string
        ex. {"crc32" : true, "dec_data" : "-SNIP-"}
        '''
        if cheader:
            comp_crc32 = struct.unpack("!I", data[:self.CRC_HSIZE])[0]
            dec_data = zlib.decompress(data[self.CRC_HSIZE:])
            dec_crc32 = zlib.crc32(dec_data) & 0xFFFFFFFF
            if comp_crc32 == dec_crc32:
                crc32 = True
            else:
                crc32 = False
            return { "header_crc32" : comp_crc32, "dec_crc32" : dec_crc32, "crc32_check" : crc32, "data" : dec_data }
        else:
            dec_data = zlib.decompress(data)
            return dec_data
