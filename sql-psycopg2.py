import psycopg2

# connect to chinook database
connection = psycopg2.connect(database="chinook")

# Build a cursor object of the database,
cursor = connection.cursor()

# Create a query
# cursor.execute('SELECT * FROM "Artist"')
# cursor.execute('SELECT "Name" FROM "Artist"')
# cursor.execute('SELECT * FROM "Artist" WHERE "Name"= %s', ["Queen"])
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId"= %s', [51])
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId"= %s', [51])
cursor.execute('SELECT * FROM "Track" WHERE "Composer"= %s', ["Queen"])

# Fetch multiple results
results = cursor.fetchall()

# close the connection
connection.close()

# Print results
for result in results:
    print(result)

