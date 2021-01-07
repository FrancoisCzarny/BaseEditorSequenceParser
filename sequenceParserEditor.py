#!/usr/bin/python
# -*- coding : utf-8 -*-

"""
# TODO : User documentation:
How to use:
This script can be executed from the command line interface (CLI, such as the
terminal or PowerShell console). From this console the current directory has to
be the one where sequenceParser.py is stored and then write: python
sequenceParserEditor.py /your/path/file.txt
"""

import os
import sys


MAP_BASE = {'n': 'n',
            'g': 'c', 'c': 'g',
            'a': 't', 't': 'a'}


def pam_reverse_strand(pam):
    pam_reversed = pam.lower()
    return ''.join([s.replace(s, MAP_BASE[s]) for s in pam_reversed])[::-1]


def compute_possible_pam(pam):
    return [i.replace('n', j) for i, j in zip([pam] * 4, ['c', 'g', 'a', 't'])]


def upper_codon_inframe(text_file, pam, search_sequence=["tgg", "cag", 'cga', 'caa']):
    file_path = text_file

    l = list(os.path.splitext(file_path))
    l.insert(1, '_parsed')
    list_res = list()

    with open(file_path, 'r+') as f:
        s = f.read()

    # validate file
    if (s[0:3].lower() != 'atg') or (len(s)%3 != 0):
        raise TypeError('Wrong file content: This is not a cDNA sequence.')
        sys.exit()

    possible_pam = compute_possible_pam(pam)
    print(possible_pam)
    pam_reversed = pam_reverse_strand(pam)
    print(pam_reversed)
    possible_rev_pam = compute_possible_pam(pam_reversed)
    print(possible_rev_pam)

    list_res = []
    for i in range(0, len(s), 3):
        codon = s[i:i+3]
        if (codon in search_sequence):
            if  (codon[0] == 'c') and any([p in s[i+13:i+22] for p in possible_pam]):
                list_res.append(codon.upper())
                print(codon.upper(), s[i:i+22])
            elif (codon[0] == 't') and any([p in s[i-21:i-12] for p in possible_rev_pam]):
                list_res.append(codon.upper())
                print(codon.upper(), s[i-21:i])
            else:
                list_res.append(codon)
        else:
            list_res.append(codon)

    res = ''.join(list_res)

    with open(''.join(l), "w+") as io_handler:
        io_handler.write(res)


if __name__ == "__main__":
    param = sys.argv[1]
    pam = input('Which PAM? ')
    print("\t ---- Parsing file for PAM ({}): {} ----".format(pam, param))
    upper_codon_inframe(param, pam)

