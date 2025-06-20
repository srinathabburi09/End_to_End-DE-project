# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Incremental Data Loading using Autoloader

# COMMAND ----------

#create a check_point_location to store the schema from the Bronze phase
check_point_location = "abfss://silver@srinath09datalake.dfs.core.windows.net/checkpoint"

# COMMAND ----------

df = (
    spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "csv")
    .option("cloudFiles.schemaLocation", check_point_location)
    .load("abfss://raw@srinath09datalake.dfs.core.windows.net")
)

display(df)    

# spark.readStream - Initiates a streaming DataFrame to continuously read new data as it arrives.
# format("cloudFiles") - Uses Databricks Autoloader, optimized for streaming new files from cloud storage like ADLS Gen2.
# option("cloudFiles.format", "csv") - Specifies the format of incoming files. In this case, we expect CSV files.
# option("cloudFiles.schemaLocation", check_point_location) - Path where Spark stores the schema metadata. 
# This is often considered part of the silver zone in the medallion architecture but technically just a schema checkpoint path.
#load(...) - Specifies the raw layer location in your Data Lake (e.g., abfss://raw@...). 
#This is where new CSV files will land and be picked up automatically by Autoloader.

# COMMAND ----------

df.writeStream\
  .option("checkpointLocation", check_point_location)\
  .trigger(processingTime= "10 seconds")\
  .start("abfss://bronze@srinath09datalake.dfs.core.windows.net/netflix_titles")

#write stream is used to write the data to the bronze layer and continuesly writes the data
#trigger is used to specify the time interval for the stream to process the data
#start is used to start the stream from the bronze layer

# COMMAND ----------

#	1.	Reading streaming CSV files from the raw layer (readStream)
#	2.	Writing those in near real-time (every 10 seconds) to the Bronze zone
#	3.	Keeping track of what’s already written using checkpointLocation

# COMMAND ----------

#data ingestion