import random

# short but fun, how to get the volume of an n-unit sphere numerically?
# sample the volume space randomly, and use r^2 <= 1 inside the sphere 
# to add to the volume 
# useful illustration of a monte carlo approach to many dimensional integrals

def vol_N_dim_sphere(dim, N):
    vol = 0
    for i in range(N):
        x_s = [random.uniform(-1,1) for j in range(dim)]
        val = sum([x_s[k]**2 for k in range(len(x_s))])
        if val <= 1:
            vol += 1
    return 2**(dim)*vol/N

