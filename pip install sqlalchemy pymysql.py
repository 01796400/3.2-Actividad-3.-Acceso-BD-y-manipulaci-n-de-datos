import sqlalchemy as sqla

# Crear el motor y la conexión
db = sqla.create_engine('mysql+pymysql://mnaTC4029User:mnaTC4029Pass!@20.106.217.214:3306/classicmodels', pool_recycle=3600)
conn = db.connect()

# Consulta 1: Información de las líneas de productos
print("\nConsulta 1: Líneas de productos")
result = conn.execute("SELECT * FROM productlines;")
for row in result:
    print(row)

# Consulta 2: Empleados ordenados por nombre
print("\nConsulta 2: Empleados ordenados por nombre")
result = conn.execute("SELECT * FROM employees ORDER BY firstName;")
for row in result:
    print(row)

# Consulta 3: Países donde hay oficinas (sin duplicar)
print("\nConsulta 3: Países donde hay oficinas")
result = conn.execute("SELECT DISTINCT country FROM offices;")
for row in result:
    print(row)

# Consulta 4: Clientes de Nueva York (NYC)
print("\nConsulta 4: Clientes de Nueva York")
result = conn.execute("SELECT customerName, phone FROM customers WHERE city = 'NYC';")
for row in result:
    print(row)

# Consulta 5: Productos de Gearbox Collectibles con menos de 1000 unidades
print("\nConsulta 5: Productos de Gearbox Collectibles con menos de 1000 unidades")
result = conn.execute("SELECT productCode, productName FROM products WHERE productVendor = 'Gearbox Collectibles' AND quantityInStock < 1000;")
for row in result:
    print(row)

# Consulta 6: Tres productos más caros
print("\nConsulta 6: Tres productos más caros")
result = conn.execute("SELECT productName, buyPrice FROM products ORDER BY buyPrice DESC LIMIT 3;")
for row in result:
    print(row)

# Consulta 7: Cantidad de productos por línea de producto
print("\nConsulta 7: Cantidad de productos por línea de producto")
result = conn.execute("SELECT productLine, COUNT(*) AS total_products FROM products GROUP BY productLine;")
for row in result:
    print(row)

# Consulta 8: Cantidad de empleados por país
print("\nConsulta 8: Cantidad de empleados por país")
result = conn.execute("""
    SELECT offices.country, COUNT(employees.employeeNumber) AS total_employees 
    FROM employees 
    JOIN offices ON employees.officeCode = offices.officeCode 
    GROUP BY offices.country;
""")
for row in result:
    print(row)

# Consulta 9: Promedio de pagos de clientes de España
print("\nConsulta 9: Promedio de pagos de clientes de España")
result = conn.execute("""
    SELECT AVG(amount) AS average_payment 
    FROM payments 
    JOIN customers ON payments.customerNumber = customers.customerNumber 
    WHERE customers.country = 'Spain' AND amount > 0;
""")
for row in result:
    print(row)
