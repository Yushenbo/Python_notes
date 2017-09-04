#-*- coding:utf-8 -*-
#########################################################################
# File Name: signalFilter.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import scipy.signal as signal
import numpy as np
import pylab as pl

# Sample freqence 8kHz
sampling_rate = 8000.0

def main():

    b, a = signal.iirdesign([0.2, 0.5], [0.1, 0.6], 2, 40)

    w, h = signal.freqz(b, a)

    power = 20 * np.log10(np.clip(np.abs(h), 1e-8, 1e100))

    #draw
    pl.subplot(211)
    pl.plot(w/np.pi * 4000, power)
    pl.title(u'freqz calculated')
    pl.ylim(-100, 20)
    pl.ylabel(u'Gain(dB)')

    
    t = np.arange(0, 2, 1/sampling_rate)
    sweep = signal.chirp(t, f0 = 0, t1 = 2, f1 = sampling_rate/2)
    
    #Filtering
    out = signal.lfilter(b, a, sweep)

    #Convert the freqency to energy
    out = 20 * np.log10(np.abs(out))

    index = np.where(np.logical_and(out[1:-1] > out[:-2], out[1:-1] > out[2:]))[0] + 1

    #drwa
    pl.subplot(212)
    pl.plot(t[index]/2.0 * 4000, out[index])
    pl.title(u'Frequency spectrum')
    pl.ylim(-100, 20)
    pl.ylabel(u'Gain(dB)')
    pl.xlabel(u'Freq(Hz)')

    pl.subplots_adjust(hspace = 0.3)
    pl.show()
main()
