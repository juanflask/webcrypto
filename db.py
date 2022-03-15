import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO contacto (nombre, email, mensaje) VALUES (?, ?, ?)",
            ('Lucia', 'lucia@lucia.com', 'Hola, quiero conocer la web.'))

cur.execute("INSERT INTO contacto (nombre, email, mensaje) VALUES (?, ?, ?)",
            ('Alberto', 'alberto@alberto.com', 'Hola, quiero conocer más la web.'))

cur.execute("INSERT INTO articulos (titulo, articulo) VALUES (?, ?)",
            ('Qué son las criptos?', 'Las criptos son...'))

cur.execute("INSERT INTO articulos (titulo, articulo) VALUES (?, ?)",
            ('Qué es el Bitcoin?', 'El bitcoin es una moneda digital.'))

connection.commit()
connection.close()
