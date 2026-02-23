import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_blobs, make_moons
 
# 1. Creiamo un dataset sintetico 2D
# make_blobs crea cluster netti, make_moons crea forme complesse (ottimo per vedere la potenza del KNN)
X, y = make_moons(n_samples=1000, noise=0.3, random_state=42)
# X, y = make_blobs(n_samples=200, centers=3, random_state=42)
 
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
 
def plot_knn_boundary(k_value):
    clf = KNeighborsClassifier(n_neighbors=k_value)
    clf.fit(X, y)
 
    # Creiamo una "griglia" di punti che copre tutto il grafico
    h = .02  # passo della griglia
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
 
    # Chiediamo al KNN di predire il colore per OGNI punto della griglia (lo sfondo)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
 
    # Disegniamo
    plt.figure(figsize=(8, 6))
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light, shading='auto') # Sfondo colorato
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold, edgecolor='k', s=20) # Punti reali
    plt.title(f"KNN Classificazione (K={k_value})\ni 'territori'")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()
 
# ESEGUIAMO CON DIVERSI K
# K=1: "Overfitting". Il confine è frastagliato, insegue ogni singolo punto di rumore.
plot_knn_boundary(1)
 
# K=15: "Generalizzazione". Il confine è più morbido e ignora i punti anomali isolati.
plot_knn_boundary(15)

plot_knn_boundary(200)

plot_knn_boundary(300)