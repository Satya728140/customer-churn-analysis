from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data/customer_churn.csv")
print(df.head())
print("\nChurn rate:", round(df.churn.mean()*100,2), "%")
print(df.groupby("contract").churn.mean().sort_values(ascending=False))
ax=df.groupby("contract").churn.mean().mul(100).plot(kind="bar", title="Churn rate by contract")
ax.set_ylabel("Churn rate (%)")
plt.tight_layout()
(ROOT/"outputs").mkdir(exist_ok=True)
plt.savefig(ROOT/"outputs/churn_by_contract.png", dpi=150)
print("Saved outputs/churn_by_contract.png")
