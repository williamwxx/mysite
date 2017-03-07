from __future__ import unicode_literals
from django.db import models

# Create your models here.

class mpay(models.Model):
    id=models.IntegerField(primary_key=True)
    alipay = models.IntegerField()
    wxpay = models.IntegerField()
    ccb = models.IntegerField()
    succee = models.IntegerField()
    fail = models.IntegerField()
    ip_time = models.DateField()

