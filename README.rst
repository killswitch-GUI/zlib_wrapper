.. image:: https://travis-ci.org/killswitch-GUI/zlib_wrapper.svg?branch=master
    :target: https://travis-ci.org/killswitch-GUI/zlib_wrapper
.. image:: https://coveralls.io/repos/github/killswitch-GUI/zlib_wrapper/badge.svg?branch=master :target: https://coveralls.io/github/killswitch-GUI/zlib_wrapper?branch=master
zlib_wrapper
--------

To get up and running:

    >>> from zlib_wrapper import compress
    >>> from zlib_wrapper import decompress
    
zlib_wrapper compression step-by-step
--------
    
To get you crc32 for suplied data or string:

    >>> data = "Always check your data"
    >>> c = compress.compress()
    >>> start_crc32 = ac.crc32_data(data)
    
To get your compressed for suplied data or string:

    >>> comp_data = a.comp_data(data)

To build your custom zlib header with crc32:
    
    >>> final_comp_data = a.build_header(comp_data, start_crc32)
