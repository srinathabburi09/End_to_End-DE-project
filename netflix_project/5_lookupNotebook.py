# Databricks notebook source
# MAGIC %md
# MAGIC ### Parameter

# COMMAND ----------

dbutils.widgets.text("week_day", "7")


# COMMAND ----------

# MAGIC %md
# MAGIC ### Variable

# COMMAND ----------

var = int(dbutils.widgets.get("week_day"))


# COMMAND ----------

dbutils.jobs.taskValues.set(key="week_day", value=var)