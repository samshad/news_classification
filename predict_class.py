import pickle
import text_cleaner as tc

with open('Model/svc.pkl', 'rb') as pickle_file:
    svc = pickle.load(pickle_file)
with open('Model/tfidf.pkl', 'rb') as pickle_file:
    tfidf = pickle.load(pickle_file)

x_sample = "Sri Lanka team for T20 WC 2022: Most of the players who were part of Sri Lankan squad for Asia Cup 2022 are included in Lanka's T20 World Cup squad."
x = tc.cleanText(x_sample)
x = tfidf.transform([x])
y = svc.predict(x)
print(y)
