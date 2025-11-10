import pandas as pd
from collections import defaultdict

data = pd.DataFrame({
    'age': ['youth','youth','middle_aged','senior','senior','senior',
            'middle_aged','youth','youth','senior','youth',
            'middle_aged','middle_aged','senior'],

    'income': ['high','high','high','medium','low','low','low',
               'medium','low','medium','medium',
               'medium','high','medium'],

    'student': ['no','no','no','no','yes','yes','yes','no','yes',
                'yes','yes','no','yes','no'],

    'credit_rating': ['fair','excellent','fair','fair','fair',
                      'excellent','excellent','fair','fair','fair',
                      'excellent','excellent','fair','excellent'],

    'BUY_computer': ['no','no','yes','yes','yes','no','yes','no',
                     'yes','yes','yes','yes','yes','no']
})

# Laplace-smoothed naive Bayes
classes = data['BUY_computer'].unique()
priors = data['BUY_computer'].value_counts(normalize=True).to_dict()

feature_counts = {}
feature_totals = {}
for c in classes:
    subset = data[data['BUY_computer'] == c]
    feature_counts[c] = {}
    feature_totals[c] = len(subset)
    for col in ['age','income','student','credit_rating']:
        counts = subset[col].value_counts().to_dict()
        feature_counts[c][col] = counts

def predict(instance):
    scores = {}
    for c in classes:
        score = priors[c]
        for col, val in instance.items():
            # Laplace smoothing: add-1, denom = total + num_possible_values
            possible_vals = data[col].unique()
            count = feature_counts[c][col].get(val, 0)
            score *= (count + 1) / (feature_totals[c] + len(possible_vals))
        scores[c] = score
    return scores

instance = {'age':'youth', 'income':'medium', 'student':'yes', 'credit_rating':'fair'}
scores = predict(instance)
print("Scores:", scores)
print("Predicted class:", max(scores, key=scores.get))
