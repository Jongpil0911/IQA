#-------------------------------------------------Packages-------------------------------------------------#
import numpy as np
import cv2
from skimage.util import view_as_blocks

#-------------------------------------------------Packages-------------------------------------------------#
from Rho_dct import rho_dct



#-------------------------------------------------Function-------------------------------------------------#
def feature_extraction(img:list[list[uint8]])->list[list[float]]:
    gaussian = cv2.getGaussianKernel(3, -1)
    h = gaussian * gaussian.T
    
    Img = np.double(img[:, :, 1])
    
    blockSize = (3, 3)
    stride = (1, 1)
    blocks = view_as_windows(Img, blockSize, step=stride)
    
    coeff_freq_var_L1 = np.array([[rho_dct(block) for block in row] for row in blocks])
    gama_L1 = np.array([[rho_dct(block) for block in row] for row in blocks])
    
    
    
    
    
    
    
#-------------------------------------------------Packages-------------------------------------------------#
#-------------------------------------------------Function-------------------------------------------------#