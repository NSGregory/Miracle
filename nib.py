# Example
# import nibabel as nib
# data = nib.load('mydata.nii.gz').get_data()

import nibabel as nib
import numpy as np
filename = ("C:/users/gregoryn/Desktop/minimal.nii.gz")
data = nib.load(filename).get_data()
