#-------------------------------------------------Packages-------------------------------------------------#
import numpy as np

#-------------------------------------------------Function-------------------------------------------------#
def rho_gen_gauss(I:list[list[float]])->float:
    std_gauss = np.std(np.abs(I))
    mean_abs = np.mean(np.abs(I))
    
    rho = std_gauss / (mean_abs + 0.0000001)
    
    retrun rho