# Customer Churn Analysis & Prediction

A runnable portfolio project using Python, Pandas, scikit-learn and SQL, with a Power BI dashboard build guide. The included dataset is **synthetic sample data** generated for this project; do not present it as a real company's customer records.

## Project contents
- `data/customer_churn.csv` — 1,500 customer records with a binary `churn` target.
- `src/explore_data.py` — basic EDA and chart export.
- `src/train_model.py` — preprocessing pipeline, Random Forest training and evaluation.
- `src/predict_customer.py` — example prediction using the saved model.
- `sql/churn_analysis.sql` — PostgreSQL analysis queries.
- `powerbi/POWER_BI_GUIDE.md` — dashboard layout, measures and import steps.

## Run on Windows PowerShell
```powershell
cd customer_churn_analysis_prediction
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python src/explore_data.py
python src/train_model.py
python src/predict_customer.py
```
If script activation is blocked, run `Set-ExecutionPolicy -Scope Process RemoteSigned` in that PowerShell window, then activate again. You can also skip activation and use `.venv\Scripts\python.exe`.

## SQL
Create a PostgreSQL database, import `data/customer_churn.csv` into a table named `customers` (use the CSV header as column names), then execute `sql/churn_analysis.sql`. The queries use PostgreSQL syntax.

## Power BI
Follow `powerbi/POWER_BI_GUIDE.md`. Import the CSV directly with **Get Data → Text/CSV**. Create the measures in the guide and build the visuals. Refresh after replacing the CSV.

## Model notes
The model uses a held-out 20% test split and reports precision, recall, F1 and ROC-AUC. Churn is imbalanced, so inspect recall and the confusion matrix rather than relying on accuracy alone. The sample prediction is illustrative, not a business decision.
