from django.db import models

# Create your models here.
class Detail(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Dateofbirth = models.DateField(default=0)
    occupation = models.CharField(max_length=50)
    Age = models.IntegerField(default=0)
    contact = models.IntegerField(default=0)
    Fathername= models.CharField(max_length=50)
    mothername= models.CharField(max_length=50)

    def __str__(self):
        return self.Firstname