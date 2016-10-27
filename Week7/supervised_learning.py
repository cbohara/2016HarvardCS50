import numpy as np
import matplotlib.pyplot as plot

# define numpy array of 2-dimensional points for training data
x_train = np.array([[1,1], [2,2.5], [3,1.2], [5.5,6.3], [6,9], [7,6]])
y_train = ['red', 'red', 'red', 'blue', 'blue', 'blue']

# create plot with training data
plot.figure()
plot.scatter(x_train[:,0], x_train[:,1], s = 170, color = y_train[:])
plot.show()

# create test point
x_test = np.array([3,4])

# add test point
plot.figure()
plot.scatter(x_train[:,0], x_train[:,1], s = 170, color = y_train[:])
plot.scatter(x_test[0], x_test[1], s = 170, color = 'green')
plot.show()

# calculate Euclidean distance (straight-line distance between 2 points)
def dist(x,y):
    return np.sqrt(np.sum((x - y)**2))

num = len(x_train)
# initialize a numpy array filled with zeros
distance = np.zeros(num)
# compute the distance from the test value to each training value and store into an output array
for i in range(num):
    distance[i] = dist(x_train[i], x_test)
print(distance)
