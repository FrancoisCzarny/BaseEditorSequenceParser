#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
# TODO : User documentation:
How to use:
This script can be executed from the command line interface (CLI, such as the terminal or PowerShell console). From this console the current directory has to be the one where sequenceParser.py is stored and then write: python sequenceParser.py /your/path/file.txt
"""

import os
import sys


def is_pam_around(pam, backward=True):
    if backward:
        pass
    else:
        pass


def upper_codon_inframe(text_file, search_sequence=["tgg", "cag", 'cga', 'caa']):
    """
    # TODO: Docstring
    """
    file_path = text_file

    l = list(os.path.splitext(file_path))
    l.insert(1, '_parsed')
    list_res = list()

    f = open(file_path, 'r+')
    s = f.read()
    f.close()

    for i in range(0, (len(s)-1), 3):
        if s[i:i+3] in search_sequence:
            list_res.append(s[i:i+3].upper())
        else:
            list_res.append(s[i:i+3])

    res = ''.join(list_res)

    with open(''.join(l), "w+") as io_handler:
        io_handler.write(res)


if __name__ == "__main__":
    param = sys.argv[1]
    pam = raw_input('Which PAM? ')
    print("\t ---- Parsing file for PAM ({}): {} ----".format(pam, param))
    upper_codon_inframe(param)
