# ----------------------------------------------------------------------
# The followig script converts a single .dat file to a .pdb file
# Usage: python3 top2pdb.py <filename.dat>
# Author: Elena Rogoulenko, 2023
# Date: 2023-08-02
# Version: 1.0
# ----------------------------------------------------------------------

import numpy as np
import sys

def ParseDatCoordinates(s):
    n = [5,4,4,3,8,8,8,8]
    idx_str, index_str, name, residue, x_str, y_str, z_str, mass_str     = [s[sum(n[:i]):sum(n[:i+1])].strip() for i in range(len(n))]
    idx, index, x, y, z, mass     = int(idx_str), int(index_str), float(x_str), float(y_str), float(z_str), float(mass_str)
    return idx, name, residue, index, x, y, z, mass

def top2pdb(file,save=True):
    """Writes single .dat file with one model to .pdb file"""
    # print('OPEN'.center(100,'-'),file,sep='\n')
    datLines = open(file,'r').readlines()
    pdbLines = []
    for line in datLines:
        if 'is the size of chain' in line and 'is the size of chain' not in datLines[datLines.index(line)+1]:
            coords = datLines.index(line)+1
    lines = np.arange(coords,len(datLines))
    for item in lines:
        spltLines = ParseDatCoordinates(datLines[item])
        pdbstring = 'ATOM{:>7}{:>4}{:>5}{:>6}{:>12}{:>8}{:>8}{:>6}  0.00\n'.format(*spltLines)
        pdbLines.append(pdbstring)
    if save==True:
        pdbFile = open(file+'.pdb','w')
        for line in pdbLines:
            pdbFile.write(line)
        pdbFile.close()
        print(' GENERATED PDB '.center(40,'='),f'{file}.pdb',sep='\n')

filename = sys.argv[1]
top2pdb(filename)