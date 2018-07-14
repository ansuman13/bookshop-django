# from django.db import models
# from django.contrib import auth

# # Create your models here.

# class user(auth.models.User,auth.models.PermissionsMixin):

# 	def __str__(self):
# 		return self.username
from django.contrib import auth
from django.db import models
from django.utils import timezone


class user(auth.models.User,auth.models.PermissionsMixin):
	def __str__(self):
		return "@{}".format(self.username)
