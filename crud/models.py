from django.db import models

# Create your models here.
class crud(models.Model):
    id = models.BigAutoField(primary_key=True)
    first = models.CharField(max_length=40) 
    last = models.CharField(max_length=40)
    
    class Meta:
      db_table = "crud"
      