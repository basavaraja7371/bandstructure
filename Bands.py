"""
Bands.py
--------

A module to plot the bandstructure from a VASP DFT calculation. It requires a
postprocessing from vaspkit. Using vaspkit 211 option one can generate the
BANDS.py and KLABLES (and some other files) files. It is just a simple plot
program, which one can easily write everytime when one wants to plot. I plot
bandstructures very often, so I wrote this module to save me some time.
"""

# Importing numpy and pyplot

import numpy as np
import matplotlib.pyplot as plt

class Bands:

    def __init__(self, name, bandfile, klabelfile, num_kpt):
        """ The string name is the name you want to call the plot. The output
        band figure will have this name. bandfile is a bandstructure data file.
        Vaspkit produces BAND.dat file. klabelfile is KLABELS file created by
        vaspkit. num_kpt is an interger value which is the number of symmtry
        points considered to plot the bandstructure."""
        self.name = name
        self.bandfile = bandfile
        self.klabelfile = klabelfile
        self.num_kpt = num_kpt

    def k_points(self):
        """The k_points method reads the klabelsfile and write to a numpy
        array. Be aware that the first line in the file is neglected. Also
        make sure that you have given the right num_kpt value. num_kpt
        should be equal to the number of rows in the kalbelfile. """

        # Reads the file, skips the first row, and reads num_kpt lines.
        klabels= np.loadtxt(self.klabelfile, dtype='str', skiprows=1,
                          max_rows=self.num_kpt)

        labels = list(klabels[:,0])


        # Changing G, Gamma, GAMMA, gamma strings to LaTeX $\Gamma$.
        temp = [0]*self.num_kpt
        for i,label in enumerate(labels):
            if label in ['g', 'G', 'gamma', 'Gamma', 'GAMMA']:
                l='$\Gamma$'
                temp[i] = l
            else:
                temp[i]=label
        labels = list(temp)
        kpoints = np.asarray(klabels[:,1], dtype=float)

        return kpoints, labels

    def get_k_info(self):
        """ Prints symmetry point information"""

        kvalue, klabel = self.k_points()
        print( "------------------------")
        print(f" Label           Kpoint")
        print( "------------------------")

        for value, label in zip(kvalue, klabel):
            print(f"   {label:8}      {value:.4f}")

        print( "------------------------")


    def bands_plot(self,ymin=-2,ymax=2,color='red',linewidth=1,save_as='png'):
        """ This module plots the bands. ymin and ymax are to set the energy
        range for the plots. color and linewidth are color and linewidth for the
        plot. image_format takes strings 'png' or 'eps' and saves the
        bandstructure figure as 'name.png' or 'name.eps'."""
        kvalue, klabel = self.k_points()
        band_data = np.loadtxt(self.bandfile)
        k_point = band_data[:,0]
        energy = band_data[:,1]

        fig, ax = plt.subplots(figsize=(9,7))

        plt.ylim(ymin, ymax)
        ax.set_ylim(ymin, ymax)
        ax.set_ylabel("$E-E_F$ (eV)", fontsize=20)

        ax.set_xlim(kvalue[0], kvalue[-1])
        ax.set_xticks(kvalue)
        ax.set_xticklabels(klabel, fontsize=18)

        ax.grid()

        ax.plot(k_point, energy,linewidth=linewidth, color=color)

        plt.tight_layout()

        if save_as=='eps':
            plt.savefig(self.name+'.eps')
        else:
            plt.savefig(self.name+'.png', dpi=200)


