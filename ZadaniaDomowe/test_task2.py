import sqlite3

connection = sqlite3.connect('OurDataBaseTest.db')
cursor = connection.cursor()

#cursor.execute("INSERT INTO OurDataBaseTest (Address, City, FirstName, LastName, PersonID, Age) VALUES('Szkolna', 'Plewiska', 'Ewelina', 'Grzybowska', 3, 38)")
#connection.commit()
cursor.execute("SELECT * FROM OurDataBaseTest")
select = cursor.fetchall()
print(select)