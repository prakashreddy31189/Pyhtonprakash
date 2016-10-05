import urllib2
import cookielib
from getpass import getpass
import sys
import os
from stat import *

from twilio.rest import TwilioRestClient



class Bank:

	balance= 0.0
	mobilenumber= 8553911356
	def __init__(self, Account_no):
		self.Account_no= Account_no
		
	def balance_amount(self):
		print " Balance in Your Account number {0} is: ".format(self.Account_no)+ str(self.balance)+ " rs"

	def deposit(self, dep_amount):
		self.dep_amount= dep_amount
		self.balance += dep_amount
		print " Your Account {0} is credited with amount of ".format(self.Account_no) + str(dep_amount)+ ". Your current balance is: "+ str(self.balance)+ " rs"

	def withdraw(self, deduct_amount):
		self.deduct_amount= deduct_amount
		self.balance -= deduct_amount
		print " Your Account {0} is debited with amount of ".format(self.Account_no) + str(deduct_amount)+ ". Your current balance is: "+ str(self.balance)+ " rs"
	
	def send_transcation_sms(self):
		username = "8050118448"
		passwd = "N4445G"
		#message = "+".join(message.split(' '))
		url ='http://site24.way2sms.com/Login1.action?'
		data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
		cj= cookielib.CookieJar()
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
		opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
		try:
			usock =opener.open(url, data)
		except IOError:
			print "error"
        

		jession_id =str(cj).split('~')[1].split(' ')[0]
		send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
		send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+str(self.mobilenumber)+'&message='+"Your curent balance is "+str(self.balance)+'&msgLen=136'
		opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
		try:
			sms_sent_page = opener.open(send_sms_url,send_sms_data)
		except IOError:
			print "error"        

		print "Your Account details has been sent to you Reg.. Mobile number" 



bank= Bank(123456)
bank.balance_amount()
bank.deposit(10000)
bank.withdraw(5000)
bank.send_transcation_sms()




