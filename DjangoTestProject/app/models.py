"""
Definition of models.
"""

from django.db import models

# Create your models here.
class ImportantButton(models.Model):
    press_count = models.IntegerField()
    expiry_time = models.DateField()