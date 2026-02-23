import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt
import numpy as np
 
# 1. Caricamento dati
(x_train, y_train), (x_test, y_test) = mnist.load_data()
 
# Normalizzazione (0-255 diventa 0-1) -> Fondamentale per le reti neurali
x_train, x_test = x_train / 255.0, x_test / 255.0
 
# L'immagine è una matrice
plt.imshow(x_train[0], cmap='gray')
plt.title(f"Label: {y_train[0]} - Shape originale: {x_train[0].shape}")
plt.show()
 
# 2. Creazione del Modello
model = Sequential([
    # Input layer che "schiaccia" la matrice 28x28 in un vettore lungo 784
    Flatten(input_shape=(28, 28)), 
    
    # Hidden Layer (ricordate lo xor?)
    Dense(128, activation='relu'), 
    
    # Output Layer (10 neuroni per le 10 cifre, softmax per la probabilità)
    Dense(10, activation='softmax')
])
 
# 3. Compile e Training
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
 
model.fit(x_train, y_train, epochs=5)


 # E ora una prova
# 1. Scegliamo un'immagine a caso dal test set (es. la numero 123)
idx = 123 
immagine = x_test[idx]
etichetta_vera = y_test[idx]
 
# 2. PREDIZIONE
# Attenzione: Keras si aspetta un "batch" di immagini, anche se ne passiamo una sola.
# Dobbiamo aggiungere una dimensione: (28, 28) -> (1, 28, 28)
immagine_batch = np.expand_dims(immagine, axis=0)
 
# Otteniamo il vettore di 10 probabilità
predizioni = model.predict(immagine_batch)
 
# 3. INTERPRETAZIONE (Argmax)
# np.argmax ci dice l'indice del valore più alto nel vettore
numero_predetto = np.argmax(predizioni)
confidenza = np.max(predizioni) * 100 # Quanto è sicura?
 
# 4. VISUALIZZAZIONE
plt.imshow(immagine, cmap='gray')
plt.title(f"Vero: {etichetta_vera} | Predetto: {numero_predetto}\nSicurezza: {confidenza:.2f}%")
plt.axis('off')
plt.show()
 
print("Vettore Probabilità:", np.round(predizioni, 2))