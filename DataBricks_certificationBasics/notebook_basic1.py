# Databricks notebook source
print('''hi
''')
## basic python print 

# COMMAND ----------

# MAGIC %sql
# MAGIC ## basic sql running
# MAGIC select " select hi from sql"

# COMMAND ----------

## run one notebook from another for modularity of code 
%run ./DataBricks_certificationBasics/notebookBasic2
print(a)

# COMMAND ----------

# MAGIC %md
# MAGIC # "#" used for title
# MAGIC ## "##" for title 2
# MAGIC ### " ###" for title 3 used fro heading heiarchy 

# COMMAND ----------

## it will list file system in default loaction 
%fs ls '/databricks-datasets'


# COMMAND ----------

## show help in dbutils 
dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls('/databricks-datasets')

# COMMAND ----------

## using display function 
files = dbutils.fs.ls('/databricks-datasets')
display(files)
