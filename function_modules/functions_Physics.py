
# import modules

import numpy
from cmath import *






# -----------------------------------------------------
# effective mass

def effective_mass(propagator):
    """
    calculate efective mass from the propagator
    """
    len_p=len(propagator)
    output=len_p*[None]
    for i in range(len_p/2-1):
        output[i]=(log(propagator[i]/propagator[i+1])).real
    for i in range(-len_p/2+1,0):
        output[i]=(log(propagator[i+1]/propagator[i])).real
    
    return output
    
  
  
    
    
# -----------------------------------------------------
# footer
             
if __name__ == "__main__":
    print "module containing physics"            
    
