import sqlite3

class Medical_Reports():
		
	

	def connection_status_stock(self):

		try:
			db = sqlite3.connect('/home/prakash/Downloads/pavan.db')
			cursor = db.cursor()
			print "database connected succesfully"
			
		except Exception as e:
			print "error"+ str(Exception)
		finally:
			db.close()
    

	def know_stock_details(self):
		try:
			db= sqlite3.connect('/home/prakash/Downloads/pavan.db')
			cursor= db.cursor()
			print "database connected succesfully"
			print "Reading Database Records.. "
			cursor.execute('''SELECT *FROM MyApp_compltestockdetails''')
			for row in cursor:
				print('{0} : {1}, {2},{3}, {4}, {5}, {6}, {7}, {8}, {9}'.format(row[0], row[1], row[2],row[3], row[4], row[5],row[6], row[7], row[8], row[9]))
		except Exception as e:
			print "error"+ str(Exception)
		finally:
			db.close()

	def transcation_details(self):
		itemname= raw_input("Enter item_name: ")
		quantity= raw_input("Enter sold quantity: ")
		


med_rep= Medical_Reports()
#med_rep.connection_status_stock()
med_rep.know_stock_details()