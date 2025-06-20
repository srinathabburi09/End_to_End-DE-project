# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Notebook Lookup tables
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Parameters

# COMMAND ----------

dbutils.widgets.text("sourcefolder", "netflix_directors")
dbutils.widgets.text("targetfolder","netflix_directors")

# COMMAND ----------

# MAGIC %md
# MAGIC ### variables

# COMMAND ----------

var_src_folder = dbutils.widgets.get("sourcefolder")
var_trg_folder = dbutils.widgets.get("targetfolder")

# COMMAND ----------

print(var_src_folder)
print(var_trg_folder)

# COMMAND ----------

df = spark.read.format("csv")\
        .option("header", True)\
        .option("inferSchema", True)\
        .load(f"abfss://bronze@srinath09datalake.dfs.core.windows.net/{var_src_folder}")

        

# COMMAND ----------

df.display()

# COMMAND ----------

df.write.format("delta")\
        .mode("append")\
        .option("path",f"abfss://silver@srinath09datalake.dfs.core.windows.net/{var_trg_folder}")\
        .save()
