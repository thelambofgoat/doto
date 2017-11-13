import sqlite3
import sys
from libs.support.ctricks import ctricks

operations = ['add']

args = sys.argv[1:]

print('doto v.0.1.1')
print('author: Paul Smalling <thelambofgoat@gmail.com>')

if ('adds' not in operations):
    sys.exit('Недопустимая операция, на данный момент допустима только операция ' + ctricks.BOLD + 'add' + ctricks.END)
print(args)

sys.exit(0)

# Connecting
conn = sqlite3.connect('doto.db')

# Cursor object
c = conn.cursor()

# Inserting data
c.execute("INSERT INTO achievements VALUES (NULL, 'first insert')")

# Commiting
conn.commit()

# Closing connection
conn.close()

# Printing something
print('Successfully commited!')
