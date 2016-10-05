import sqlite3

def stock():
	try:
		db = sqlite3.connect('/home/prakash/Downloads/pavan.db')
		cursor = db.cursor()
		cursor.execute('''SELECT *FROM MyApp_compltestockdetails''')
		for row in cursor:
			print('{0} : {1}, {2},{3}, {4}, {5}, {6}, {7}, {8}, {9}'.format(row[0], row[1], row[2],row[3], row[4], row[5],row[6], row[7], row[8], row[9]))
	except Exception as e:
		print "error:" + str(Exception)
	finally:
		db.close()


#stock()

def stock_update():
	try:
		db = sqlite3.connect('/home/prakash/Downloads/pavan.db')
		cursor = db.cursor()
		cursor.execute('''UPDATE MyApp_compltestockdetails set batch_num = 205 where company= 'Dettol' ''')
		db.commit()
		print "Total number of rows updated :", db.total_changes		
	except Exception as e:
		print "error:" + str(Exception)
	finally:
		db.close()


stock_update()
stock()
