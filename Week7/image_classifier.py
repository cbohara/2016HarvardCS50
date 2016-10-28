import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

# the digits dataset contains 1797 images representing handwritten digits
digits = datasets.load_digits()
# each element in the array digits.images is on its own a 8 by 8 array of pixels,
# where each pixel is an integer between 0 and 16
print(digits.images[0])

plt.figure()
plt.imshow(digits.images[0], cmap = plt.cm.gray_r, interpolation = 'nearest')
plt.show()

# extract subset from original dataset
x_train = digits.data[0:10]
y_train = digits.target[0:10]

# run nearest neighbor classifier using test data point
x_test = digits.data[345]

plt.figure()
plt.imshow(digits.images[345], cmap = plt.cm.gray_r, interpolation = 'nearest')
plt.show()

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

# Machine Learning algorithms improve their performance with the amount of training data they are exposed to
x_train = digits.data[0:1000]
y_train = digits.data[0:1000]
# now we run the same code as above to count the errors the algorithm commits over the same test set
num = len(x_train)
no_errors = 0
distance = np.zeros(num)
for j in range(1697, 1797):
    x_test = digits.data[j]
    for i in range(num):
        distance[i] = dist(x_train[i], x_test)
    min_index = np.argmin(distance)
    if y_train[min_index] != digits.target[j]:
        no_errors += 1
print(no_errors)
