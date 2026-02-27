import os
import pickle
import numpy as np
import tensorflow as tf
from sklearn.neighbors import KNeighborsClassifier
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
 
def get_file_size(filepath):
    """Restituisce la dimensione del file in Kilobyte (KB)"""
    return os.path.getsize(filepath) / 1024
 
# 1. SETUP DELL'ESPERIMENTO
# Creiamo un dataset "corposo": 10.000 campioni, 50 caratteristiche ciascuno
n_samples = 10000 
n_features = 50
X = np.random.rand(n_samples, n_features).astype('float32')
y = np.random.randint(0, 2, n_samples)
 
print(f"--- ESPERIMENTO: {n_samples} Campioni con {n_features} caratteristiche ---")
 
# ==========================================
# 2. ADDESTRAMENTO E SALVATAGGIO KNN
# ==========================================
print("\nAddestramento KNN in corso...")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)
 
# Salviamo il modello su disco (simuliamo l'invio al cliente)
with open('modello_knn.pkl', 'wb') as f:
    pickle.dump(knn, f)
 
size_knn = get_file_size('modello_knn.pkl')
print(f"💾 Dimensione modello KNN su disco: {size_knn:.2f} KB")
 
 
# ==========================================
# 3. ADDESTRAMENTO E SALVATAGGIO RETE NEURALE
# ==========================================
print("\nAddestramento Rete Neurale in corso...")
model = Sequential([
    Dense(32, input_dim=n_features, activation='relu'), # Hidden Layer
    Dense(16, activation='relu'),                       # Hidden Layer
    Dense(1, activation='sigmoid')                      # Output Layer
])
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(X, y, epochs=2, verbose=0, batch_size=32) # Poche epoche, basta che inizializzi i pesi
 
# Salviamo il modello nel nuovo formato nativo di Keras
model.save('modello_nn.keras')
 
size_nn = get_file_size('modello_nn.keras')
print(f"💾 Dimensione modello Neural Network su disco: {size_nn:.2f} KB")
 
# ==========================================
# 4. IL RISULTATO FINALE (Il confronto)
# ==========================================
ratio = size_knn / size_nn
print(f"\n--- CONCLUSIONE ---")
print(f"Il modello KNN è {ratio:.1f} volte più pesante della Rete Neurale!")
print(f"Se dovessi spedire l'aggiornamento antivirus a 1 milione di clienti:")
print(f"- Traffico KNN: {size_knn * 1000000 / 1024 / 1024:.2f} GB")
print(f"- Traffico NN:  {size_nn * 1000000 / 1024 / 1024:.2f} GB")