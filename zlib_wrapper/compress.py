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

class compress(object):
    
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

    def comp_data(self, data, cvalue=COMP_RATIO):
        '''
        Takes in a string and computes
        the comp obj.
        data = string wanting compression
        cvalue = 0-9 comp value (default 6)
        '''
        cdata = zlib.compress(data,cvalue)
        return cdata

    def crc32_data(self, data):
        '''
        Takes in a string and computes crc32 value.
        data = string before compression

        returns:
        HEX bytes of data
        '''
        crc = zlib.crc32(data) & 0xFFFFFFFF
        return crc

    def build_header(self, data, crc):
        '''
        Takes comp data, org crc32 value,
        and adds self header.
        data =  comp data
        crc = crc32 value
        '''
        header = struct.pack("!I",crc)
        built_data = header + data
        return built_data
