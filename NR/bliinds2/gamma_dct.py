#-------------------------------------------------Packages-------------------------------------------------#
from scipy.fftpack import dct

#-------------------------------------------------Packages-------------------------------------------------#
from gamma_gen_gauss import gama_gen_gauss

#-------------------------------------------------Function-------------------------------------------------#
def gama_dct(I:list[list[float]])->float:
    temp1 = dct(dct(I.T, norm="ortho").T, norm-"ortho")
    
    temp2 = temp1.flatten()
    
    temp3 = temp2[1:]
    
    g = gama_gen_gauss(temp3)
    
    return g