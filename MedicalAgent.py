import xlrd
import xlwt

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

class Medical_Report:

	def know_stock(self):
		book = xlrd.open_workbook("/home/prakash/Desktop/produceSales.xlsx") 
		global sheets
		sheets= book.sheets()	
		col= sheets[0].ncols			
		for row in range(1, sheets[0].nrows):			
			print sheets[0].cell_value(row, 0) + " "+ str(sheets[0].cell_value(row, 1)) +" "+ str(sheets[0].cell_value(row, 2))

	def update_stock(self):
		style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00')
		wb = xlwt.Workbook()
		ws = wb.add_sheet('A Test Sheet')
		total = 0
		a= 1
		ws.write(0,0, sheets[0].cell_value(0, 0), style0)
		ws.write(0,1, sheets[0].cell_value(0, 1), style0)
		ws.write(0,2, sheets[0].cell_value(0, 2), style0)
		ws.write(0,3, 'Total', style0)

		for row in range(1, sheets[0].nrows):
			total = sheets[0].cell_value(row, 2) * sheets[0].cell_value(row, 1)
			ws.write(a, 0, sheets[0].cell_value(row, 0), style0)
			ws.write(a, 1, sheets[0].cell_value(row, 1), style0)
			ws.write(a, 2, sheets[0].cell_value(row, 2), style0)
			ws.write(a, 3, total, style0)
			a += 1
			print total

		wb.save('example1.xls')

	def email_send_report(self, fromaddr, pwd, toaddr):

		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Mail From Agent "
		body = "Here is the list of Stock Details, "
		html= """\
		   <html>
			<head> Hi, </head>
				<p>Medical Stock Details:</p>
				  <ol>
					 <li>Please check the attached stock details</li>					 				                  
				  </ol>
			</body>
		   </html> """


		msg.attach(MIMEText(body, 'plain'))
		msg.attach(MIMEText(html, 'html'))

		filename = "example1.xls"
		attachment = open("/home/prakash/Desktop/produceSales.xlsx", "rb")
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		msg.attach(part)

		try:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.ehlo()
			server.starttls()
			server.login(fromaddr, pwd)
			text = msg.as_string()
			server.sendmail(fromaddr, toaddr, text)
			server.quit()

		except Exception:
			print "Error: unable to send email"




obj= Medical_Report()

obj.know_stock()
obj.update_stock()
obj.email_send_report('remodemo008@gmail.com', 'dbENGINEER@001', 'remodemo008@gmail.com')

