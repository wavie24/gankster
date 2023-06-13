from django.db import models

class Simulasi(models.Model):
  panjang = models.CharField(max_length=15)
  lebar = models.CharField(max_length=15)