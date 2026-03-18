# 📊 DataPulse — Real-Time Financial Transaction Analytics Pipeline

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=for-the-badge&logo=numpy)
![Flask](https://img.shields.io/badge/Flask-API_Layer-black?style=for-the-badge&logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions)
![Big Data](https://img.shields.io/badge/Domain-Financial_Analytics-FF6B35?style=for-the-badge)

> A production-grade ETL data pipeline that processes large-scale financial transaction datasets — extracting, transforming, and loading 1000+ records while generating real-time business insights through an analytics engine and REST API layer.

---

## 🎯 Project Overview

DataPulse is a **scalable financial data pipeline** inspired by real-world banking transaction processing systems. It simulates the end-to-end journey of financial data — from raw transaction generation through ETL processing to actionable business analytics — mirroring the kind of data infrastructure used at large financial institutions.

The system processes **1000+ transactions per pipeline run**, applies multi-stage data transformations, and surfaces insights like category breakdowns, peak spending hours, high-value transaction flags, and user-level analytics — all accessible via a REST API.

---

## 💡 Problem Statement

Large financial institutions process **millions of transactions daily**. Key challenges include:

- **Raw data is messy** — failed transactions, missing fields, inconsistent formats
- **No real-time insights** — analytics lag behind actual transaction activity
- **Manual processing** — time-consuming, error-prone data workflows
- **No centralized API** — insights locked inside scripts, not accessible to other systems

**DataPulse solves all four with an automated ETL pipeline and analytics API.**

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Data Generation** | Python, NumPy, Random | Synthetic financial dataset simulation |
| **ETL Pipeline** | Pandas, NumPy | Extract, Transform, Load processing |
| **Analytics Engine** | Pandas, NumPy | Business insight generation |
| **API Layer** | Flask | REST endpoints to trigger pipeline & serve insights |
| **Containerization** | Docker | Consistent deployment environment |
| **CI/CD** | GitHub Actions | Automated testing & build pipeline |
| **Testing** | Pytest | Unit tests for all pipeline stages |
| **Version Control** | Git + GitHub | Source control & collaboration |

---

## 🏗️ Pipeline Architecture

```
┌─────────────────────────────────────────────────────┐
│                 DataPulse Pipeline                    │
└─────────────────────────────────────────────────────┘

  ┌──────────────┐
  │   EXTRACT     │  ◄── Load raw CSV / simulated transaction stream
  │               │       1000+ records, 7 fields per transaction
  └──────┬────────┘
         │
         ▼
  ┌──────────────┐
  │   TRANSFORM   │  ◄── Clean, validate, enrich data
  │               │       • Remove failed transactions
  │               │       • Parse timestamps → extract month/hour/day
  │               │       • Flag high-value transactions (>₹10,000)
  │               │       • Min-max normalization of amounts
  └──────┬────────┘
         │
         ▼
  ┌──────────────┐
  │     LOAD      │  ◄── Store processed data to output sink
  │               │       (CSV → in production: Redshift / BigQuery)
  └──────┬────────┘
         │
         ▼
  ┌──────────────┐
  │   ANALYTICS   │  ◄── Generate business insights
  │               │       Category breakdown, city stats,
  │               │       peak hours, top users, high-value %
  └──────┬────────┘
         │
         ▼
  ┌──────────────┐
  │   REST API    │  ◄── Serve insights via Flask endpoints
  │               │       POST /pipeline/run | GET /analytics
  └──────────────┘
```

---

## 📊 Analytics Generated

After each pipeline run, DataPulse generates the following insights:

| Insight | Description |
|---|---|
| **Total Volume** | Sum of all successful transaction amounts |
| **Average Transaction** | Mean spend per transaction |
| **Category Breakdown** | Total, count, average spend per category |
| **City-wise Spending** | Transaction volume by city |
| **Peak Hour** | Hour of day with highest transaction activity |
| **High-Value Rate** | % of transactions exceeding ₹10,000 |
| **Top 5 Users** | Highest spending users by total volume |

**Sample Analytics Output:**
```json
{
  "total_transactions": 847,
  "total_volume": 21473829.50,
  "average_transaction": 25353.40,
  "peak_hour": 14,
  "high_value_transactions": 203,
  "high_value_percentage": 23.97,
  "top_5_users": {
    "USR042": 487293.20,
    "USR017": 423819.75,
    "USR088": 401234.50,
    "USR031": 389102.30,
    "USR056": 371849.90
  }
}
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Pipeline health check |
| `POST` | `/pipeline/run` | Trigger full ETL pipeline run |
| `GET` | `/analytics` | Retrieve latest analytics insights |

---

## 🔄 Data Transformation Details

```
Raw Data                          Transformed Data
────────                          ────────────────
transaction_id: TXN000001         transaction_id: TXN000001
timestamp: "2024-03-15 14:23"  →  month: 3
status: "failed"                  day_of_week: "Friday"
amount: 15000.00                  hour: 14
                                  is_high_value: True
                                  amount_normalized: 0.73
                                  [failed records removed]
```

---

## 🚀 CI/CD Pipeline

Every `git push` automatically triggers:

```
Push to GitHub
      │
      ▼
┌──────────────────────┐
│  1. Checkout Code     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  2. Setup Python 3.10 │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  3. Install Deps      │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  4. Run Pytest        │  ◄── ETL + Analytics unit tests
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  5. Build Docker Image│
└──────────────────────┘
```

---

## 🐳 Run with Docker

```bash
# Build the image
docker build -t datapulse-pipeline .

# Run the container
docker run -p 5000:5000 datapulse-pipeline
```

---

## 💻 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/SoumyasreeMitra/datapulse-pipeline.git
cd datapulse-pipeline

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate data and run pipeline
python data_generator.py
python etl_pipeline.py
python analytics.py

# 4. Start the API server
python app.py
```

---

## 📁 Project Structure

```
datapulse-pipeline/
├── app.py                  # Flask API — pipeline trigger & analytics endpoints
├── data_generator.py       # Synthetic transaction dataset generator
├── etl_pipeline.py         # ETL pipeline — Extract, Transform, Load
├── analytics.py            # Analytics engine — insights & reporting
├── requirements.txt        # Project dependencies
├── Dockerfile              # Container configuration
├── test_pipeline.py        # Unit tests for all pipeline stages
├── .gitignore              # Excludes data files and cache
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI/CD pipeline
```

---

## 🌱 Software Engineering Practices Demonstrated

| Practice | Implementation |
|---|---|
| **Big Data Processing** | ETL pipeline processing 1000+ financial records |
| **Data Engineering** | Multi-stage transformation with Pandas + NumPy |
| **Agile / CI/CD** | Automated GitHub Actions pipeline on every push |
| **Application Resiliency** | Error handlers + pipeline health check endpoint |
| **Containerization** | Dockerized for consistent cross-environment runs |
| **RESTful Architecture** | Flask API layer to expose pipeline and analytics |
| **Automated Testing** | Pytest unit tests for all three pipeline stages |
| **Secure Coding** | Structured error handling, environment isolation |

---

## 🔮 Future Enhancements

- [ ] Integrate Apache Spark for distributed processing of 10M+ records
- [ ] Connect to Apache Kafka for real-time transaction stream ingestion
- [ ] Load processed data into PostgreSQL or AWS Redshift data warehouse
- [ ] Add anomaly detection using Isolation Forest for fraud flagging
- [ ] Build Grafana dashboard for real-time pipeline monitoring

---

## 👩‍💻 Author

**Soumyasree Mitra**
- GitHub: [@SoumyasreeMitra](https://github.com/SoumyasreeMitra)
- LinkedIn: [linkedin.com/in/soumyasree-mitra](#)

---

> *Built to demonstrate real-world data engineering skills — from raw transaction ingestion to actionable financial insights — reflecting the kind of large-scale data infrastructure that powers modern financial institutions.*