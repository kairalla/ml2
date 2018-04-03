import numpy as np
import random
from sklearn import linear_model
from sklearn import metrics

x_train = np.genfromtxt("output.csv", delimiter=",", skip_header=1)
y_train = np.genfromtxt("train.csv", delimiter=",", skip_header=1)

current_column = 1;


def getRow(row, column):
    if row[0] in ids:
        return y_train[ids.index(row[0])][column] >= 0
    return False

x_filtered = filter(lambda z: getRow(z, current_column), x_train)
y_filtered = filter(lambda z: z[current_column] >= 0, y_train)
y_filtered = np.transpose(y_filtered)[current_column]