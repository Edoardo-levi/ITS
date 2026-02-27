import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from Levenshtein import distance as lev_dist
 
# 1. DEFINIAMO LE "ANCORE" (I domini legittimi di riferimento)
# Questi sono i punti fissi del nostro universo.
anchors = ["google.com", "facebook.com", "amazon.com", "apple.com", "microsoft.com"]
 
# 2. FUNZIONE DI VETTORIZZAZIONE (Feature Engineering)
# Trasforma una stringa in una lista di distanze dalle ancore
def string_to_vector(domain):
    # Calcola la distanza da OGNI ancora
    dists = [lev_dist(domain, anchor) for anchor in anchors]
    return np.array(dists)
 
# --- 3. CREIAMO IL DATASET ---
# Dati grezzi
raw_data = [
    "google.com",       # Legit (Dist da google: 0)
    "facebook.com",     # Legit
    "amazon.com",       # Legit
    "g0ogle.com",       # Phish (Dist da google: 1)
    "faceb00k.com",     # Phish (Dist da facebook: 2)
    "amaz0n.net",       # Phish
    "appple.com",       # Phish
    "microsft.com",     # Phish
    "yahoo.com"         # Legit (ma non è nelle ancore, vediamo che succede)
]
 
# Labels: 0 = Legit, 1 = Phish
labels = np.array([0, 0, 0, 1, 1, 1, 1, 1, 0])
 
# Trasformiamo le stringhe in vettori numerici
# X sarà una matrice (9 campioni, 5 ancore)
X = np.array([string_to_vector(d) for d in raw_data])
 
# Normalizziamo leggermente (opzionale ma utile per le NN)
X = X / 10.0  # Scaliamo le distanze (assumiamo max dist ~10-20)
 
print("Esempio di input trasformato per 'g0ogle.com':")
print(f"Ancore: {anchors}")
print(f"Vettore Distanze: {string_to_vector('g0ogle.com')}")
# Output atteso: [1, 7, 6, 7, 12] -> Nota l'1 all'inizio!
 
# --- 4. COSTRUIAMO LA RETE NEURALE ---
model = Sequential([
    # Input Layer: dimensione = numero di ancore (5)
    Dense(16, input_dim=len(anchors), activation='relu'), 
    Dense(8, activation='relu'),
    Dense(1, activation='sigmoid') # Output: Probabilità Phishing
])
 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
 
# --- 5. ADDESTRAMENTO ---
print("\nTraining NN...")
model.fit(X, labels, epochs=100, verbose=0) 
print("Training completato.")
 
# --- 6. TEST SU NUOVI DOMINI ---
test_domains = ["google.it", "googel.com", "amazon.com", "msoft.com"]
print("\n--- TEST ---")
 
for domain in test_domains:
    # 1. Preprocessing (uguale al training)
    vec = string_to_vector(domain)
    vec_norm = vec / 10.0
    
    # 2. Reshape per Keras (da (5,) a (1, 5))
    vec_input = vec_norm.reshape(1, -1)
    
    # 3. Predizione
    prob = model.predict(vec_input, verbose=0)[0][0]
    
    label = "PHISHING" if prob > 0.5 else "LEGIT"
    print(f"Dominio: '{domain}'")
    print(f" -> Vettore distanze: {vec}")
    print(f" -> Rete dice: {prob:.4f} ({label})")
