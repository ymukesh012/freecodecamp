


"""Question_1: Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix."""

import numpy as np
def calculate(input_lst):
    if len(input_lst)!=9:
        raise ValueError("List must contain nine numbers.") 
        return
    matrix=np.array(input_lst).reshape(3, 3)
    calculations={
    'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(),matrix.mean().item()],
    'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(),matrix.var().item()],
    'standard deviation':[matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(),matrix.std().item()],
    'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(),matrix.max().item()],
    'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(),matrix.min().item()],
    'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(),matrix.sum().item()]
    }
    return calculations
print(calculate([0,1,2,3,4,5,6,7,8]))


