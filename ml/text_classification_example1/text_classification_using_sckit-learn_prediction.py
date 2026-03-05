import pickle

filename_model = "20newsgroups.pickle"
clf = pickle.load(open(filename_model, "rb"))

filename_fitted_vectorizer = "20newsgroups_fitted_vectorizer.pickle"
vectorizer = pickle.load(open(filename_fitted_vectorizer, "rb"))

filename_target_names = "20newsgroups_target_names.pickle"
target_names = pickle.load(open(filename_target_names, "rb"))

# Example usage
#inout_text = "NASA announced the discovery of new exoplanets."
inout_text = "Microsoft is a good company"

text_vec = vectorizer.transform([inout_text])
prediction = clf.predict(text_vec)
predicted_category = target_names[prediction[0]]

print(f'The predicted category is: {predicted_category}')
