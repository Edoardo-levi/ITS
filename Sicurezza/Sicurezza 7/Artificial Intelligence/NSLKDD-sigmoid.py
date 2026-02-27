import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import tensorflow as tf

# URL diretto al dataset
url = "/home/its/ITS/Sicurezza/Sicurezza 7/Artificial Intelligence/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv"

# 1. DEFINIZIONE COLONNE (La tua nuova lista ufficiale)
col_names = [
    "fl_dur", "tot_fw_pk", "tot_bw_pk", "tot_l_fw_pkt", "fw_pkt_l_max", 
    "fw_pkt_l_min", "fw_pkt_l_avg", "fw_pkt_l_std", "Bw_pkt_l_max", "Bw_pkt_l_min", 
    "Bw_pkt_l_avg", "Bw_pkt_l_std", "fl_byt_s", "fl_pkt_s", "fl_iat_avg", 
    "fl_iat_std", "fl_iat_max", "fl_iat_min", "fw_iat_tot", "fw_iat_avg", 
    "fw_iat_std", "fw_iat_max", "fw_iat_min", "bw_iat_tot", "bw_iat_avg", 
    "bw_iat_std", "bw_iat_max", "bw_iat_min", "fw_psh_flag", "bw_psh_flag", 
    "fw_urg_flag", "bw_urg_flag", "fw_hdr_len", "bw_hdr_len", "fw_pkt_s", 
    "bw_pkt_s", "pkt_len_min", "pkt_len_max", "pkt_len_avg", "pkt_len_std", 
    "pkt_len_va", "fin_cnt", "syn_cnt", "rst_cnt", "pst_cnt", "ack_cnt", 
    "urg_cnt", "cwe_cnt", "ece_cnt", "down_up_ratio", "pkt_size_avg", 
    "fw_seg_avg", "bw_seg_avg", "fw_byt_blk_avg", "fw_pkt_blk_avg", 
    "fw_blk_rate_avg", "bw_byt_blk_avg", "bw_pkt_blk_avg", "bw_blk_rate_avg", 
    "subfl_fw_pk", "subfl_fw_byt", "subfl_bw_pkt", "subfl_bw_byt", 
    "fw_win_byt", "bw_win_byt", "Fw_act_pkt", "fw_seg_min", "atv_avg", 
    "atv_std", "atv_max", "atv_min", "idl_avg", "idl_std", "idl_max", "idl_min",
    "label"
]

# Caricamento mantendo la struttura originale
print("Caricamento dataset in corso...")
df = pd.read_csv(url, names=col_names, header=0).sample(n=1000000, random_state=42)

# 2. PREPROCESSING
print("Preprocessing e pulizia...")

# Trasformiamo la label in Binario: "Benign" -> 0, tutto il resto -> 1
df['target'] = df['label'].apply(lambda x: 0 if str(x).strip() == 'Benign' else 1)

# SELEZIONE FEATURE (Sostituite quelle di NSL-KDD con quelle valide di CIC-IDS-2018)
# Ho selezionato quelle numeriche corrispondenti alla tua lista per evitare il KeyError
features_numeric = [
    'fl_dur', 'tot_fw_pk', 'tot_bw_pk', 'tot_l_fw_pkt', 
    'fl_byt_s', 'fl_pkt_s', 'fw_win_byt', 'bw_win_byt'
]

# Creiamo il set di dati X con le sole colonne scelte
X_numeric = df[features_numeric].apply(pd.to_numeric, errors='coerce')

# Gestione valori infiniti/nulli (struttura preservata)
X_numeric.replace([np.inf, -np.inf], np.nan, inplace=True)
data_combined = pd.concat([X_numeric, df['target']], axis=1).dropna()

X = data_combined.drop(columns=['target'])
y = data_combined['target']

print(f"Nuovo numero di feature: {X.shape[1]}")

# 3. NORMALIZZAZIONE
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.1, random_state=42)

print(f"Dati pronti. Feature vector size: {X_train.shape[1]}")

# --- CONFRONTO ---

# A) KNN
print("\nAddestramento KNN...")
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
print(f"KNN Accuracy: {accuracy_score(y_test, y_pred_knn):.4f}")

# B) Rete Neurale (TensorFlow)
print("\nAddestramento Neural Network...")
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=1)

# --- VERIFICA FINALE (Struttura Reale | KNN | NN) ---
print("\n--- Confronto Predizioni (Primi 10 campioni) ---")
campioni = X_test[:10]
reali = y_test[:10].values

pred_knn = knn.predict(campioni)
pred_nn = (model.predict(campioni) > 0.5).astype(int).flatten()

print("Reale | KNN | NN")
for r, k, n in zip(reali, pred_knn, pred_nn):
    status = "✅" if r == k == n else "❌"
    print(f"  {r}   |  {k}  | {n}  {status}")

print("\n--- Analisi Dettagliata KNN ---")
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn, target_names=['Normal/Benign', 'Attack']))