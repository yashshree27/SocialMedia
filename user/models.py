

from django.db import models

# Create your models here.

class users_new(models.Model):
    userId= models.IntegerField(primary_key=True)
    name= models.CharField(max_length=30)
    mobilenumber= models.CharField(max_length=30)
    password= models.CharField(max_length=30)
    emailid= models.CharField(max_length=30)
    acc_created= models.CharField(max_length=30,blank=True,null=True)
    friendslist= models.CharField(max_length=30,blank=True,null=True)
    private= models.BooleanField()
    #class Meta:
      #  db_table= 'mydb'
