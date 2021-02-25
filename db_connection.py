from dbmodule import connect

#Create Connection Object
connection = connect('dbname','user','pwd')

#Create Cursor Object
cursor = connection.cursor()

#Run Queries
cursor.execute('select * from mytable')
results = cursor.fetchall()

#Free resources
cursor.close()
connection.close()