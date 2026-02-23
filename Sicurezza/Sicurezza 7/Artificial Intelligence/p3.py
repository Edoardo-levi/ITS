import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import time
 
# 1. Caricamento dati
(x_train, y_train), (x_test, y_test) = mnist.load_data()
 
# 2. FLATTENING: Da Matrice (28x28) a Vettore (784)
# Scikit-learn vuole vettori piatti, non matrici
x_train_flat = x_train.reshape(x_train.shape[0], -1)  # (60000, 784)
x_test_flat = x_test.reshape(x_test.shape[0], -1)    # (10000, 784)
 
# 3. RIDUZIONE DATASET
# Usiamo solo 5000 immagini per il training per non bloccare il PC
limit = 5000
x_train_small = x_train_flat[:limit]
y_train_small = y_train[:limit]
 
# Normalizzazione (0-255 -> 0-1) aiuta il calcolo della distanza euclidea
x_train_small = x_train_small / 255.0
x_test_flat = x_test_flat / 255.0
 
print(f"Training su {limit} immagini (vettori di dim 784)...")
 
# 4. Addestramento KNN
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
 
start_time = time.time()
knn.fit(x_train_small, y_train_small) # "Fit" nel KNN è solo memorizzazione
print(f"Training completato in {time.time() - start_time:.2f} secondi.")
 
# 5. Predizione su un esempio
index = 0
sample_image = x_test_flat[index].reshape(1, -1)
prediction = knn.predict(sample_image)
 
# Visualizzazione risultato
plt.imshow(x_test[index], cmap='gray')
plt.title(f"Vero: {y_test[index]} - Predetto dal KNN: {prediction[0]}")
plt.show()
 
# 6. Accuracy su tutto il test set (o una parte)
print("Calcolo accuracy su 1000 test images...")
preds = knn.predict(x_test_flat[:1000])
acc = accuracy_score(y_test[:1000], preds)
print(f"Accuracy KNN (K={k}): {acc:.2%}")