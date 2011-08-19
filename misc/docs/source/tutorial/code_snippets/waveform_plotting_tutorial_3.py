from obspy.core import read

threechannels = read('http://examples.obspy.org/COP.BHE.DK.2009.050')
threechannels += read('http://examples.obspy.org/COP.BHN.DK.2009.050')
threechannels += read('http://examples.obspy.org/COP.BHZ.DK.2009.050')
threechannels.plot(size=(800, 600))
