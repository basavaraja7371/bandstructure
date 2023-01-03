# Band.py module for VASP with vaspkit

A module to plot the bandstructure from a VASP DFT calculation. It requires
a postprocessing from vaspkit. Using vaspkit 211 option one can generate the
BANDS.py and KLABLES (and some other files) files. Using 213 option projected
band data are printed as PBAND_XX.dat.

An example of the usage is shown for silicon. The vaspkit generated `BAND.dat`
and `KLABELS` are given. The `plot_band.py` uses the `Bands.py` module to plot
the bands. The bandstructure plotted is saved as `silicon.png`.

It is just a simple plot program, which one can easily write everytime when one
wants to plot. I plot bandstructures very often, so I wrote this module to save
me some time.

> **Note**:
> 1. Make sure you have given the label for each high symmetry points in `KPOINTS`
> file of VASP. Otherwise vaspkit will identify them as 'Undefined' in `KLABELS`.
> (You can manually edit the `KLABELS` file also to include labels.)
> 2. The bandfile name should be given as a list of lists.
> 3. In case of just band plotting bandfiles=[["BAND.dat"]]
> 4. In case of projected bands bandfiles = [["PBAND_XX.dat", "s", "p", "etc"], ["PBAND_yy.dat", "s", "p_z", "etc"]]
> 5. The orbitals should be specified only as follows 's', 'p_y', 'p_z', 'p_x', 'd_{xy}', 'd_{yz}', 'd_{z^2}', 'd_{xz}' and 'd_{x^2-y^2}'

> **Warning**:
> The legends of the projected bands are not yet complete.
