# Databricks notebook source
# MAGIC %md
# MAGIC # Array parameter

# COMMAND ----------

files = [
    {
        "sourcefolder" : "netflix_directors",
        "targetfolder" : "netflix_directors"
    },
    {
        "sourcefolder" : "netflix_cast",
        "targetfolder" : "netflix_cast"
    },
    {
        "sourcefolder" : "netflix_category",
        "targetfolder" : "netflix_category"
    },
    {
        "sourcefolder" : "netflix_countries",
        "targetfolder" : "netflix_countries"
    }
]

# COMMAND ----------

# MAGIC %md
# MAGIC ### Jon Utility to return the array

# COMMAND ----------

dbutils.jobs.taskValues.set(key = "my_arr", value = files)

# COMMAND ----------

