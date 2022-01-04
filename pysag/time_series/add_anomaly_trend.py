# %%
import numpy as np

# %%
# TODO: random_walk
def add_anomaly_trend(time_series, start, end, slope, noise=0, seed=None):
    time_series = np.array(time_series)
    if seed:
        np.random.seed(seed)
    for i in range(start, end):
        time_series[i::] += np.random.random() * slope 
        time_series[i] += (np.random.random() - 0.5) * noise
    return time_series

# %%
