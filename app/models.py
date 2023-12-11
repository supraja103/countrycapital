from django.db import models

# Create your models here.
class Country(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)

    def __str__(self):
        return self.cname
class Capital(models.Model):
    cid=models.OneToOneField(Country,on_delete=models.CASCADE)
    capid=models.IntegerField()
    capname=models.CharField(max_length=100)

    def __str__(self):
        return self.capname

