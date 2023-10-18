import sqlite3

# Conecta a la base de datos
conn = sqlite3.connect('contactos.db')
cursor = conn.cursor()

# Datos del nuevo contacto
nombre = 'Nombre del Contacto'
email = 'correo@example.com'
telefono = '1234567890'

# Inserta el nuevo contacto en la tabla
cursor.execute("INSERT INTO contactos (nombre, email, telefono) VALUES (?, ?, ?)", (nombre, email, telefono))
import sqlite3

# Consulta todos los contactos
cursor.execute("SELECT * FROM contactos")
contactos = cursor.fetchall()
# Imprime los contactos
for contacto in contactos:
    print(contacto)


# Guarda los cambios y cierra la conexión
conn.commit()
conn.close()
