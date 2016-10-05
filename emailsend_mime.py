import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def email_send(fromaddr, pwd, toaddr):

	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "Python Test Mail"
	body = "Here is the list of Python Concepts"
	html= """\
		   <html>
			<head> Hi, </head>
				<p>Python Topics:</p>
				  <ol>
					 <li>Pyhton Basics</li>
					 <li>Python Data Types/Data Structures</li>
					 <li>Python looping concepts</li>
					 <li>Iterators/Generators</li>
					 <li>List Comprehension</li>
					 <li>Python Modules</li>
					 <li>Python Exception Handling</li>
					 <li>File Handling</li>
					 <li>Pyhton Classes</li>
					 <li>OOPs Concepts</li>                     
				  </ol>
			</body>
		   </html> """


	msg.attach(MIMEText(body, 'plain'))
	msg.attach(MIMEText(html, 'html'))

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


email_send('from adress', 'password', 'to-adress')
