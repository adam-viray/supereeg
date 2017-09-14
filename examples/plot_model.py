# -*- coding: utf-8 -*-
"""
=============================
Load and plot a model
=============================

Here we load the example model, and then plot it.

"""

# Code source: Andrew Heusser & Lucy Owen
# License: MIT

# import
import superEEG as se

# load example data
model = se.load('example_model')

# plot it
model.plot(xticklabels=False, yticklabels=False)