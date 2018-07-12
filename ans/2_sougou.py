import math

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

N = 10000

# %% (1)
x = np.random.uniform(0.0, 1.0, N)
y = np.random.uniform(0.0, 1.0, N)

# %% (2)
is_inside = np.sqrt(x**2 + y**2) < 1
cnt = np.sum(is_inside)

plt.figure(figsize=(6, 6))
plt.scatter(x[is_inside], y[is_inside], marker='.')
plt.scatter(x[~is_inside], y[~is_inside], marker='x')
plt.show()

# %% (3)
pi_pred = 4 * cnt / N
print(pi_pred)
