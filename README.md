# NovaMart Enterprise BI & Analytics Platform

![Dashboard Preview](images/dashboard_demo.gif)

*If the GIF does not load, view the [Static Dashboard Screenshot](images/dashboard_final.png) or the [PDF Preview](NovaMart_BI_Platform.pdf).*

## Project Overview
An end-to-end Business Intelligence solution engineered for a simulated global retail company. This project replaces disjointed departmental spreadsheets with a centralized Star Schema data model serving as the single source of truth. to track revenue, profitability margins, and Year-over-Year growth.

**Tools Used:** Excel Power Query (M), Power Pivot, Data Modeling, DAX, Advanced CUBE Functions.

---

## The Business Problem
The NovaMart C-suite was relying on fragmented reports causing conflicting data in executive meetings. They lacked visibility into true regional performance, active product margins, and historical time-intelligence tracking. The objective was to build an interactive executive dashboard entirely independent of vulnerable flat-file PivotTables.

---

## Solution Architecture

### 1. ETL & Data Engineering (Power Query)
Processed approximately 85,000+ transactional records of raw, dirty transactional data.
* Standardized inconsistent categorical text and resolved data type formatting.
* Identified 96 orphan Customer IDs through a Left Anti Join, preserving financial totals while exposing data-quality issues in the simulated source system.
* Handled duplicate primary keys and null financial values prior to model loading.

### 2. Data Modeling (Power Pivot)
Abandoned flat-file reporting to architect a highly efficient Star Schema utilizing the VertiPaq memory engine.
* Built a dedicated `Dim_Calendar` table for contiguous Time Intelligence calculations.
* Established strict 1-to-Many cross-filter relationships flowing from Dimension tables to the central `Fact_Sales` table.

![Star Schema Data Model](images/data_model.png)

### 3. Analytical Engine (DAX)
Wrote explicit DAX measures to calculate dynamic business logic, ensuring reusability across the enterprise model.
* **Iterators:** Utilized `SUMX` for row-by-row transactional evaluation (e.g., Gross Revenue = Quantity * List Price).
* **Safe Division:** Implemented `DIVIDE` to prevent Zero-Denominator errors in margin percentages.
* **Time Intelligence:** Leveraged `CALCULATE` paired with `SAMEPERIODLASTYEAR` and `TOTALYTD` for advanced context transition to calculate YoY Growth and Accumulating targets.

### 4. Presentation Layer (CUBE Functions & UI)
Designed an application-like Executive Dashboard focused on immediate high-level insights.
* Engineered KPI cards using `CUBEVALUE` functions, extracting DAX measures directly from the internal model to bypass fragile PivotTable layouts.
* Synchronized global Timeline and Slicer controls to filter multiple distinct objects simultaneously.

---

## Features

- Interactive Executive Dashboard
- Dynamic KPI Cards
- Timeline Filtering
- Multi-Slicer Synchronization
- Star Schema Data Model
- Time Intelligence
- Revenue Trend Analysis
- Regional Performance Analysis
- Category Profitability Analysis
- Python-based Synthetic Data Generator

---

## Repository Structure

```text
NovaMart-Enterprise-BI-Platform
│
├── NovaMart_Raw_Datasets/
│   ├── Raw_Dim_Customer.csv
│   ├── Raw_Dim_Product.csv
│   ├── Raw_Dim_Region.csv
│   └── Raw_Fact_Sales.csv
│
├── images/
│   ├── dashboard_demo.gif
│   ├── dashboard_final.png
│   └── data_model.png
│
├── NovaMart_BI_Platform.xlsx
├── NovaMart_BI_Platform.pdf
├── data_generator.py
└── README.md
```

---

## Key Business Insights
1. **Top Driver:** North America generated the highest raw Net Revenue volume.
2. **Profitability:** While Electronics drive volume, the Furniture category yielded the highest Gross Profit Margin at over 38%.
3. **Data Governance:** The ETL process revealed critical gaps in the source CRM system, identifying millions in revenue tied to unassigned Customer IDs, highlighting the need for stricter front-end data validation.

---
*Disclaimer: All data within this project is synthetically generated via Python for demonstration purposes.*
