import scipy as sp
import numpy as np
import matplotlib.pyplot as plot
from sklearn import datasets

# the digits dataset contains 1797 images representing handwritten digits
digits = datasets.load_digits()
# each element in the array digits.images is on its own a 8 by 8 array of pixels,
# where each pixel is an integer between 0 and 16
print(digits.images[0])

plot.figure()
plot.imshow(digits.images[0], cmap = plot.cm.gray_r, interpolation = 'nearest')
plot.show()

# extract subset from original dataset
x_train = digits.data[0:10]
y_train = digits.target[0:10]

# run nearest neighbor classifier using test data point
x_test = digits.data[345]

plot.figure()
plot.imshow(digits.images[345], cmap = plot.cm.gray_r, interpolation = 'nearest')
plot.show()

# calculate Euclidean distance (straight-line distance between 2 points)
def dist(x,y):
    return np.sqrt(np.sum((x - y)**2))

# compute the distance between each training value and the test value and store in the distance array
num = len(x_train)
distance = np.zeros(num)
for i in range(num):
    distance[i] = dist(x_train[i], x_test)

# get the index value of the minimum distance value
min_index = np.argmin(distance)
print(y_train[min_index])
