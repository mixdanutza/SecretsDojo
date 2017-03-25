from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import requests 
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'[a-zA-Z]{2,}')
#Our new manager!
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
	def reg(self,first_name,last_name, email1, password, password2):
		error_list=[]
		if not NAME_REGEX.match(first_name):
			error_list.append('First name contains digital  character(s)\n')
		if not NAME_REGEX.match(last_name):
			error_list.append('First name contains digital  character(s)\n')
		if not EMAIL_REGEX.match(email1):
			error_list.append('Email is not a valid email!\n')			
		if not password==password2:
			error_list.append('Password does not match the confirm password.\n')			
		if  self.filter(email=email1):
			error_list.append('Email already exists')		
		if not error_list:
			password = password.encode()
			hashed = bcrypt.hashpw(password, bcrypt.gensalt())			
			self.create(first_name=first_name, last_name=last_name, email=email1, password=hashed)	
			this_user=self.get(email=email1)
			return True, this_user
		else:
			return False, error_list
	def login(self, Info):
		if User.objects.filter(email=Info['email']) :			
			encrypted_password=self.filter(email=Info['email'])[0].password
			encrypted_password=encrypted_password.encode("utf-8")
			password=Info['log_password']
			password=password.encode("utf-8")
			if bcrypt.hashpw(password, encrypted_password)==encrypted_password:	
				this_user=self.get(email=Info['email'])	
				return True,this_user		
		else:
			return False,'Email not found!'
class User(models.Model):
	first_name=models.CharField(max_length=255)
	last_name=models.CharField(max_length=255)
	email=models.CharField(max_length=255)
	password=models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()