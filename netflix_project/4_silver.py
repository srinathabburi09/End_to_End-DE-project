# Databricks notebook source
# MAGIC %md
# MAGIC # Silver Data Transformation

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

df = spark.read.format("delta")\
        .option("header", True)\
        .option("inferSchema", True)\
        .load("abfss://bronze@srinath09datalake.dfs.core.windows.net/netflix_titles")

    

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.fillna({"duration_minutes" : 0, "duration_seasons" : 1})

df.display()

# COMMAND ----------

df = df.withColumn("duration_minutes", col("duration_minutes").cast(IntegerType()))\
            .withColumn("duration_seasons", col("duration_seasons").cast(IntegerType()))
#Converts the duration_minutes and duration_seasons columns to integer type using cast function

# COMMAND ----------

#schema of df using printSchema function
df.printSchema()

#from the schema we can see that the selected columns from the above cell are converted from strins to integers and as well as no nulls presents

# COMMAND ----------

df.display()

#why these all are in strings? basically the extracted is CSV,so that all the data is in String format for duration_minutes,duration_seasons,etc

# COMMAND ----------

#dividing title by : this as a split
from pyspark.sql.functions import split, col; 
df = df.withColumn("Shorttitle", split(col("title"), ":").getItem(0))
df.display()

# COMMAND ----------

#splitting by - in rating change that column to rating(same column by splitting on -)
df = df.withColumn("rating", split(col('rating'), '-').getItem(0))
df.display()

# COMMAND ----------

df = df.withColumn(
    "type_flag",
    when(col("type") == "Movie", 1)
    .when(col("type") == "TV Show", 2)
    .otherwise(0)
)

display(df)

#Conditional Statements
#nwe_column = type_flag, if type is movie we set type_flag of movie as 1 and for Tv_show is 2 and others simply 0, Just like if,elif and else

# COMMAND ----------

from pyspark.sql.window import Window

# COMMAND ----------

#window function
#ranks the data in decending orders based on the duration_minutes("desc()") - function
#to rank in ascending type without .desc
#dense_rank is a function lets say 	•	It gives the same rank to equal values.
#•	But does NOT skip the next rank — it continues sequentially.

df = df.withColumn(
    "duration_ranking",
    dense_rank().over(Window.orderBy(col('duration_minutes').desc()))
)



# COMMAND ----------

df.display()

# COMMAND ----------

#converting the dataframe into temporary sql table
#we cannot use this table Globally as these are session_scoped tables and only acquire with the current pyspark notebook
df.createOrReplaceTempView("temp_view")

# COMMAND ----------

#To use a temp_views Globally, works outside the notebook but Once the session is expired,these will be terminated
df.createOrReplaceGlobalTempView("Global_view")

# COMMAND ----------

#selecting all the columns and rows from temp_view using spark.sql function
df = spark.sql("""
               select * from temp_view;
               """)

df.display()

# COMMAND ----------

#This is a global view tables which can be used globally
df = spark.sql("""
               select * from global_temp.Global_view
               """)
display(df)

# COMMAND ----------

#To visualize the data simply click on the output console > +(click) > select visualization

# COMMAND ----------

#Aggregate Function - performs calculation on similar group of values
#groupby("type") - like movies, tv, null etc 
#agg - counts the number movies,tv's, null by groups and will be saved as total_count
df_visualization = df.groupby("type").agg(count('*').alias("total_count"))
df_visualization.display()

# COMMAND ----------

df.display()

# COMMAND ----------

df.write.format("delta")\
        .mode("overwrite")\
        .option("path","abfss://silver@srinath09datalake.dfs.core.windows.net/netflix_titles")\
        .save()
