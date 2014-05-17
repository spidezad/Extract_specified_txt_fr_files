Extract_specified_txt_fr_files
==============================

Module to extract specified portion of txt from a txt file
Module that extract user defined paragraph chuncks from a text file.

Usage:
    User mark the start and end position of text required with specific symbol, eg '@'
    Multiple marking can be done and can be specified by using overlap or non overlapping mode.
    Overlapping mode will use each subsequent symbol as end position as well as start position of next paragraph.
    Non Overlapping mode make even symbol index to be end position\
    so each pair of symbol index represent a paragraph to be extracted.

