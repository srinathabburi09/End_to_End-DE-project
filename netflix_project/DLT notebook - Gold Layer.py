# Databricks notebook source
#we cannot run dlt tables in normal clusters we require job clusters to run
looktable_rules = {
    "rule1" : "show_id is NOT NULL"
} 

# COMMAND ----------

@dlt.table(
    name = "gold_netflixdirector"
)

@dlt.expect_all_or_drop(looktable_rules)
def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@srinath09datalake.dfs.core.windows.net/netflix_director")

# COMMAND ----------

@dlt.table(
    name = "gold_netflixdirector"
)

@dlt.expect_all_or_drop(looktable_rules)
def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@srinath09datalake.dfs.core.windows.net/netflix_director")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflixcast"
)

@dlt.expect_all_or_drop(looktable_rules)
def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@srinath09datalake.dfs.core.windows.net/netflix_cast")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflixcountries"
)

@dlt.expect_all_or_drop(looktable_rules)
def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@srinath09datalake.dfs.core.windows.net/netflix_countries")
    return df

# COMMAND ----------

@dlt.table(
    name = "gold_netflixcategory"
)

@dlt.expect_all_or_drop(looktable_rules)
def myfunc():
    df = spark.readStream.format("delta").load("abfss://silver@srinath09datalake.dfs.core.windows.net/netflix_category")

# COMMAND ----------

@dlt.table


def gold_stg_netflixtitles():
    df = spark.readStream.format("delta").load("abfss://silver@srinath09datalake.dfs.core.windows.net/netflix_titles")
    return df

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

@dlt.views

def gold_trns_netflixtitles():
    df = spark.readStream.table("LIVE.gold_stg_netflixtitles")
    df = df.withColumn("newflag",lit(1))
    return df


# COMMAND ----------

masterdata_rules = {
    "rule1" : "newflag is NOT NULL"
    "rule2" : "show_id is NOT NULL"
}

# COMMAND ----------

@dlt.table


@dlt.expect_all_or_drop(masterdata_rules)
def gold_netflixtitles:
    df = spark.readStream.table("LIVE.gold_trns_netflixtitles")
    return df