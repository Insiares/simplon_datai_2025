## Clustering definition

A clustering algorithm is a method used to group similar objects together based on their characteristics or similarities. It aims to identify patterns or clusters in a dataset without any prior knowledge of the groups.Imagine you have a bag of mixed fruits, and you want to organize them into different groups based on their similarities. You might start by looking at their shape, color, and size. For example, you would group together all the round-shaped, red fruits, such as apples and tomatoes. Then, you might group the elongated, yellow fruits, such as bananas and lemons. This process of categorizing fruits based on their features is similar to how a clustering algorithm works.

A popular clustering algorithm is K-means clustering. It divides a dataset into a predetermined number of clusters, where each object belongs to the cluster with the closest mean value. Imagine you have a dataset of customer information, including age and income. You could use K-means clustering to group customers based on similar age and income levels. For example, you might find a cluster of younger customers with lower incomes and another cluster of older customers with higher incomes.

K-means clustering is widely used in various fields, such as market segmentation, image recognition, and social network analysis.

## Complexity 

Clustering can be challenging for several reasons. Firstly, it is a type of unsupervised learning, meaning there is no predetermined outcome to guide the process. Unlike supervised learning where the algorithm is provided with labeled data to learn from, clustering algorithms must identify patterns and similarities within the data on their own.

Additionally, the difficulty of clustering can vary based on the complexity of the dataset. If the data is inherently noisy, overlapping, or contains outliers, it becomes harder to define clear clusters. For example, imagine trying to group a diverse set of animals based on their characteristics. While it may be easy to cluster cats and dogs separately, distinguishing between animals with similar features like dolphins and sharks becomes more challenging.

The computational complexity of clustering algorithms can also impact the difficulty of the problem. Some algorithms, such as hierarchical clustering, have a time complexity of O(n^3) where n represents the number of data points. This means that as the dataset grows in size, the time required to cluster the data increases significantly. Other algorithms like k-means have a time complexity of O(n*k*T*i), where k is the number of clusters, T is the number of iterations, and i is the size of each data instance. This complexity can make clustering computationally expensive for large datasets.

In terms of memory, clustering algorithms also require storage for the input data, intermediate results, and the final cluster assignments. The amount of memory needed depends on the size of the dataset and the algorithm used. For instance, density-based clustering algorithms like DBSCAN require additional memory to store the neighborhood information of each point, making them more memory-intensive compared to k-means.

## Metrics 

Metrics are used in clustering to measure the similarity or dissimilarity between data points. In this context, metrics refer to distance or similarity measures

# 1. Metrics with Ground Truth:

a. **Rand Index (ARI):** ARI measures the similarity between two clusterings, taking into account all pairwise agreements between data points. The ARI value ranges from -1 to 1, where 1 indicates perfect agreement and 0 represents random clustering.

b. **Mutual Information (NMI & AMI)** Given the knowledge of the ground truth class assignments labels_true and our clustering algorithm assignments of the same samples labels_pred, the Mutual Information is a function that measures the agreement of the two assignments, ignoring permutations.

c. **Pair confusion matrix** Confusion matrix confronting true labels with prediction labels from clustering.

# 2. Metrics without Ground Truth:

 **Silhouette Coefficient:** The Silhouette Coefficient measures how well each data point fits into its assigned cluster. It combines both the average distance between data points within a cluster (a) and the average distance between data points of different clusters (b). The coefficient ranges from -1 to 1, where values closer to 1 indicate well-separated clusters. A value of 0 suggests overlapping clusters, and negative values indicate misclassified data points

a. **Euclidean Distance:** This is a commonly used metric for clustering continuous numerical data. It calculates the straight-line distance between two data points in the multidimensional space. For instance, if we have two data points A = (2, 3) and B = (5, 7), the Euclidean distance would be √((2-5)^2 + (3-7)^2) = √29.

b. **Cosine Similarity:** Cosine similarity is used to measure the similarity between two vectors, regardless of their magnitudes. It calculates the cosine of the angle between the vectors. For example, if we have two vectors A = [1, 2, 3] and B = [4, 5, 6], the cosine similarity would be (1*4 + 2*5 + 3*6) / (√(1^2+2^2+3^2) * √(4^2+5^2+6^2)) = 0.9746.

c. **Hamming Distance:** This metric is commonly used for clustering categorical or binary data. It calculates the number of positions at which two binary strings differ. For instance, if we have two binary strings A = 10101 and B = 11101, the Hamming distance would be 1.


