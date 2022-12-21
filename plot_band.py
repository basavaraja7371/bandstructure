import Bands as bnd
band = bnd.Bands('silicon', 'BAND.dat', 'KLABELS', 7)
band.bands_plot(-7, 5, 'blue', 1.5, 'png')
