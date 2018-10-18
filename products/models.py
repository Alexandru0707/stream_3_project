# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from redactor.fields import RedactorField

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = RedactorField(verbose_name=u'Text')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __unicode__(self):
        return self.name
