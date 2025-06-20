# Databricks notebook source
# Cell 1
var = dbutils.jobs.taskValues.get(
    taskKey="weekday_lookup",
    key="week_day",
    debugValue="default_value"
)

# Cell 2
print(var)

# COMMAND ----------

print(var)