#-------------------------------------------------Packages-------------------------------------------------#
import pack

#-------------------------------------------------Function-------------------------------------------------#
def gama_gen_gauss(I:list[list[float]])->float:
    mean_gauss = np.mean(I)
    var_gauss = np.var(I)
    mean_abs = np.mean(np.abs(I) - mean_gauss) ** 2
    rho = var_gauss / (mean_abs + 0.0000001)
    
    g = np.arange()
    
    
if __name__ == "__main __":
    x = [1, 2, 3, 4]
    
    plt.figure()
    plt.plot(x, x**2)
    plt.show()