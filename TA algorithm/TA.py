import TS
import Mix 
# Given mixture design matrix Mix
Mix = Mix_0
D_fll = generate_full_design(Mix)
def TA (m,D_full,n,n_i,f):
    ts = generate_threshold_sequence(m,n,D_full,n_i,f)

    
