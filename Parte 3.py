import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# Cargar las credenciales desde el archivo JSON
cred = credentials.Certificate('veterinary.json')
firebase_admin.initialize_app(cred)

# Conectarse a la base de datos Firestore
db = firestore.client()

# Leer la colección PET_OWNER
pet_owner_ref = db.collection('PET_OWNER')
docs = pet_owner_ref.stream()

# Almacenar los datos en una lista de diccionarios
data = []
for doc in docs:
    doc_dict = doc.to_dict()
    doc_dict['id'] = doc.id  # Incluir el id en los datos
    data.append(doc_dict)

# Convertir los datos en un dataframe de Pandas
df_pet_owner = pd.DataFrame(data)

# Mostrar el contenido del dataframe
print(df_pet_owner)
