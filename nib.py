# Example
# import nibabel as nib
# data = nib.load('mydata.nii.gz').get_data()
import matplotlib
matplotlib.use('TkAgg') #explicitly use TkAgg for plotting
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
filename = "/SSD2/Nick_G/KNK_sample2_decent/niftis_original_and_fixed_with_slicer/niftis_original/mouse1L_Lhemi_02x_down_autofl_chan.nii.gz"

pre_slicer_file = ""
post_slicer_file = ""
# nibFile = nib.load(filename) #loads the whole file
# data = nib.load(filename).get_data() # loads file, gives you an array as output, subset of nibFile above
# fData = nibFile.get_fdata()
#
# slice1=fData[int(fData.shape[0]/2), :, :]
# slice2=fData[:, int(fData.shape[1]/2) ,:]
# slice3=fData[:, :, int(fData.shape[2]/2)]
#
# slice_list = [slice1, slice2, slice3]
#show_slices(slice_list)

def show_slices(slices):
    """ Function to display row of image slices """
    fig, axes = plt.subplots(1, len(slices))
    for i, slice in enumerate(slices):
        axes[i].imshow(slice.T, cmap="gray", origin="lower")


def compare_files(file1, file2):
    nibFile1 = nib.load(file1)
    nibFile1Fdata = nibFile1.get_fdata()
    nib1_slice1 = nibFile1Fdata[int(nibFile1Fdata[0], :, :)]
    nib1_slice2 = nibFile1Fdata[:, int(nibFile1Fdata[1], :)]
    nib1_slice3 = nibFile1Fdata[:, :, int(nibFile1Fdata[2])]
    nib1_list = [nib1_slice1, nib1_slice2, nib1_slice3]

    nibFile2 = nib.load(file2)
    nibFile2Fdata = nibFile2.get_fdata()
    nib2_slice1 = nibFile2Fdata[int(nibFile2Fdata[0], :, :)]
    nib2_slice2 = nibFile2Fdata[:, int(nibFile2Fdata[1], :)]
    nib2_slice3 = nibFile2Fdata[:, :, int(nibFile2Fdata[2])]
    nib2_list = [nib2_slice1, nib2_slice2, nib2_slice3]

    shapeTrue = (nibFile1.shape == nibFile2.shape)
    print(f"Shape of file 1 == file 2: {shapeTrue}")

    for key in nibFile1.header.keys()
        result = (nibFile1.header[key]==nibFile2.header[key])
        print(f"{key}: {result}")

    show_slices(nib1_list)
    plt.suptitle("File1")
    show_slices(nib2_list)
    plt.suptitle("File2")

compare_files(pre_slicer_file,post_slicer_file)
