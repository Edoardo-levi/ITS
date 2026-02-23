#pip install scikit-learn
#pip install tensorflow

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
from sklearn.metrics import confusion_matrix 

iris = load_iris()

data, labels = iris.data, iris.target

res = train_test_split(data, labels, 
                       train_size=0.8,
                       test_size=0.2,
                       random_state=42)
train_data, test_data, train_labels, test_labels = res

X = train_data
y = train_labels

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

y = ConvertiY(y)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(128, activation=tf.keras.activations.relu, input_shape=(4,)))
model.add(tf.keras.layers.Dense(32, activation=tf.keras.activations.relu))
model.add(tf.keras.layers.Dense(3, activation=tf.keras.activations.softmax))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.05), loss='categorical_crossentropy', metrics=[tf.keras.metrics.Accuracy()])
model.fit(X, y, epochs=1000)

# Mi sono perso, non ci sto capendo più nulla
# la cosa migliore è stampare le X e le Y per vedere che cosa sono
# for vx, vy in zip(X, y):
#     print(vx, vy)

predictions = model.predict(X)
# print(predictions)

# Stampo accoppiati predizione e valore reale/atteso
conta=0
for vp, vy in zip(predictions, y):
    for x in vp:
        print(round(x), end=", ")
    print(vy)
    if round(vp[0])==vy[0] and round(vp[1])==vy[1] and round(vp[2])==vy[2]:
        conta+=1
print(conta) 

