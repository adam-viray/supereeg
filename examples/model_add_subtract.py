from __future__ import print_function
#from builtins import range
import supereeg as se
import numpy as np
import scipy
import pytest

# some example locations

locs = np.array([[-61., -77.,  -3.],
                 [-41., -77., -23.],
                 [-21., -97.,  17.],
                 [-21., -37.,  77.],
                 [-21.,  63.,  -3.],
                 [ -1., -37.,  37.],
                 [ -1.,  23.,  17.],
                 [ 19., -57., -23.],
                 [ 19.,  23.,  -3.],
                 [ 39., -57.,  17.],
                 [ 39.,   3.,  37.],
                 [ 59., -17.,  17.]])


# number of timeseries samples
n_samples = 10
# number of subjects
n_subs = 6
# number of electrodes
n_elecs = 5
# simulate correlation matrix
data = [se.simulate_model_bos(n_samples=10, sample_rate=10, locs=locs, sample_locs = n_elecs) for x in range(n_subs)]

mo1 = se.Model(data=data[0:3], locs=locs)
mo2 = se.Model(data=data[3:6], locs=locs)

mo3 = mo1 + mo2

mo3.n_subs == mo1.n_subs + mo2.n_subs

mo2_recon = mo3 - mo1

np.allclose(mo2.numerator.real, mo2_recon.numerator.real)
np.allclose(mo2.numerator.imag, mo2_recon.numerator.imag)
np.allclose(mo2.denominator, mo2_recon.denominator)




