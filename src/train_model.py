from pathlib import Path
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data/customer_churn.csv")
X = df.drop(columns=["customer_id", "churn"])
y = df["churn"]
cat = X.select_dtypes(include="object").columns.tolist()
num = X.select_dtypes(exclude="object").columns.tolist()
prep = ColumnTransformer([
    ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), num),
    ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), cat)
])
model = Pipeline([("prep", prep), ("classifier", RandomForestClassifier(n_estimators=300, class_weight="balanced", random_state=42))])
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2,random_state=42,stratify=y)
model.fit(X_train,y_train)
pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:,1]
print(classification_report(y_test,pred))
print("ROC-AUC:", round(roc_auc_score(y_test,proba),3))
print("Confusion matrix:\n", confusion_matrix(y_test,pred))
(ROOT/"models").mkdir(exist_ok=True)
joblib.dump(model, ROOT/"models/churn_model.joblib")
print("Saved models/churn_model.joblib")
