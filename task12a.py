# pip install scikit-learn pandas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score

# Replace this with pd.read_csv('your_UCI_csv_link') if you have direct CSV link
from sklearn.datasets import load_diabetes
X_raw = load_diabetes()
X = pd.DataFrame(X_raw.data, columns=X_raw.feature_names)
y = (X_raw.target > X_raw.target.mean()).astype(int)  # binarize as example

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt = DecisionTreeClassifier(max_depth=5)
rf = RandomForestClassifier(n_estimators=100)

for model in [dt, rf]:
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(model.__class__.__name__, "accuracy:", accuracy_score(y_test, preds))
    print(classification_report(y_test, preds))
