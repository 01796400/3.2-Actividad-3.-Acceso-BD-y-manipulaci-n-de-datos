import pandas as pd
import sqlalchemy as sqla

# Conectar a la base de datos (reutilizando la conexión)
db = sqla.create_engine('mysql+pymysql://mnaTC4029User:mnaTC4029Pass!@20.106.217.214:3306/classicmodels', pool_recycle=3600)
conn = db.connect()

# Cargar las tablas en dataframes
df_products = pd.read_sql("SELECT * FROM products", conn)
df_productlines = pd.read_sql("SELECT * FROM productlines", conn)
df_employees = pd.read_sql("SELECT * FROM employees", conn)
df_offices = pd.read_sql("SELECT * FROM offices", conn)
df_customers = pd.read_sql("SELECT * FROM customers", conn)
df_payments = pd.read_sql("SELECT * FROM payments", conn)
