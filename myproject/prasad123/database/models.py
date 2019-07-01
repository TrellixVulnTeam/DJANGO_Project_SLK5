from django.db import models

# Create your models here.
'''class Customer2(models.Model):
     c_name = models.CharField(max_length = 264,unique = False)
     c_id = models.IntegerField(unique = True)
     contact_no = models.IntegerField()
     
     def __str__(self):
          return (self.c_name + " " + str(self.c_id) +" " + str(self.contact_no))'''
     
class Employee(models.Model):
     e_name = models.CharField(max_length = 264,unique = False)
     e_id = models.IntegerField(unique = True)
     dept = models.CharField(max_length =264,unique = False)
     
     def __str__(self):
          return (self.e_name + " " + str(self.e_id) + " " + self.dept)
      