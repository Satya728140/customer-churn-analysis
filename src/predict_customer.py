from pathlib import Path
import joblib
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
model = joblib.load(ROOT/"models/churn_model.joblib")
sample = pd.DataFrame([{
    "gender":"Female", "senior_citizen":0, "partner":"No", "dependents":"No",
    "tenure_months":4, "phone_service":"Yes", "internet_service":"Fiber optic",
    "online_security":"No", "tech_support":"No", "contract":"Month-to-month",
    "paperless_billing":"Yes", "payment_method":"Electronic check",
    "monthly_charges":99.5, "total_charges":398.0
}])
p = model.predict_proba(sample)[0,1]
print(f"Predicted churn probability: {p:.1%}")
print("Prediction:", "LIKELY TO CHURN" if p >= .5 else "LIKELY TO STAY")
