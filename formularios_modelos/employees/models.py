from django.db import models

# Create your models here.
class Employee(models.Model):
  first_name = models.CharField(max_length=50, blank=False, null=False)
  last_name  = models.CharField(max_length=50, blank=False, null=False)
  email      = models.EmailField(max_length=50, blank=False, null=False)
  
  imagen     = models.ImageField(null=True, blank=True)

  def __str__(self):
      return self.first_name
  