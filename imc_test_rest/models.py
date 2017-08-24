# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Animal(models.Model):
    class Meta():
        db_table = 'animal'

    name = models.CharField(max_length=256, unique=True)

    def __unicode__(self):
        return "%s" % (self.name)


class Area(models.Model):
    class Meta():
        db_table = 'area'

    name = models.CharField(max_length=256)
    animals = models.ManyToManyField('Animal', blank=True, related_name='animal')

    def __unicode__(self):
        return "%s" % (self.name)
