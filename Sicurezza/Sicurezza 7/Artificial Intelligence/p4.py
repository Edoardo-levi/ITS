import numpy as np
from sklearn.neighbors import KNeighborsClassifier
def lev_dist_pure(s1, s2):
    if len(s1) < len(s2):
        return lev_dist_pure(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]
 
# --- 1. DATI REALI (Le stringhe restano fuori dal KNN) ---
# Creiamo una lista "esterna" che funge da database
corpus_train = [
    "google.com", 
    "facebook.com", 
    "amazon.com", 
    "g00gle.com",      # Phishing
    "faceb00k.login",  # Phishing
    "amaz0n-security"  # Phishing
]
y_train = np.array([0, 0, 0, 1, 1, 1])
 
# --- 2. DATI PER IL KNN (Solo gli indici!) ---
# Creiamo un array di numeri: [[0], [1], [2], [3], [4], [5]]
# Questo è ciò che vedrà Scikit-Learn. Per lui sono numeri, quindi è felice.
X_train_indices = np.arange(len(corpus_train)).reshape(-1, 1)
 
# --- 3. LA FUNZIONE METRICA TRUCCATA ---
def levenshtein_metric_proxy(x, y):
    # x e y qui dentro arrivano come numeri (float).
    # Esempio: x=[3.0], y=[0.0]
    
    # 1. Convertiamo in intero per avere l'indice
    idx1 = int(x[0])
    idx2 = int(y[0])
    
    # 2. Recuperiamo le stringhe vere dalla lista esterna
    # Nota: Dobbiamo gestire sia il training che il test.
    # Se l'indice è dentro il range del training, usiamo corpus_train.
    # Ma se stiamo testando, l'indice arriverà dal test set... 
    # Qui stiamo assumendo che x e y siano entrambi indici che puntano
    # a una lista globale o che facciamo un "lookup".
 
   # Per far funzionare fit() e predict() insieme senza impazzire con gli indici,
    # passiamo direttamente le stringhe nel test set usando una Lambda, 
    # ma siccome sklearn blocca le stringhe, la via più pulita è usare "precomputed".
    # Ma proviamo a finire questo approccio "proxy" con una lista unificata temporanea.
    
    str1 = data_source[idx1]
    str2 = data_source[idx2]
    
    return lev_dist_pure(str1, str2)
 
# ==============================================================================
# (Evita tutti i problemi di indici e tipi di dati)
# Questa è quella che ti consiglio di mostrare, funziona sempre.
# ==============================================================================
 
# 1. Calcoliamo noi la matrice delle distanze PRIMA
def compute_distance_matrix(list_a, list_b):
    matrix = np.zeros((len(list_a), len(list_b)))
    for i, str_a in enumerate(list_a):
        for j, str_b in enumerate(list_b):
            matrix[i, j] = lev_dist_pure(str_a, str_b)
    return matrix
 
print("1. Calcolo matrice distanze Training...")
# Distanza tra training e se stesso
X_train_dist_matrix = compute_distance_matrix(corpus_train, corpus_train)
 
# 2. Addestriamo il KNN dicendogli "Ho già calcolato tutto io" (metric='precomputed')
knn = KNeighborsClassifier(n_neighbors=1, metric='precomputed')
knn.fit(X_train_dist_matrix, y_train) 
 
# 3. Test
test_domains = ["google.it", "googel.com", "microsoft.com", "g00gle.it"]
 
print("2. Calcolo matrice distanze Test...")
# Per predire, dobbiamo dare le distanze tra i NUOVI dati e i VECCHI dati (Training)
# Righe = Nuovi dati, Colonne = Dati Training
X_test_dist_matrix = compute_distance_matrix(test_domains, corpus_train)
 
print("\n--- RISULTATI ---")
preds = knn.predict(X_test_dist_matrix)
 
for domain, pred in zip(test_domains, preds):
    label = "Phishing" if pred == 1 else "Safe"
    # Troviamo il vicino più prossimo manualmente per mostrarlo
    dists = X_test_dist_matrix[test_domains.index(domain)]
    nearest_idx = np.argmin(dists)
    nearest_name = corpus_train[nearest_idx]
    nearest_dist = dists[nearest_idx]
    
    print(f"Dominio: '{domain}' -> {label}")
    print(f"  (Simile a: '{nearest_name}', Distanza: {int(nearest_dist)})")
