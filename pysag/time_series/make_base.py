# %%
import numpy as np


# %%
def make_base(
    length=100, 
    min_start=0, 
    max_start=0,
    diff=1,
    seed=None
    ):

    if seed:
        np.random.seed(seed)

    stream = np.empty(length)
    start = np.random.uniform(min_start, max_start)
    stream[0] = start

    for i in range(1,length):
        stream[i] = stream[i-1] +  np.random.uniform(-1,1) * diff
    return stream
    
# %%

# %%

# %%
