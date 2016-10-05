import json

"""
with open('/home/prakash/Desktop/Json-Read-write/generated.json') as json_data:
    d = json.load(json_data)
    print d[1]['friends'][1]['id']"""



def read_json(path=None):

	try:
		with open(path) as json_data:
			d= json.load(json_data)
			#print dir(d)
			#print type(d)  'd' type is list
			d[0]['favoriteFruit']='Apple'
			print d[0]['favoriteFruit']
			print d[0]

	except Exception as error_:
		print "File Error: "+ str(error_)

if __name__=='__main__':

	file_path= raw_input("Enter Json File Path :")
	read_json(file_path)







