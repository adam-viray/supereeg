# -*- coding: utf-8 -*-
"""
=============================
Create a model from scratch, and then update it with new subject data
=============================

In this example, we will simulate a model and some data, and see if we can
recover the model from the data. First, we'll load in some example locations.
Then, we will simulate correlational structure (a toeplitz matrix) to impose on
our simulated data.  This will allow us to test whether we can recover the
correlational structure in the data, and how that changes as a function of the
number of subjects in the model. Then, we will simulate 10 subjects and create
brain objects with their data.  The left figure shows the model derived from
10 simulated subjects.  Finally, we simulate 10 additional subjects and use the
model.update method to update an existing model with new data. On the right, the
updated model is plotted. As is apparent from the figures, the more data in the
model, the better the true correlational structure can be recovered.

"""

# Code source: Andrew Heusser & Lucy Owen
# License: MIT

# import libraries
import os
import scipy
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import superEEG as se

# load example model to get locations
locs = se.load('example_locations')

# simulate correlation matrix
R = scipy.linalg.toeplitz(np.linspace(0,1,len(locs))[::-1])

# number of timeseries samples
n_samples = 1000

# number of subjects
n_subs = 10

# number of electrodes
n_elecs = 20

data = []

# loop over simulated subjects
for i in range(n_subs):

    # for each subject, randomly choose n_elecs electrode locations
    p = np.random.choice(range(len(locs)), n_elecs, replace=False)

    # generate some random data
    rand_dist = np.random.multivariate_normal(np.zeros(len(locs)), np.eye(len(locs)), size=n_samples)

    # impose R correlational structure on the random data, create the brain object and append to data
    data.append(se.Brain(data=np.dot(rand_dist, scipy.linalg.cholesky(R))[:,p], locs=pd.DataFrame(locs[p,:], columns=['x', 'y', 'z'])))

# create the model object
model = se.Model(data=data, locs=locs)

new_data = []

# loop over simulated subjects
for i in range(n_subs):

    # for each subject, randomly choose n_elecs electrode locations
    p = np.random.choice(range(len(locs)), n_elecs, replace=False)

    # generate some random data
    rand_dist = np.random.multivariate_normal(np.zeros(len(locs)), np.eye(len(locs)), size=n_samples)

    # new brain object
    new_data.append(se.Brain(data=np.dot(rand_dist, scipy.linalg.cholesky(R))[:,p], locs=pd.DataFrame(locs[p,:], columns=['x', 'y', 'z'])))

# update the model
new_model = model.update(new_data)

# initialize subplots
f, (ax1, ax2) = plt.subplots(1, 2)

# plot it and set the title
model.plot(ax=ax1, yticklabels=False, xticklabels=False, cmap='RdBu_r', cbar=True, vmin=0, vmax=1)
ax1.set_title('Before updating model: 10 subjects total')

# plot it and set the title
new_model.plot(ax=ax2, yticklabels=False, xticklabels=False, cmap='RdBu_r', cbar=True, vmin=0, vmax=1)
ax2.set_title('After updating model: 20 subjects total')

sns.plt.show()
