# Band.py module for VASP with vaspkit

A module to plot the bandstructure from a VASP DFT calculation. It requires
a postprocessing from vaspkit. Using vaspkit 211 option one can generate the
BANDS.py and KLABLES (and some other files) files. 

An example of the usage is shown for silicon. The vaspkit generated `BAND.dat`
and `KLABELS` are given. The `plot_band.py` uses the `Bands.py` module to plot
the bands. The bandstructure plotted is saved as `silicon.png`.

It is just a simple plot program, which one can easily write everytime when one
wants to plot. I plot bandstructures very often, so I wrote this module to save
me some time.

> **Note**:
> Make sure you have given the label for each high symmetry points in `KPOINTS`
> file of VASP. Otherwise vaspkit will identify them as 'Undefined' in `KLABELS`.
> (You can manually edit the `KLABELS` file also to include labels.)
