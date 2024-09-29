import pandas as pd
import sqlalchemy as sqla

# Conectar a la base de datos
db = sqla.create_engine('mysql+pymysql://mnaTC4029User:mnaTC4029Pass!@20.106.217.214:3306/classicmodels', pool_recycle=3600)
conn = db.connect()

# Cargar las tablas en dataframes
df_products = pd.read_sql("SELECT * FROM products", conn)
df_productlines = pd.read_sql("SELECT * FROM productlines", conn)
df_employees = pd.read_sql("SELECT * FROM employees", conn)
df_offices = pd.read_sql("SELECT * FROM offices", conn)
df_customers = pd.read_sql("SELECT * FROM customers", conn)
df_payments = pd.read_sql("SELECT * FROM payments", conn)

# Consulta 1: Líneas de productos
print("\nConsulta 1: Líneas de productos")
print(df_productlines)

# Consulta 2: Empleados ordenados por nombre
print("\nConsulta 2: Empleados ordenados por nombre")
print(df_employees.sort_values(by='firstName'))

# Consulta 3: Países donde hay oficinas (sin duplicar)
print("\nConsulta 3: Países donde hay oficinas")
print(df_offices['country'].unique())

# Consulta 4: Nombre y teléfono de los clientes de Nueva York (NYC)
print("\nConsulta 4: Clientes de Nueva York")
print(df_customers[df_customers['city'] == 'NYC'][['customerName', 'phone']])

# Consulta 5: Productos de Gearbox Collectibles con menos de 1000 unidades
print("\nConsulta 5: Productos de Gearbox Collectibles con menos de 1000 unidades")
print(df_products[(df_products['productVendor'] == 'Gearbox Collectibles') & (df_products['quantityInStock'] < 1000)][['productCode', 'productName']])

# Consulta 6: Tres productos más caros
print("\nConsulta 6: Tres productos más caros")
print(df_products[['productName', 'buyPrice']].sort_values(by='buyPrice', ascending=False).head(3))

# Consulta 7: Cantidad de productos por línea de producto
print("\nConsulta 7: Cantidad de productos por línea de producto")
print(df_products.groupby('productLine').size())

# Consulta 8: Cantidad de empleados por país (tomando en cuenta la ubicación de la oficina)
print("\nConsulta 8: Cantidad de empleados por país")
df_merged = pd.merge(df_employees, df_offices, on='officeCode')
print(df_merged.groupby('country').size())

# Consulta 9: Promedio de pagos de clientes de España
print("\nConsulta 9: Promedio de pagos de clientes de España")
df_spain_customers = df_customers[df_customers['country'] == 'Spain']
df_spain_payments = pd.merge(df_spain_customers, df_payments, on='customerNumber')
print(df_spain_payments['amount'].mean())
