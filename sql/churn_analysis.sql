-- Run after importing data/customer_churn.csv into a table named customers.
-- PostgreSQL syntax.
-- 1. Overall churn KPI
SELECT COUNT(*) AS customers,
       SUM(churn) AS churned_customers,
       ROUND(100.0 * SUM(churn) / NULLIF(COUNT(*),0), 2) AS churn_rate_pct
FROM customers;

-- 2. Churn by contract
SELECT contract, COUNT(*) AS customers,
       SUM(churn) AS churned,
       ROUND(100.0 * SUM(churn) / COUNT(*),2) AS churn_rate_pct
FROM customers GROUP BY contract ORDER BY churn_rate_pct DESC;

-- 3. Churn by tenure band
SELECT CASE WHEN tenure_months < 12 THEN '0-11 months'
            WHEN tenure_months < 24 THEN '12-23 months'
            WHEN tenure_months < 48 THEN '24-47 months'
            ELSE '48+ months' END AS tenure_band,
       COUNT(*) AS customers, ROUND(100.0*AVG(churn),2) AS churn_rate_pct
FROM customers GROUP BY 1 ORDER BY 1;

-- 4. Revenue at risk (monthly charges of churned customers)
SELECT ROUND(SUM(monthly_charges),2) AS monthly_revenue_at_risk
FROM customers WHERE churn = 1;

-- 5. Churn by payment method
SELECT payment_method, COUNT(*) AS customers,
       ROUND(100.0*AVG(churn),2) AS churn_rate_pct
FROM customers GROUP BY payment_method ORDER BY churn_rate_pct DESC;
