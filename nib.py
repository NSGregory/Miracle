# Example
# import nibabel as nib
# data = nib.load('mydata.nii.gz').get_data()

import nibabel as nib
import numpy as np
filename = "/SSD2/Nick_G/KNK_sample2_decent/niftis_original_and_fixed_with_slicer/niftis_original/mouse1L_Lhemi_02x_down_autofl_chan.nii.gz"
data = nib.load(filename).get_data()
