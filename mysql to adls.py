# Databricks notebook source
import json

# Databricks scope name pointing to Key Vault secret
scope_name = "key-vault-136"
#MySQL credentials stored in Azure Key Vault as a secret
mysql_secret_name = "mysql-db"

#ADLS access key stored in Azure Key Vault as a secret
adls_secret_name="adls-accesskey"


