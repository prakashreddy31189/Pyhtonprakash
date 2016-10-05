d= {'25':'Twenty Five','26':'Twenty Six','27':'Twenty Seven','28':'Twenty Eight','29':'Twenty Nine','30':'Thirty','31':'Thirty One','32':'Thirty Two','33':'Thirty Three','34':'Thirty Four','35':'Thirty Five','36':'Thirty Six','37':'Thirty Seven','38':'Thirty Eight','39':'Thirty Nine','40':'Forty','41':'Forty One','42':'Forty Two','43':'Forty Three','44':'Forty Four','45':'Forty Five','46':'Forty Six','47':'Forty Seven','48':'Forty Eight','49':'Forty Nine','50':'Fifty','51':'Fifty One','52':'Fifty Two','53':'Fifty Three','54':'Fifty Four','55':'Fifty Five','56':'Fifty Six','57':'Fifty Seven','58':'Fifty Eight','59':'Fifty Nine','11':'Eleven', '12': 'Twelve', '13': 'Thiteen', '14': 'Fourteen', '15': ' Fifteen', '16': 'Sixteen', '17':'Seventeeen', '18': 'Eighteen', '19': 'Ninteen', '20': 'Twenty', '21':'Twenty One', '22': 'Twenty Two', '23': 'Twenty Three', '24': 'Twenty Four', '01':'One', '02':'Two', '03':'Three', '04':'Four','05':'Five', '06':'Six', '07': 'Seven', '08':'Eight', '09':'Nine', '00': 'Zero',':': ':'}

inp= raw_input("Please Enter Time: ")
print inp[0:2]

if inp[0:2]>= 25 or inp[3:5]>= 60:
	print "please check time format"
		
else:	
	string_format_1= "Your Time in String Format is: %s Hour %s %s Mins" %(d[inp[0:2]], d[inp[2]], d[inp[3:5]])
	print string_format_1
	


