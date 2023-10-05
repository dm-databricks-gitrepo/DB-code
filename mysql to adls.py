# Databricks notebook source
import json

# Databricks scope name pointing to Key Vault secret
scope_name = "key-vault-136"
#MySQL credentials stored in Azure Key Vault as a secret
mysql_secret_name = "mysql-db"

#ADLS access key stored in Azure Key Vault as a secret
adls_secret_name="adls-accesskey"



# COMMAND ----------

# Retrieve MySQL credentials from Azure Key Vault using the provided scope_name and mysql_secret_name
secret = dbutils.secrets.get(scope_name, mysql_secret_name)

# Parse the retrieved secret as JSON to access the individual credentials
mssql_cred = json.loads(secret)

host=mssql_cred["host"]
port=mssql_cred["port"]
user=mssql_cred["user"]
password=mssql_cred["password"]


# COMMAND ----------

# Retrieving data from a MySQL table


mysql_table_df = (spark.read
  .format("mysql")
  .option("dbtable", 'employees')
  .option("host", host)
  .option("port", port)
  .option("database", 'my_db')
  .option("user",user)
  .option("password", password)
  .load()
)
display(mysql_table_df)

print("hello")
