import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# 1. Generate sample data
# Feature matrix (4 samples, 2 features)
X = np.array(
    [
        [-1, -1],
        [-2, -1],
        [1, 1],
        [2, 1]
    ]
)
# Target labels
y = np.array(
    [
        1,
        1,
        2,
        2
    ]
)

# 2. Create a pipeline with scaling (crucial for SGD)
# SGD is sensitive to feature scaling.
clf = make_pipeline(StandardScaler(),
                    SGDClassifier(max_iter=1000, tol=1e-3))

# 3. Train the model
clf.fit(X, y)

# 4. Predict new data
prediction = clf.predict([[2, 2]])
print(f"Prediction: {prediction}") # Output: [2]