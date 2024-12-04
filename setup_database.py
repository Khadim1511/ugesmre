import psycopg2

conn = psycopg2.connect(
    dbname='recen_xl1y',
    user='recen_xl1y_user',
    password='9VE7TJGshNIkqYFzTEzFS95bLXsL1ZDj',
    host='dpg-ct84e4pu0jms73aun6p0-a',
    port='5432'
)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    nom_prenom TEXT NOT NULL,
    date_naissance DATE NOT NULL,
    annee_arrivee TEXT NOT NULL,
    email TEXT NOT NULL,
    etablissement TEXT NOT NULL,
    filiere TEXT NOT NULL,
    student_code TEXT UNIQUE NOT NULL,
    photo TEXT
)
''')

print("Table 'users' créée avec succès.")
conn.commit()
cursor.close()
conn.close()
