import cv2
import pandas as pd
#import matplotlib.pyplot as plt
#pyplot throws error related to incompatibility with system install

good_file = "/SSD2/Nick_G/KNK_sample2_decent/190808_mouse1L_Rhemi_488_16-50-08/16-50-08_Mouse1L_UltraII_C00_xyz-Table Z0642.ome.tif"

img = cv2.imread(good_file)
#plt.imshow(img)
