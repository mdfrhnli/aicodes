import pandas as pd
import numpy as np

data = pd.DataFrame({
    'Gender': ['male','male','male','male','female','female','female','female'],
    'Height': [6,5.92,5.58,5.92,5,5.5,5.42,5.75],
    'Weight': [180,190,170,165,100,150,130,150],
    'Foot_Size': [12,11,12,10,6,8,7,9]
})

person = pd.DataFrame({'Height':[6], 'Weight':[130], 'Foot_Size':[8]})

priors = data['Gender'].value_counts(normalize=True)
means = data.groupby('Gender').mean()
vars_ = data.groupby('Gender').var()

def gaussian(x, mean, var):
    var = var if var > 1e-6 else 1e-6
    return (1 / np.sqrt(2*np.pi*var)) * np.exp(-((x-mean)**2) / (2*var))

probs = {}
for gender in priors.index:
    prob = priors[gender]
    for feature in person.columns:
        prob *= gaussian(person[feature][0], means.loc[gender, feature], vars_.loc[gender, feature])
    probs[gender] = prob

print("Posterior scores:", probs)
print("Predicted gender:", max(probs, key=probs.get))
