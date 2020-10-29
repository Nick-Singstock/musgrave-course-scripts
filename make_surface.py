#!/usr/bin/env python
"""
Created on Wed Oct  2 10:14:24 2019

@author: Nick Singstock
"""

# Import the neccesary tools to generate surfaces
from pymatgen.core.surface import SlabGenerator, Structure


def make_surface(file, facet = (1,1,1), verbose = True):
    # read in structure
    st = Structure.from_file(bulk_file)
    # generate slabs with the given facet
    slabgen = SlabGenerator(st, facet, 6, 16, center_slab=True)
    all_slabs = slabgen.get_slabs(symmetrize = True) 
    if verbose:
        print("The slab has %s termination." %(len(all_slabs)))
    # save surfaces
    for i, slab in enumerate(all_slabs):
        slab.to('POSCAR', 'POSCAR_SURF_'+str(i).zfill(2))

if __name__ == '__main__':
    bulk_file = 'POSCAR'
    facet = (1,1,1)
    make_surface(bulk_file, facet)
