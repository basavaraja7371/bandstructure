import Bands as bnd

# Bandstructure
band = bnd.Bands('silicon', [['BAND.dat']], 'KLABELS', 7)
band.plot_bands(-7, 5, 'blue', 1.5, 'png')

# Projected Bands
pband = bnd.Bands('silicon', [['PBAND_Si.dat',"s", "p_y", "p_x", "p_z"]], 'KLABELS', 7)
pband.plot_projbands(ymin=-5,ymax=5,color='red',linewidth=1,save_as='png')
