import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

"""
In Unsupervised Learning, algorithms are trained with unlabeled data.

Here the machine (i.e., the algorithm) is expected to derive structure from the
data on its own, without the presence of labels that can guide the process as in
Supervised Learning.

A typical application of Unsupervised Learning is clustering, i.e., the task of
grouping the data into k categories, where k can be given be the user or
inferred directly by the algorithm.
"""

# define numpy array of 2-dimension points
x = np.array([[1,1], [2,2.5], [3,1.2], [5.5,6.3], [6,9], [7,6], [8,8]])
plt.figure()
plt.scatter(x[:,0], x[:,1], s = 170, color = 'black')
# let us stress once again that this collection of points is unlabelled. our job now is to cluster these points!
plt.show()

# lets start with 2 clusters
k = 2
# KMeans divides the data points into k clusters
kmeans = KMeans(n_clusters = k)
kmeans.fit(x)

# get centroids coordinates (central point of triangle configuration from plt points) for each cluster
centroids = kmeans.cluster_centers_
# get labels assigned to each data
labels = kmeans.labels_
# specify colors to label the different clusters
colors = ['r.', 'g.']
plt.figure()
for i in range(len(x)):
    plt.plot(x[i,0], x[i,1], colors[labels[i]], markersize = 30)
plt.scatter(centroids[:,0], centroids[:,1], marker = "x", s = 300, linewidth = 5)
plt.show()

# now lets split into 3 clusters
k = 3
kmeans = KMeans(n_clusters = k)
kmeans.fit(x)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_
colors = ['r.', 'g.', 'b.']
plt.figure()
for i in range(len(x)):
    plt.plot(x[i,0], x[i,1], colors[labels[i]], markersize = 30)
plt.scatter(centroids[:,0], centroids[:,1], marker = "x", s = 300, linewidth = 5)
plt.show()
