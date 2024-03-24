import numpy as np

def calculate(list):
    nparray = np.array(list)
    matrix = nparray.reshape((3,3))

    mean0 = matrix.mean(0)
    mean1 = matrix.mean(1)


    return mean1
    #calculations