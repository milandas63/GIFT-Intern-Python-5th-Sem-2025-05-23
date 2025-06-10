import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'gift_contact'
)

curs = conn.cursor()
curs.execute("SELECT c.con_id,c.con_name,c.con_mobile,r.rel_desc,l.loc_name FROM contact AS c LEFT JOIN relation AS r ON r.rel_id=c.rel_id LEFT JOIN location AS l ON l.loc_id=c.loc_id")

for row in curs:
	print()
	for index, col in enumerate(row):
		print(col, end=' ')
