from builtins import str
from builtins import range
import pytest
import supereeg as se
import numpy as np
import os
import nibabel as nib

# downsample locations
locs = se.load('example_locations')[0::17]
n_samples = 10
n_subs = 3
n_elecs = 10
data = [se.simulate_model_bos(n_samples=10, sample_rate=10, locs=locs,
                              sample_locs = n_elecs) for x in range(n_subs)]
test_bo = data[0]
test_model = se.Model(data=data, locs=locs)

def test_load_example_data():
    bo = se.load('example_data')
    assert isinstance(bo, se.Brain)

def test_load_example_model():
    model = se.load('example_model')
    assert isinstance(model, se.Model)

def test_load_example_locations():
    locs = se.load('example_locations')
    assert isinstance(locs, np.ndarray)

def test_load_nifti():
    nii = se.load('example_nifti')
    assert isinstance(nii, nib.nifti1.Nifti1Image)

# # this makes the test super long, from 5 secs to 73 secs
#
# def test_load_pyFR_k10r20_6mm():
#     bo = se.load('pyFR_k10r20_6mm')
#     assert isinstance(bo, se.Model)

def test_load_pyFR_union():
    data = se.load('pyFR_union')
    assert isinstance(data, np.ndarray)

def test_load_mini_model():
    bo = se.load('gray_mask_20mm_brain')
    assert isinstance(bo, se.Brain)

def test_load_gray_mask_6mm_brain():
    bo = se.load('gray_mask_6mm_brain')
    assert isinstance(bo, se.Brain)

def test_bo_load(tmpdir):
    p = tmpdir.mkdir("sub").join("example")
    test_bo.save(fname=p.strpath)
    bo = se.load(os.path.join(p.strpath + '.bo'))
    assert isinstance(bo, se.Brain)

def test_mo_load(tmpdir):
    p = tmpdir.mkdir("sub").join("example")
    test_model.save(fname=p.strpath)
    bo = se.load(os.path.join(p.strpath + '.mo'))
    assert isinstance(bo, se.Model)

def test_nii_load(tmpdir):
    p = tmpdir.mkdir("sub").join("example")
    test_bo.to_nii(filepath=p.strpath)
    bo = se.load(os.path.join(p.strpath + '.nii'))
    assert isinstance(bo, se.Brain)
