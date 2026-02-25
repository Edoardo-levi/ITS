import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import numpy as np
import pandas as pd
import tensorflow as tf

# 1. Caricamento del dataset Wine
wine = load_wine()
data, labels = wine.data, wine.target

# 2. Divisione in 150 per il training e 28 per il test
train_data, test_data, train_labels, test_labels = train_test_split(
    data, labels, 
    train_size=150, 
    test_size=28, 
    random_state=42 # Per la riproducibilità
)

# 3. Funzione di conversione per creare i vettori one-hot per le 3 classi
def ConvertiY(y):
    ly=[]
    for vy in y:
        if vy==0:
            ly.append(np.array([1,0,0]))
        elif vy==1:
            ly.append(np.array([0,1,0]))
        else:
            ly.append(np.array([0,0,1]))
    return np.array(ly)

y_train = ConvertiY(train_labels)
y_test = ConvertiY(test_labels)

# 4. Creazione del modello della Rete Neurale
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(128, activation=tf.keras.activations.relu, input_shape=(13,)))
model.add(tf.keras.layers.Dense(32, activation=tf.keras.activations.relu))
model.add(tf.keras.layers.Dense(3, activation=tf.keras.activations.softmax))

# 5. Compilazione
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# 6. Addestramento del modello
history = model.fit(train_data, y_train, epochs=200, verbose=0, validation_data=(test_data, y_test))

# 7. Valutazione sui 28 campioni di test
predicted_probabilities = model.predict(test_data)
predicted_labels = np.argmax(predicted_probabilities, axis=1)

# ----------------------------------------------------------------------------------
# NUOVA SEZIONE: Dati forniti, Valori Attesi e Predizioni
# ----------------------------------------------------------------------------------

# Creiamo un DataFrame Pandas per combinare le caratteristiche di input con le etichette
df_results = pd.DataFrame(test_data, columns=wine.feature_names)
df_results['Valore_Atteso'] = test_labels
df_results['Valore_Predetto'] = predicted_labels
df_results['Corretto'] = (df_results['Valore_Atteso'] == df_results['Valore_Predetto'])

# Stampa a schermo un riassunto dei risultati per ogni campione testato
print("\n--- Confronto sul Test Set (28 Campioni) ---")
for i in range(len(test_labels)):
    esito = "Sì" if test_labels[i] == predicted_labels[i] else "No"
    print(f"Campione {i+1:2d} | Valore Atteso (Target): {test_labels[i]} | Valore Predetto: {predicted_labels[i]} | Classificazione Corretta: {esito}")

# Esportiamo tutti i "valori dati" originali combinati alle predizioni su file
df_results.to_csv('confronto_risultati_test.csv', index=False)
print("\n[!] I dati di input completi, insieme a valori attesi e predetti, sono stati salvati in 'confronto_risultati_test.csv'.\n")

# ----------------------------------------------------------------------------------
# GESTIONE DEI RISULTATI VISIVI CON MATPLOTLIB (Come prima)
# ----------------------------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Sottografico Accuratezza
axs[0].plot(history.history['accuracy'], label='Training Accuracy')
axs[0].plot(history.history['val_accuracy'], label='Test Accuracy')
axs[0].set_title('Accuratezza della Rete Neurale')
axs[0].set_xlabel('Epoca')
axs[0].set_ylabel('Accuratezza')
axs[0].legend(loc='lower right')

# Sottografico Loss
axs[1].plot(history.history['loss'], label='Training Loss')
axs[1].plot(history.history['val_loss'], label='Test Loss')
axs[1].set_title('Funzione di Perdita (Loss)')
axs[1].set_xlabel('Epoca')
axs[1].set_ylabel('Loss')
axs[1].legend(loc='upper right')

plt.tight_layout()
plt.show()

# Matrice di confusione
cm = confusion_matrix(test_labels, predicted_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=wine.target_names)
disp.plot(cmap=plt.cm.Blues)
plt.title('Matrice di Confusione sui 28 Vini di Test')
plt.show()