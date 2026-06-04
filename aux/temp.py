import numpy as np

for _ in range(10):
    U = np.random.uniform(0, 0.25)
    print(f'{2 + 2 * np.sqrt(U)}')
