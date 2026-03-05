from sklearn.datasets import fetch_20newsgroups
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

# library for save and load scikit-learn models
import pickle


# Load dataset
#newsgroups = fetch_20newsgroups(subset='all', categories=['rec.sport.baseball', 'sci.space'], shuffle=True, random_state=42)
newsgroups = fetch_20newsgroups(subset='all', shuffle=True, random_state=42)
data = newsgroups.data
target = newsgroups.target

# Create a DataFrame for easy manipulation
df = pd.DataFrame({'text': data, 'label': target})
df.head()



# Initialize TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Transform the text data to feature vectors
X = vectorizer.fit_transform(df['text'])

# Labels
y = df['label']


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the classifier
clf = SVC(kernel='linear')
clf.fit(X_train, y_train)

# Predict on the test set
y_pred = clf.predict(X_test)

# Evaluate the performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=newsgroups.target_names)

print(f'Accuracy: {accuracy:.4f}')
print('Classification Report:')
print(report)


#Save Model
filename_model = "20newsgroups.pickle"
pickle.dump(clf, open(filename_model, "wb"))

filename_fitted_vectorizer = "20newsgroups_fitted_vectorizer.pickle"
pickle.dump(vectorizer, open(filename_fitted_vectorizer, "wb"))

filename_target_names = "20newsgroups_target_names.pickle"
pickle.dump(newsgroups.target_names, open(filename_target_names, "wb"))