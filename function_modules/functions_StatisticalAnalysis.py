
# import modules

import random
import numpy



# -----------------------------------------------------
# bootstrap et al.

def bootstrap_sample(list_of_elements):
    """
    create bootstrap sample of list of elemets
    """
    n=len(list_of_elements)
    idx=[random.randint(0,n-1) for i in range(n)]
    return [list_of_elements[i] for i in idx] 

# ----------------------

def bootstrap_interval(list_of_results,central_percents=68):
    """
    find the "cetral_percents" interval of confidence
    """
    n=len(list_of_results)
    a=int(n*((100.0-central_percents)/200))
    b=n-a
    sorted_list=sorted(list_of_results)
    
    return (numpy.mean(list_of_results),(sorted_list[a], sorted_list[b]))
    
   

# -----------------------------------------------------
# jackknife at al.

def jackknife_sample(list_of_elements, index):
    """
    create a Jackknife sample of list of elemets
    """
    new_list = [el for el in list_of_elements]
    del new_list[index]
    return new_list

# ----------------------

def jackknife_error(original_mean,list_of_results):
    """
    Jackknife estimate of error
    """
    n=len(list_of_results)
    return (original_mean,numpy.sqrt((n-1.0)/n * sum([(original_mean-mean)**2 for mean in list_of_results])))




# -----------------------------------------------------
# footer
             
if __name__ == "__main__":
    print "library with statistical functions"    
    x=[1,2,3,4,5,6,7,8,9,10]
    print x
    print bootstrap_sample(x)
    print jackknife_sample(x,9)
    
    y=[]
    for i in range(100):
        l=bootstrap_sample(x)
        y.append(1.0*sum(l)/len(l))
    print bootstrap_interval(y)

    yy=[]
    for i in range(len(x)):
        yy.append(numpy.mean(jackknife_sample(x,i)))
    print jackknife_error(numpy.mean(x),yy)
    
    


