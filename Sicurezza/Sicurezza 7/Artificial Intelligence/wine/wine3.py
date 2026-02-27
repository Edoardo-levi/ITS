import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

# 1. Caricamento dati
wine = load_wine()
X = wine.data     # 178 campioni, 13 features
y = wine.target   # 178 etichette (classe 0, 1 o 2)

# 2. Divisione dei dati (150 per addestramento, 28 per test)
# Il totale è 178, questa divisione è esatta e rispetta le tue richieste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    train_size=150, 
    test_size=28, 
    random_state=42 # Impostato per riproducibilità
)

# 3. Normalizzazione dei dati
# Come nel MNIST dividevi per 255.0, qui usiamo StandardScaler per
# portare tutte le 13 features sulla stessa scala (media 0, varianza 1).
# È fondamentale per far imparare bene la rete neurale.
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Creazione del Modello
model = Sequential([
    # Input layer/Primo Hidden layer: si aspetta un vettore di 13 elementi (le 13 features del vino)
    Dense(64, activation='relu', input_shape=(13,)), 
    
    # Secondo Hidden Layer
    Dense(32, activation='relu'), 
    
    # Output Layer (3 neuroni per le 3 tipologie di vino, softmax per la probabilità)
    Dense(3, activation='softmax')
])

# 5. Compile e Training
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

print("Inizio addestramento della rete neurale sui 150 campioni...")
# Addestriamo per 30 epoche, usando i 28 campioni di test per calcolare la validazione passo passo
history = model.fit(X_train, y_train, epochs=30, validation_data=(X_test, y_test))

# 6. Valutazione finale
print("\n--- VALUTAZIONE SUL SET DI TEST (28 campioni) ---")
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Accuratezza finale: {accuracy * 100:.2f}%\n")

# 7. Prova di predizione su un singolo vino (simile a rete_neurale.py)
idx = 5 # Scegliamo un vino a caso dal test set
vino_selezionato = X_test[idx]
etichetta_vera = y_test[idx]

# Aggiungiamo una dimensione: (13,) -> (1, 13)
vino_batch = np.expand_dims(vino_selezionato, axis=0)

# Otteniamo il vettore di 3 probabilità
predizioni = model.predict(vino_batch)

# Argmax per capire qual è l'indice predetto
vino_predetto = np.argmax(predizioni)
confidenza = np.max(predizioni) * 100

print("--- ESEMPIO DI PREDIZIONE ---")
print(f"Classe vera del vino: {wine.target_names[etichetta_vera]} (Indice: {etichetta_vera})")
print(f"Classe predetta:      {wine.target_names[vino_predetto]} (Indice: {vino_predetto})")
print(f"Sicurezza:            {confidenza:.2f}%")
print("Vettore Probabilità:", np.round(predizioni, 3))