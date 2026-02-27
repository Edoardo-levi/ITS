# nn_autoencoder.ipynb
# Autoencoder per anomaly detection
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras import regularizers

# Esempio: dataset di log "normali" + "anomali"
df = pd.read_csv('user_logs.csv')  # fittizio

# Supponiamo che "anomaly" = 0 o 1 (label)
df_normal = df[df['anomaly']==0].drop('anomaly', axis=1)
df_anomal = df[df['anomaly']==1].drop('anomaly', axis=1)

# Useremo SOLO i dati normali per addestrare l'autoencoder
X_normal = df_normal.values
X_anomal = df_anomal.values

scaler = StandardScaler()
X_normal_scaled = scaler.fit_transform(X_normal)
X_anomal_scaled = scaler.transform(X_anomal)

# Dividiamo train e test
X_train, X_val = train_test_split(X_normal_scaled, test_size=0.2, random_state=42)

input_dim = X_train.shape[1]

# Definizione autoencoder
input_layer = Input(shape=(input_dim,))
encoded = Dense(16, activation='relu', 
                activity_regularizer=regularizers.l1(1e-5))(input_layer)
encoded = Dense(8, activation='relu')(encoded)
decoded = Dense(16, activation='relu')(encoded)
output_layer = Dense(input_dim, activation='linear')(decoded)

autoencoder = Model(inputs=input_layer, outputs=output_layer)
autoencoder.compile(optimizer='adam', loss='mse')

# Training su dati normali
history = autoencoder.fit(X_train, X_train,
                          epochs=20,
                          batch_size=32,
                          validation_data=(X_val, X_val),
                          verbose=1)

# Calcoliamo errore di ricostruzione
reconstructions = autoencoder.predict(X_normal_scaled)
mse = np.mean(np.power(X_normal_scaled - reconstructions, 2), axis=1)
threshold = np.percentile(mse, 95)  # soglia al 95% percentile

# Test su dati anomali
reconstructions_anom = autoencoder.predict(X_anomal_scaled)
mse_anom = np.mean(np.power(X_anomal_scaled - reconstructions_anom, 2), axis=1)

# Classificazione:
normal_pred = (mse < threshold).astype(int)   # 1 = normale, 0 = anomalia
anomal_pred = (mse_anom < threshold).astype(int)

print("Percentuale di anomalie correttamente rilevate:", np.mean(anomal_pred==0)*100, "%")
