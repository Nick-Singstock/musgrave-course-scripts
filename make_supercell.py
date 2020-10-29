#!/usr/bin/env python
"""
Created on Fri Sep 13 12:58:56 2019

@author: Nick
"""

from pymatgen.core.structure import Structure
import os

# function to make a supercell
def make_supercell(file, expansion = [2,2,2]):
    # setup structure
    st = Structure.from_file(file)
    # create supercell
    st.make_supercell(expansion)
    # make a supercell folder in the directory if it doesn't exist
    new_loc = 'supercell/'
    if not os.path.exists(new_loc):
        os.mkdir(new_loc)
    # save supercell
    st.to('POSCAR', new_loc+'POSCAR')
    
if __name__ == '__main__':
    file = 'POSCAR_SURF_00' 
    expansion = [2,2,1]
    make_supercell(file, expansion)
    