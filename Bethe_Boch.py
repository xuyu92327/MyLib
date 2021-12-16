import numpy as np

def dE_over_dx(P,m,z=1, Z=7, A=13):
    '''
    This is a function to calculate dE/dx value with Bethe-Boch formular
    Here you need to provide at least 2 values:
    P: The momentum of the incident particle          unit: MeV
    m: The rest mass of the incident particle         unit: MeV
    z: The charge of the incident particle 
    Z: The proton number of the material particle(s)
    A: Total nucleon number of the material particle(s)
    '''
    k = 0.3071
    E_2 = P**2+m**2
    gamma_2 = E_2/m**2
    beta_2 = (gamma_2-1)/gamma_2
    Tmax = 0.225
    I = 12.4e-6*Z
    term1 = k*z**2*(Z/A)/beta_2
    term2 = 0.5*np.log(2*0.511*(gamma_2-1)*Tmax/I**2)
    term3 = term2-beta_2
    result = term1*term3
    return result
