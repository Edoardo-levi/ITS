import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import tensorflow as tf

# 1. CARICAMENTO E ANALISI PRELIMINARE
url = "/home/its/ITS/Sicurezza/Sicurezza 7/Artificial Intelligence/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv"

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

print("Caricamento dataset...")
df = pd.read_csv(url, names=col_names, header=0).sample(n=100000, random_state=42)

# --- NUOVA SEZIONE: Conteggio Benigni vs Maligni ---
print("\n--- Distribuzione del Traffico ---")
counts = df['label'].value_counts()
for name, count in counts.items():
    tipo = "BENIGNO" if name.strip() == "Benign" else "MALIGNO"
    print(f"[{tipo}] {name.strip()}: {count} pacchetti")

# 2. PREPROCESSING
df['target'] = df['label'].apply(lambda x: 0 if str(x).strip() == 'Benign' else 1)

features_numeric = ['fl_dur', 'tot_fw_pk', 'tot_bw_pk', 'tot_l_fw_pkt', 'fl_byt_s', 'fl_pkt_s', 'fw_win_byt', 'bw_win_byt']
X_numeric = df[features_numeric].apply(pd.to_numeric, errors='coerce')
X_numeric.replace([np.inf, -np.inf], np.nan, inplace=True)

# Uniamo per non perdere gli indici originali delle label
data_combined = pd.concat([X_numeric, df['target'], df['label']], axis=1).dropna()

X = data_combined[features_numeric]
y = data_combined['target']
labels_originali = data_combined['label']

# 3. NORMALIZZAZIONE E SPLIT
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test, label_train, label_test = train_test_split(
    X_scaled, y, labels_originali, test_size=0.1, random_state=42
)

# 4. TRAINING MODELLI
knn = KNeighborsClassifier(n_neighbors=3).fit(X_train, y_train)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=5, batch_size=32, verbose=0)

# --- VERIFICA FINALE---
print("\n--- Analisi Dettagliata: Rilevamento Maligni (❌) vs Benigni (✅) ---")

campioni = X_test[:15]
reali_binary = y_test[:15].values
nomi_reali = label_test[:15].values

# Predizione della Rete Neurale
pred_nn_raw = model.predict(campioni, verbose=0)
pred_nn = np.argmax(pred_nn_raw, axis=1)

print(f"{'Stato':<10} | {'NN Pred':<7} | {'Prob. Attack':<12} | {'Tipo Attacco Reale'}")
print("-" * 75)

for i in range(len(reali_binary)):
    r_bin = reali_binary[i]
    p_bin = pred_nn[i]
    prob_atk = pred_nn_raw[i][1]
    tipo_reale = nomi_reali[i].strip()
    
    # LOGICA RICHIESTA: 
    # Se il reale è 1 (Maligno) -> ❌
    # Se il reale è 0 (Benigno) -> ✅
    icona = "❌ MALIGNO" if r_bin == 1 else "✅ BENIGNO"
    
    # Verifica se la previsione della rete è corretta rispetto al reale
    match = "CORRETTO" if r_bin == p_bin else "ERRORE"
    
    print(f"{icona:<10} | {p_bin:<7} | {prob_atk:<12.4f} | {tipo_reale:<25} ({match})")

# Conteggio rapido nel campione visualizzato
maligni_trovati = sum(reali_binary)
print(f"\nRiepilogo campioni: {len(reali_binary)} totali, {maligni_trovati} Maligni individuati.")