
# import modules

from subprocess import check_output  # calling bash


# -----------------------------------------------------
# extracting propagators

def extract_propagators(path_results, measurement, particles, single_conf=0, single_t_slice=0):
    """
    extract propagators for a given measurement, and particles
    arguments : path_results - path to result folder
                measurements - type of measurement
                particles    - list of particles (always as a list)
                single_conf (optional)    - if = 1, only one configuration
                single_t_slice (optional) - if = 1, only one time slice
    
    output is a tuple of a format    (
                                     [particle]
                                     [configuration]
                                     [measurements within one configuration (various source positions,
                                                                             for example)]
                                     [propagator itself as a complex number]
                                     ,
                                     list of particles, list of configurations
                                     )
    """
    particles_in=[par for par in particles]
    
    configurations = [name for name in check_output(["ls",path_results]).split("\n")[:-1]]
    if single_conf:
      configurations=[configurations[0]]

    folder_paths=[path_results+conf+"/"+measurement+"/" for conf in  configurations]

    for particle in particles:
      for con,folder_con in enumerate(folder_paths):
        if particle not in check_output(["ls",folder_con]):
          print "ERROR, particle", particle, "not in", configurations[con]
          print "       continue without", particle
          particles_in.remove(particle)
          break
          if len(particles_in)==0:
            print "ERROR, not enough particles to work with"
            return -1

          
    particle_paths=[
                    [
                     [folder_con+name for name in check_output(["ls",folder_con]).split("\n")[:-1]
                       if particle in name]
                     for folder_con in folder_paths] 
                    for particle in particles_in]
    if single_t_slice:
      particle_paths=[
                       [[slices[0]] for slices in confs]
                     for confs in particle_paths] 
                    
    
    propagators_all=[
                     [
                      [
                       read_propagator(particle_paths[particle][conf][prop])  
                         for prop in range(len(particle_paths[particle][conf]))]
                     for conf in range(len(particle_paths[particle]))]
                    for particle in range(len(particle_paths))]
                   
    return (propagators_all, particles_in, configurations)
    


# -----------------------------------------------------
# reading from file

def read_propagator(file_path):
    """
    read propagator from a file at file_path
    """
    return [complex(float(line.split('\t')[1].split(' ')[0]),float(line.split('\t')[1].split(' ')[1]))
            for line in open(file_path,'rb').readlines()
           ]
             
             
             
             
             
             
# -----------------------------------------------------
# footer
             
if __name__ == "__main__":
    print "module containing I/O functions"            

