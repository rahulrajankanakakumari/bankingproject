from django.db import models

# Create your models here.
class Customer_Data(models.Model):
    Cust_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Phone_no = models.CharField(max_length=10)
    #Fixed length can't be specified. Only max_length can be.
    Email = models.EmailField()
    #Username = models.CharField(max_length=30)
    #Password = models.CharField(max_length=30)
    class Meta:
        db_table = 'customer'
