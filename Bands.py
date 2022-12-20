# Importing numpy and pyplot

import numpy as np
import matplotlib.pyplot as plt

class Bands:
    def __init__(self, name, bandfile, klabelfile, num_kpt):
        self.name = name
        self.bandfile = bandfile
        self.klabelfile = klabelfile
        self.num_kpt = num_kpt

    def k_points(self):
        kpoint= np.loadtxt(self.klabelfile, dtype='str', skiprows=1, max_rows=self.num_kpt)
        klabel = list(kpoint[:,0])

        temp = [0]*self.num_kpt
        for i,label in enumerate(klabel):
            if label=='G' or label=='GAMMA' or label=='Gamma' or label=='gamma':
                l='$\Gamma$'
                temp[i] = l
            else:
                temp[i]=label
        klabel = temp


        kvalue = np.asarray(kpoint[:,1], dtype=float)
        return kvalue, klabel

    def get_k_info(self):
        kvalue, klabel = self.k_points()
        print( "------------------------")
        print(f" Label           Kpoint")
        print( "------------------------")

        for value, label in zip(kvalue, klabel):
            print(f"   {label:8}      {value:.4f}")

        print( "------------------------")


    def bands_plot(self, ymin=-2, ymax=2, color='red', linewidth='1', image_format='png'):
        kvalue, klabel = self.k_points()
        band_data = np.loadtxt(self.bandfile)
        k_point = band_data[:,0]
        energy = band_data[:,1]

        fig, ax = plt.subplots()

        ax.set_ylim(ymin, ymax)
        ax.set_ylabel("$E-E_F$ (eV)", fontsize=20)

        ax.set_xlim(kvalue[0], kvalue[-1])
        ax.set_xticks(kvalue)
        ax.set_xticklabels(klabel, fontsize=18)

        ax.grid()

        ax.plot(k_point, energy,linewidth=linewidth, color=color)

        plt.tight_layout()

        if image_format=='eps':
            plt.savefig(self.name+'.eps')
        else:
            plt.savefig(self.name+'.png', dpi=200)

def read_klabels(self, klabels):
    self.klabels, self.kpoints = np.loadtxt('KLABELS')

