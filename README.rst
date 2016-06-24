.. image:: https://travis-ci.org/killswitch-GUI/zlib_wrapper.svg?branch=master
    :target: https://travis-ci.org/killswitch-GUI/zlib_wrapper
.. image:: https://coveralls.io/repos/github/killswitch-GUI/zlib_wrapper/badge.svg?branch=master :target: https://coveralls.io/github/killswitch-GUI/zlib_wrapper?branch=master
zlib_wrapper
--------

A very small library for building crc32 header on top of zlib (in 2.7 standard library). Was built to learn pip packaging, and implement compression before encryption for EmPyre https://github.com/adaptivethreat/EmPyre.

To get up and running:

    >>> from zlib_wrapper import compress
    >>> from zlib_wrapper import decompress
    
zlib_wrapper compression step-by-step
--------

To get you crc32 for supplied data or string:

    >>> data = "Killswitc-gui is a sick handle"
    >>> c = compress.compress()
    >>> start_crc32 = ac.crc32_data(data)
    
To get your compressed for suplied data or string:

    >>> comp_data = a.comp_data(data)

To build your custom zlib header with crc32:
    
    >>> final_comp_data = a.build_header(comp_data, start_crc32)

zlib_wrapper decompression step-by-step
--------

Decompression goes through crc32 checks and returns a custom dictonary object. 

To decompress your compressed data:

    >>> dec_data = b.dec_data(final_comp_data)
    {'data': 'Killswitc-gui is a sick handle', 'header_crc32': 2727504892, 'crc32_check': True, 'dec_crc32': 2727504892}
    
