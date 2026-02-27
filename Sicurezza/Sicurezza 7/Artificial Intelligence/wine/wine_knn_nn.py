import tensorflow as tf
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Input
import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn.preprocessing import StandardScaler, LabelEncoder

 
# 1. Caricamento dati
wine = load_wine()
print(wine.DESCR)
data, labels = wine.data, wine.target

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)


x_train, x_test, y_train, y_test = train_test_split(data_scaled, labels, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=12)
print(x_train.shape) # Deve essere (numero_righe, 13)

# 2. Creazione del Modello
model = Sequential([
    # Input layer che "schiaccia" la matrice 28x28 in un vettore lungo 784
    Input(shape=(13,)),
    # Hidden Layer (ricordate lo xor?)
    Dense(256, activation='relu'), 
    Dense(128, activation='relu'), 
    
    
    # Output Layer (3 neuroni per le 3 cifre, softmax per la probabilità)
    Dense(3, activation='softmax')
])
 
# 3. Compile e Training
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
 
model.fit(x_train, y_train, epochs=30)


 
# E ora una prova
# 1. Scegliamo un'immagine a caso dal test set (es. la numero 123)

for i in range(100):
    idx = random.randint(0, len(x_test)-1)
    data = x_test[idx]
    data = np.expand_dims(data, axis=0)
    etichetta_vera = y_test[idx]
    
    # 2. PREDIZIONE

    # Otteniamo il vettore di 3 probabilità
    predizioni = model.predict(data)
    
    # 3. INTERPRETAZIONE (Argmax)
    # np.argmax ci dice l'indice del valore più alto nel vettore
    numero_predetto = np.argmax(predizioni)
    confidenza = np.max(predizioni) * 100 # Quanto è sicura?
    print(f"Vero: {etichetta_vera} | Predetto: {numero_predetto}\nSicurezza: {confidenza:.2f}%")
    # # 4. VISUALIZZAZIONE
    # plt.imshow(immagine, cmap='gray')
    # plt.title(f"Vero: {etichetta_vera} | Predetto: {numero_predetto}\nSicurezza: {confidenza:.2f}%")
    # plt.axis('off')
    # plt.show()
    
    print("Vettore Probabilità:", np.round(predizioni, 2))
