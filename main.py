# Get the column names of a NumPy ndarray in Python

import numpy as np

data = np.genfromtxt(
    'employees.txt',
    names=True,
    encoding='utf-8',
    delimiter=',',
    dtype=None,
)

# [('Alice', 'Smith', '2023-01-05') ('Bobby', 'Hadz', '2023-03-25')
print(data)

# ('first_name', 'last_name', 'date')
print(data.dtype.names)