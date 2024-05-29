# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN

# Generate sample data
n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state)

# k-means Clustering
def kmeans_clustering(X, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    y_kmeans = kmeans.fit_predict(X)
    
    plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='X')
    plt.title("k-means Clustering")
    plt.show()

# Hierarchical Clustering (Agglomerative)
def hierarchical_clustering(X, n_clusters=3):
    hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
    y_hierarchical = hierarchical.fit_predict(X)
    
    plt.scatter(X[:, 0], X[:, 1], c=y_hierarchical, s=50, cmap='viridis')
    plt.title("Hierarchical Clustering")
    plt.show()

# DBSCAN Clustering
def dbscan_clustering(X, eps=0.5, min_samples=5):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    y_dbscan = dbscan.fit_predict(X)
    
    plt.scatter(X[:, 0], X[:, 1], c=y_dbscan, s=50, cmap='viridis')
    plt.title("DBSCAN Clustering")
    plt.show()

# Generate the plots
kmeans_clustering(X)
hierarchical_clustering(X)
dbscan_clustering(X)
