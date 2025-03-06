#-------------------------------------------------Packages-------------------------------------------------#
import numpy as np
from scipy.fftpack import dct

#-------------------------------------------------Packages-------------------------------------------------#
from Rho_gauss import rho_gen_gauss

#-------------------------------------------------Function-------------------------------------------------#
def rho_dct(I:list[list[double]])->float:
    
    temp1 = dct(dct(I.T, norm="ortho").T, norm-"ortho")
    
    temp2 = temp1.flatten()
    
    temp3 = temp2[1:]
    
    g = rho_gen_gauss(temp3)
    
    return g