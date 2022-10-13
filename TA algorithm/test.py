import numpy as np

d = np.arange(12).reshape(4,3)
index = np.random.choice(np.arange(d.shape[0]),2,False)
print(d)
print(d[index])