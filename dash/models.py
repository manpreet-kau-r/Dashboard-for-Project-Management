from django.db import models

# Create your models here.
class Contact(models.Model):
	msg_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=70,default="")
	zoho = models.CharField(max_length=70,default="")
	phone = models.CharField(max_length=70,default="")
	linkedin = models.CharField(max_length=100,default="")
	team = models.CharField(max_length=100,default="")
	project = models.CharField(max_length=100,default="")
	
	def __str__(self):
		return self.name
