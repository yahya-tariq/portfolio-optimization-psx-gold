# Portfolio Optimization: PSX Stocks & Gold

This project analyzes portfolio risk-return dynamics using PSX-listed stocks and gold data, applying Modern Portfolio Theory to compare equal-weighted and optimized portfolios. The goal is to demonstrate how strategic asset allocation can improve performance using historical data and quantitative methods.

## 🔧 Tools & Technologies
- **Microsoft Excel** – Portfolio modeling, return & risk calculations, Sharpe Ratio, scenario and drawdown analysis
- **Power BI** – Interactive dashboards for visualizing efficient frontier, risk-return metrics (used in final presentation)
- **Python** – Data preprocessing using `fix_prices.py`
- **PSX & Gold data** – Sourced manually and structured for analysis

## 📊 Key Outcomes
- Sharpe Ratio improved from **0.27 to 0.57** by optimizing portfolio weights
- Included **drawdown analysis** to evaluate downside risk and **scenario-based analysis** to test portfolio performance under extreme conditions

## 📂 Folder Structure
- `data/` – Raw and cleaned price data
  - `ClosingPricesData.xlsx` – Original PSX and gold prices
  - `processed_closingpricesdata.xlsx` – Cleaned data used for modeling
- `analysis/` – Excel file containing portfolio optimization, return-risk metrics, drawdown analysis, and scenario testing
  - `FDA_Project.xlsx`
- `code/` – Python script for preprocessing price data
  - `fix_prices.py`
- `report/` – Final project report
  - `ProjectReport.docx`, `ProjectReport.pdf`

## ✅ Features
- Comparison of equal-weighted vs. optimized portfolios
- Modern Portfolio Theory applied to real financial data
- **Drawdown analysis** for downside risk understanding
- **Scenario-based stress testing** for performance under market shocks
- Sharpe Ratio and efficient frontier visualization
