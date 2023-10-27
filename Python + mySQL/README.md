# Python-MySQL

Connecting Python to mySQL:

```python
db = mysql.connector.connect(
    host='localhost',
    user='#',
    password='#',
    database='#'
)
```

- `mycursor = db.cursor()`: gives permission to modify the database
- `mycursor.execute()`: execute SQL 

```python
for x in mycursor:
    print(x)

 #loop throw database
