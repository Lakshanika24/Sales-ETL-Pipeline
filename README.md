# 📊 Sales ETL Pipeline using Apache Airflow

## 📌 Project Overview
This project is a simple ETL (Extract, Transform, Load) pipeline built using Apache Airflow.  
It automates daily processing of sales data using a Python script.

---

## 🛠️ Tech Stack
- Apache Airflow
- Python
- Docker
- BashOperator / PythonOperator

---

## ⚙️ Workflow
The pipeline performs the following steps:

1. **Extract** → Read or collect sales data  
2. **Transform** → Clean and process the data  
3. **Load** → Store or save processed data  

---

## 📁 Project Structure

Airflow_ETL_Pipeline/
│
├── dags/
│ └── sales_etl_pipeline.py # Airflow DAG file
│
├── scripts/
│ └── etl.py # ETL logic in Python
│
├── docker-compose.yml # Airflow setup
└── README.md


---

## How to Run the Project

### Step 1: Start Airflow
```bash
docker-compose up -d
Step 2: Open Airflow UI
http://localhost:8080
Step 3: Trigger DAG
Enable DAG: sales_etl_pipeline
Click Trigger DAG
 DAG Details
DAG Name: sales_etl_pipeline
Schedule: Daily (@daily)
Task: Runs ETL Python script
👩‍💻 Author

Keerthana Thangaraj
