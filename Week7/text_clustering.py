import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

"""
Unsupervised learning example

Text content will be split into most-similar clusters.

First, we build a vocabulary from the words used in the text, when we do
not consider the so-called "stop words" such as "a," "the," or "in," as they do
not convey meaningful information.

For each text instance we count the number of occurrences of each word and store it into a matrix.
In the matrix, each row represents a text instance and each column represents a word.
"""

sentences = ['I love CS50. Staff is awesome, awesome, awesome!',
            'I have a dog and a cat.',
            'Best of CS50? Staff. And cakes. Ok, CS50 staff.',
            'My dog keeps chasing my cat. Dogs!']

# create the bag-of-words matrix
count_vector = Count_Vectorizer(stop_words= 'english')
x = vectorizer.fit_transform(sentences)
x.todense()

# define the number of clusters
k = 2
# define the proper notation of distance to deal with the sentences
dist = 1 - cosine_similarity(x)
# run the algorithm KMeans
model = KMeans(n_clusters = k)
model.fit(x)
