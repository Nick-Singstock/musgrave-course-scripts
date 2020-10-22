#!/usr/bin/env python
"""
Created on Thu Oct 22 10:43:02 2020

@author: NSing
"""

# import the Vasprun class from the outputs script in the pymatgen/io/vasp/ folder
from pymatgen.io.vasp.outputs import Vasprun, Outcar

# **********
# Choose whether to print optional outputs
print_electronic = True
print_magnetic = True
make_dosplot = True
dos_smearing = 0.02
# **********

# create an instance of a Vasprun object
vsp = Vasprun('./vasprun.xml')

# print whether ionic and electronic convergene was achieved
print('Ionic Convergence:', vsp.converged_ionic)
print('Electronic Convergence:', vsp.converged_electronic)
assert vsp.converged_ionic and vsp.converged_electronic, 'ERROR: Structure is not converged!'

# print final energy
print('Total Energy:', vsp.final_energy)

# make a band structure object
bs = vsp.get_band_structure('KPOINTS', efermi=vsp.efermi)

# if print_electronic is set to False, the following items will not be printed
if print_electronic:    
    # print properties of the band structure
    print("Number of bands:", bs.nb_bands)
    print("Number of kpoints:", len(bs.kpoints))
    print("Efermi: %.4f" % bs.efermi)
    print('Is Metal:', bs.is_metal())
    
    # print band gap
    bg = bs.get_band_gap()
    print('Band Gap:', bg['energy'])
    print('Direct Band Gap:', bg['direct'])

if print_magnetic:
    # read in magentic moment from OUTCAR and print
    out = Outcar('./OUTCAR')
    print('Total Magnetic Moment:', out.total_mag)
    
if make_dosplot:
    # read in BSDOSPlotter function to plot DOS and BS
    from pymatgen.electronic_structure.plotter import DosPlotter
    
    # make and save a plot of the band structure and DOS
    dos = vsp.complete_dos
    energy_range = (-10, 7) # eV, change if desired to change plotting range

    # create DosPlotter object with smearing  
    edosplot = DosPlotter(sigma=dos_smearing)
    # plot Total DOS and element-projected dos
    edosplot.add_dos("Total DOS", dos)
    edosplot.add_dos_dict(dos.get_element_dos())
    plt = edosplot.get_plot(xlim=energy_range) 
    plt.plot((-20,20), (0,0), 'k--')
    plt.savefig('Element_DOS_plot.png')

    # create DosPlotter object with smearing 
    odosplot = DosPlotter(sigma=dos_smearing)
    # plot Total DOS and orbital-projected dos
    odosplot.add_dos("Total DOS", dos)
    odosplot.add_dos_dict(dos.get_spd_dos())
    plt = odosplot.get_plot(xlim=energy_range) 
    plt.plot((-20,20), (0,0), 'k--')
    plt.savefig('Orbital_DOS_plot.png')

    print('Generated DOS plots')
