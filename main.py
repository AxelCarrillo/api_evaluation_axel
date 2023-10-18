import fastapi
import sqlite3
from pydantic import BaseModel

# Conecta a la base de datos
conn = sqlite3.connect("contactos.db")

app = fastapi.FastAPI()

class Contacto(BaseModel):
    email: str
    nombres: str  # Cambiado de 'nombres' a 'nombre'
    telefono: str  # Cambiado de 'telefono' a 'telefono'

# Rutas para las operaciones CRUD

@app.post("/contactos")
async def crear_contacto(contacto: Contacto):
    """Crea un nuevo contacto."""
    c = conn.cursor()
    c.execute('INSERT INTO contactos (email, nombre, telefono) VALUES (?, ?, ?)',
              (contacto.email, contacto.nombres, contacto.telefono))  # Cambiado de 'nombres' a 'nombre'
    conn.commit()
    return contacto

@app.get("/contactos")
async def obtener_contactos():
    """Obtiene todos los contactos."""
    c = conn.cursor()
    c.execute('SELECT * FROM contactos')
    response = []
    for row in c.fetchall():
        contacto = Contacto(email=row[0], nombres=row[1], telefono=row[2])
        response.append(contacto)
    return response

@app.get("/contactos/{email}")
async def obtener_contacto(email: str):
    """Obtiene un contacto por su email."""
    c = conn.cursor()
    c.execute('SELECT * FROM contactos WHERE email = ?', (email,))
    row = c.fetchone()
    if row:
        contacto = Contacto(email=row[0], nombres=row[1], telefono=row[2])
        return contacto
    return {"mensaje": "Contacto no encontrado"}

@app.put("/contactos/{email}")
async def actualizar_contacto(email: str, contacto: Contacto):
    """Actualiza un contacto."""
    c = conn.cursor()
    c.execute('UPDATE contactos SET nombre = ?, telefono = ? WHERE email = ?',
              (contacto.nombres, contacto.telefono, email))
    conn.commit()
    return contacto

@app.delete("/contactos/{email}")
async def eliminar_contacto(email: str):
    """Elimina un contacto."""
    c = conn.cursor()
    c.execute('DELETE FROM contactos WHERE email = ?', (email,))
    conn.commit()
    return {"mensaje": "Contacto eliminado"}
