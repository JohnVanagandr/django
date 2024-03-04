from django.db import models

# Create your models here.

class Contac(models.Model):

  name    = models.CharField(max_length=250, null=False)
  phone   = models.CharField(max_length=40, null=False)
  email   = models.CharField(max_length=40, null=False)
  messaje = models.TextField(null=False)

  def __str__(self):
      return self.name
