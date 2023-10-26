import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


cursor.execute('SELECT username, COUNT(*) as similar_count FROM Users GROUP BY username')
results = cursor.fetchall()
cursor.execute('SELECT username FROM Users GROUP BY username Order by count(*) desc LIMIT 1')
max_similar = cursor.fetchall()



for row in results:
  print(row)

print(max_similar)

connection.close()