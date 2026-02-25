# pip install scikit-learn tensorflow

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import tensorflow as tf

# 1. Caricamento del dataset Wine (esattamente 178 campioni)
wine = load_wine()
data, labels = wine.data, wine.target

# 2. Divisione dei dati (150 addestramento, 28 test)
res = train_test_split(data, labels, 
                       train_size=150,
                       test_size=28,
                       random_state=42)
train_data, test_data, train_labels, test_labels = res

# 3. Standardizzazione dei dati (FONDAMENTALE per il dataset Wine)
scaler = StandardScaler()
X_train = scaler.fit_transform(train_data)
X_test = scaler.transform(test_data) # Attenzione: uso solo 'transform' per il test!

# 4. Funzione per la conversione in One-Hot encoding (valida per 3 classi)
def ConvertiY(y):
    ly = []
    for vy in y:
        if vy == 0:
            ly.append(np.array([1, 0, 0]))
        elif vy == 1:
            ly.append(np.array([0, 1, 0]))
        else:
            ly.append(np.array([0, 0, 1]))
    return np.array(ly)

# Converto sia le etichette di addestramento che quelle di test
y_train = ConvertiY(train_labels)
y_test = ConvertiY(test_labels)

# 5. Costruzione del Modello Neurale
model = tf.keras.models.Sequential()
# Aggiorno input_shape a 13 perché il dataset Wine ha 13 feature
model.add(tf.keras.layers.Dense(128, activation=tf.keras.activations.relu, input_shape=(13,)))
model.add(tf.keras.layers.Dense(32, activation=tf.keras.activations.relu))
# 3 classi di vino in uscita
model.add(tf.keras.layers.Dense(3, activation=tf.keras.activations.softmax))

# Compilazione (ho abbassato un po' il learning_rate e sistemato la metrica Accuracy)
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01), 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# 6. Addestramento (100 epoche sono generalmente sufficienti con i dati standardizzati)
print("Inizio addestramento sui 150 vini...")
model.fit(X_train, y_train, epochs=100, verbose=1)

# 7. Valutazione e Predizione sui 28 dati di TEST
print("\n--- Test sui 28 vini non visti dalla rete ---")
predictions = model.predict(X_test)

conta = 0
# Stampo accoppiati predizione (arrotondata) e valore reale/atteso
for vp, vy in zip(predictions, y_test):
    predizione_pulita = [round(x) for x in vp]
    valore_reale = list(vy)
    
    print(f"Predizione: {predizione_pulita} | Atteso: {valore_reale}")
    
    # Verifico se la predizione è corretta
    if round(vp[0])==vy[0] and round(vp[1])==vy[1] and round(vp[2])==vy[2]:
        conta += 1

print("\n--- RISULTATO FINALE ---")
print(f"Vini classificati correttamente: {conta} su 28")
print(f"Accuratezza del modello sul Test Set: {(conta/28)*100:.2f}%")