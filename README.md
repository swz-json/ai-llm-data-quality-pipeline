#  AI‑Powered E‑commerce Data Quality Pipeline

 **Enterprise‑grade data pipeline demonstrating how modern data teams ensure data trust, analytics reliability, and business‑ready insights using automated processing and AI‑assisted validation.**

---

##  Overview

This project implements an **end‑to‑end data quality and analytics pipeline** for an e‑commerce use case. It simulates how real‑world data engineering teams ingest raw operational data, clean and validate it at scale, enrich it with AI‑based reasoning, and expose actionable insights through an interactive dashboard.

The pipeline goes beyond traditional rule‑based checks by integrating a **Large Language Model (LLM)** to generate **executive‑level data quality reports**, anomaly explanations, and business impact assessments.

---

##  High‑Level Architecture

```
Raw Data (CSV / API)
        ↓
Ingestion Layer
        ↓
Cleaning & Standardization
        ↓
Rule‑Based Data Quality Checks
        ↓
LLM‑Based Validation & Reporting
        ↓
Analytics‑Ready Dataset
        ↓
Streamlit Dashboard
```

 **Interactive architecture & UI design** are documented in Figma:
👉 *Dashboard & Architecture – Figma link*  -> [🔗 Figma – Dashboard & Architecture](https://www.figma.com/make/v0DRrtrvwKEjx9iA1PZjNa/Confetti-Explosion-on-Click?node-id=0-1&p=f&t=FtZFFkbh4LwivS3J-0&fullscreen=1)


---

## Key Objectives

* Ensure **data reliability and consistency** across e‑commerce datasets
* Detect and explain **data quality issues** before analytics consumption
* Bridge the gap between **technical validation** and **business understanding**
* Demonstrate production‑oriented **data engineering best practices**

---

##  Core Features

###  1. Automated Data Ingestion

* Secure loading of **customers, products, and orders** datasets
* Schema alignment and data type standardization
* Designed to be schedulable (batch‑ready)

---
###  2. Data Cleaning & Quality Enforcement

* Detection of missing and invalid values
* Identification of price, quantity, and date anomalies
* Outlier detection and removal
* Generation of a **clean, analytics‑ready dataset**

---

###  3. LLM‑Based Data Validation (OpenAI GPT‑4)

The LLM automatically generates:

* Executive summary of data quality
* List of detected anomalies
* Root‑cause hypotheses
* Business impact estimation
* Actionable recommendations

**Example output:**

> *Data conformity rate: 94.8% (+2.1%).*
> *47 anomalies detected, mainly related to inconsistent quantities and missing values.*

This layer demonstrates how AI can **augment data governance and observability**.

---

###  4. Interactive Analytics Dashboard (Streamlit)

**KPIs displayed:**

* Active customers
* Total orders
* Revenue
* Conversion rate
* Global data quality score

**Visualizations:**

* Sales trends over time
* Detected anomalies table
* Cleaned orders preview

The dashboard is designed for **data analysts, business stakeholders, and managers**.

---

## Data Schema (Simplified)

**Orders**

* `order_id` (int)
* `customer_id` (int)
* `product_id` (int)
* `quantity` (int)
* `price` (float)
* `order_date` (datetime)

**Customers**

* `customer_id` (int)
* `name` (string)
* `email` (string)
* `country` (string)

**Products**

* `product_id` (int)
* `category` (string)
* `unit_price` (float)

---

##  How to Run the Project

### Install dependencies

```bash
pip install -r requirements.txt
```

### Execute the pipeline

```bash
python pipelines/ingest.py
python pipelines/clean.py
python pipelines/llm_validation.py
```

###  Launch the dashboard

```bash
streamlit run app/dashboard.py
```

---

## Testing & Data Quality Assurance

* Unit tests for ingestion, cleaning, and validation steps
* Data sanity checks (nulls, ranges, outliers)
* Validation of LLM outputs before dashboard exposure

Tests are included to ensure **pipeline robustness and reproducibility**.

---

##  Tech Stack

* **Python 3.10+**
* **Pandas / NumPy** — data processing
* **Streamlit** — analytics dashboard
* **OpenAI GPT‑4** — data quality validation & narrative reporting
* **Matplotlib / Plotly** — visualizations
* **Figma** — architecture & UI documentation ->  
---

## Production‑Ready Design (Conceptual)

While this repository runs locally, it is designed with production extension in mind:

* Scheduling via **Airflow / Prefect**
* Storage in **S3 / Delta Lake**
* Asynchronous LLM validation (batch or event‑driven)
* Containerized deployment (Docker)
* Dashboard deployment via **Streamlit Cloud**

This reflects **real‑world data platform architecture patterns**.

---

## 📈 Sample LLM Results

**Detected anomalies:**

* Quantity inconsistencies: 21
* Missing values: 18
* Outliers: 8

**Recommendation:**

> Review data entry workflows for high‑value products and implement automated thresholds for critical quantities.

---

## 👤 Author

**Wassim Elmoufakkir**
MSc Data Engineering for Artificial Intelligence

* 💼 LinkedIn: [https://www.linkedin.com/in/wassim-elmoufakkir/](https://www.linkedin.com/in/wassim-elmoufakkir/)
* 💻 GitHub: [https://github.com/swz-json](https://github.com/swz-json)

---

##  Why This Project Matters

My project demonstrates:

* Strong **data engineering fundamentals**
* Practical and responsible **LLM integration**
* Business‑oriented thinking beyond raw data processing
* Clear communication through dashboards and narratives

It reflects how modern data teams **build trust in data before driving decisions**.

