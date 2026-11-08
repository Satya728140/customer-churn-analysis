# Power BI Dashboard Guide — Customer Churn

## 1. Load data
Power BI Desktop → Get Data → Text/CSV → `data/customer_churn.csv` → Transform Data. Set `churn` and `senior_citizen` to Whole Number; charges to Decimal Number; other fields to Text. Select Close & Apply.

## 2. Create DAX measures
```DAX
Total Customers = COUNTROWS(customers)
Churned Customers = CALCULATE(COUNTROWS(customers), customers[churn] = 1)
Churn Rate = DIVIDE([Churned Customers], [Total Customers], 0)
Monthly Revenue = SUM(customers[monthly_charges])
Revenue at Risk = CALCULATE([Monthly Revenue], customers[churn] = 1)
Average Tenure = AVERAGE(customers[tenure_months])
```
Format `Churn Rate` as Percentage.

## 3. Suggested one-page layout
- KPI cards: Total Customers, Churned Customers, Churn Rate, Revenue at Risk.
- Clustered column chart: Contract on Axis, Churn Rate as Values.
- Bar chart: Payment Method on Axis, Churn Rate as Values.
- Donut: Churn (0/1) by customer count.
- Scatter: Tenure Months vs Monthly Charges; Legend = Churn.
- Slicers: Contract, Internet Service, Payment Method, Tech Support.

## 4. Questions to explain in a presentation
- Which contract group has the highest churn rate?
- Does short tenure correlate with churn?
- Which customer segments contribute most to monthly revenue at risk?
- What retention actions could be tested (e.g., onboarding outreach or contract incentives)?

## 5. Publish
Save as `Customer_Churn_Dashboard.pbix`. If publishing to Power BI Service, verify workspace permissions and refresh credentials.
