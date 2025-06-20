# 📦 End_to_End-DE-project  
**End-to-End Data Engineering Project using Azure & Databricks**

---

## 📂 Project Overview

This project implements an **end-to-end streaming ETL pipeline** for processing Netflix titles data, leveraging **Azure Data Factory (ADF)** for orchestration and **Databricks** for transformation and enrichment. The pipeline follows a **medallion architecture**:  
**Raw → Bronze → Silver → Gold**

---

## 📁 Directory Structure

```
.
├── pipeline1_support_live/           # ADF pipeline support files
│   ├── pipeline/pipeline1.json       # ADF pipeline definition
│   ├── dataset/                      # Datasets used in ADF
│   ├── linkedService/                # Data lake & GitHub connections
│
├── netflix_project/                  # Databricks notebooks
│   ├── 1.AutoLoader.py               # Raw → Bronze (streaming ingest)
│   ├── 2_silver.py                   # Bronze → Silver (cleansing)
│   ├── 3.Lookup notebook.py          # Reference data mapping
│   ├── 4_silver.py                   # Additional Silver transformations
│   ├── 5_lookupNotebook.py           # Dimension lookups
│   ├── 6.weekday.py                  # Adds weekday column
│   ├── DLT notebook - Gold Layer.py  # Silver → Gold layer aggregation
```


---

## ⚙️ Technologies Used

- **Azure Data Lake Storage Gen2** – Storing raw, bronze, silver, and gold data  
- **Azure Data Factory (ADF)** – Orchestration using pipelines and activities  
- **Azure Databricks (PySpark)** – Transformations and streaming ingestion  
- **Structured Streaming + AutoLoader** – Real-time ingestion of new CSVs  
- **Delta Lake** – ACID-compliant data storage format  
- **GitHub Integration** – Version control for pipelines and notebooks  

---

## 🔄 Pipeline Flow

### 1. 🔹 Raw → Bronze
- Handled via `1.AutoLoader.py`  
- Uses `spark.readStream` with `cloudFiles.format = "csv"`  
- Writes ingested data in Delta format to Bronze layer

### 2. 🔸 Bronze → Silver
- Files: `2_silver.py`, `4_silver.py`  
- Cleans nulls, splits columns, casts datatypes  
- Adds derived fields like `Shorttitle`, `duration_minutes`, etc.

### 3. 🧩 Lookups
- Files: `3.Lookup notebook.py`, `5_lookupNotebook.py`  
- Adds metadata from dimension tables (e.g., country/rating mappings)

### 4. 🥇 Silver → Gold
- File: `DLT notebook - Gold Layer.py`  
- Performs final aggregation for reporting (e.g., counts by type)

### 5. ➕ Extras
- `6.weekday.py`: Adds a `weekday` column for release day analysis

---

## 🧩 Azure Data Factory Integration

The folder `pipeline1_support_live/` includes:
- `pipeline1.json` – Full ADF pipeline (ForEach, Web Activity, etc.)  
- Linked Services:
  - `DataLake_connection.json`
  - `github_connection.json`
- Datasets:
  - GitHub resources
  - Validation
  - Sink definitions

---

## 🚀 How to Run the Pipeline

1. **Deploy ADF pipeline** using the exported JSON  
2. **Upload Netflix CSVs** to Azure Data Lake → `raw` container  
3. **Run Databricks notebooks in this order**:
   - `1.AutoLoader.py`
   - `2_silver.py` and `4_silver.py`
   - `3.Lookup notebook.py` and `5_lookupNotebook.py`
   - `DLT notebook - Gold Layer.py`
4. **Visualize** Gold Layer output using:
   - Power BI
   - Databricks SQL Dashboards

---

## 📌 Best Practices Followed

- ✅ Modular notebooks for each pipeline stage  
- ✅ Follows Medallion architecture (Raw → Gold)  
- ✅ Real-time streaming ingestion using AutoLoader  
- ✅ ACID-compliant Delta Lake storage  
- ✅ Parameterized lookups & reusable logic  

---

## 📎 Optional Files

- `manifest.mf`: Manifest file (can be ignored for now)

---

## 🙌 Author

**Srinath Abburi**  
Passionate about cloud data engineering, streaming pipelines, and real-time analytics.

📧 Email: [abburisrinath09@gmail.com](mailto:abburisrinath09@gmail.com)  
🔗 LinkedIn: [https://www.linkedin.com/in/abburi-srinath-59a505281/]

---

> 💡 Feel free to fork, clone, and explore this project. Contributions are welcome!
