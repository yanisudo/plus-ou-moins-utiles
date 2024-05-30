import numpy as np
from sklearn.ensemble import IsolationForest

# Exemple de données réseau
data = np.array([[10, 0.5], [12, 0.6], [11, 0.55], [100, 20], [200, 30]])

# Entraînement du modèle de détection
clf = IsolationForest(contamination=0.2)
clf.fit(data)

# Détection des anomalies
predictions = clf.predict(data)
print(predictions)  # -1 pour anomalie, 1 pour normal