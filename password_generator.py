import random

def password():
	s= '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()'
	passlength= 10
	pwd=''.join(random.sample(s, passlength))	
	if pwd.isalnum():
		print pwd
	else:
		password()


if __name__== "__main__":
	password()





