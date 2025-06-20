# End_to_End-DE-project
End_to_End Data Engineering Project


📂 Project Overview
This project implements an end-to-end streaming ETL pipeline for processing Netflix titles data, leveraging Azure Data Factory (ADF) for orchestration and Databricks for transformation and enrichment. The pipeline follows a medallion architecture: Raw → Bronze → Silver → Gold.



📁 Directory Structure
.
├── pipeline1_support_live/           # ADF pipeline support files
│   ├── pipeline/pipeline1.json       # ADF pipeline definition
│   ├── dataset/                      # Datasets used in ADF
│   ├── linkedService/               # Data lake & GitHub connections
│
├── netflix_project/                 # Databricks notebooks
│   ├── 1.AutoLoader.py              # Raw → Bronze (streaming ingest)
│   ├── 2_silver.py                  # Bronze → Silver (cleansing)
│   ├── 3.Lookup notebook.py         # Reference data mapping
│   ├── 4_silver.py                  # Additional Silver transformations
│   ├── 5_lookupNotebook.py          # Dimension lookups
│   ├── 6.weekday.py                 # Adds weekday column
│   ├── DLT notebook - Gold Layer.py # Silver → Gold layer aggregation


⚙️ Technologies Used
	•	Azure Data Lake Storage (Gen2) – for storing raw/bronze/silver/gold data
	•	Azure Data Factory – for triggering pipelines & activities
	•	Databricks (PySpark) – for notebook-based transformations
	•	Structured Streaming – for ingesting new CSVs via AutoLoader
	•	Delta Lake – for reliable, ACID-compliant table storage
	•	GitHub Integration – for version control of linked services and datasets

⸻

🔄 Pipeline Flow

1. Raw → Bronze
	•	Handled via 1.AutoLoader.py
	•	Uses spark.readStream with .option("cloudFiles.format", "csv")
	•	Writes output to bronze layer in Delta format

2. Bronze → Silver
	•	Files: 2_silver.py, 4_silver.py
	•	Cleans nulls, splits title, casts columns
	•	Enriches data with additional fields like Shorttitle, duration_minutes, etc.

3. Lookups
	•	Files: 3.Lookup notebook.py, 5_lookupNotebook.py
	•	Adds additional metadata using reference data
	•	E.g., country mappings or rating categories

4. Silver → Gold
	•	File: DLT notebook - Gold Layer.py
	•	Aggregates by type, computes counts, and prepares final analytical output

5. Extras
	•	6.weekday.py: Adds weekday column to analyze release patterns

📂 Azure Data Factory Integration

The folder pipeline1_support_live/ contains:
	•	pipeline1.json – full ADF pipeline (ForEach, Web Activity, etc.)
	•	Linked services for:
	•	Azure Data Lake (DataLake_connection.json)
	•	GitHub (github_connection.json)
	•	Datasets including:
	•	Validation
	•	GitHub-hosted resources
	•	Sink dataset definitions

⸻

🚀 How to Run
	1.	Deploy ADF pipeline using the exported JSON.
	2.	Upload raw Netflix CSVs to your Data Lake (raw container).
	3.	Execute Databricks notebooks in order:
	•	1.AutoLoader.py
	•	2_silver.py and 4_silver.py
	•	3.Lookup notebook.py, 5_lookupNotebook.py
	•	DLT notebook - Gold Layer.py
	4.	Visualize gold layer in Power BI or Databricks SQL.

⸻

📌 Best Practices Followed
	•	Medallion architecture with modular notebooks
	•	Autoloader for real-time streaming ingestion
	•	Delta format for reliability and performance
	•	Parameterized lookups and joins for maintainability

⸻

📁 Optional Files
	•	manifest.mf: Manifest file (can be ignored for now)

⸻

🙌 Author

Srinath Abburi
Passionate about cloud data engineering, streaming pipelines, and real-time analytics.
📧 Feel free to connect on gmail: abburisrinath09@gmail.com or LinkedIn : https://www.linkedin.com/in/abburi-srinath-59a505281/
