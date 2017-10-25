# -*- coding: utf-8 -*-

import os
from django.db import models

class AdMaterialFile(models.Model):
    material = models.FileField(upload_to='videoMaterial')

    @property
    def filename(self):
        return os.path.basename(self.file.name)

class Item(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    gd_no = models.IntegerField()
    amount = models.IntegerField()
    vip_url = models.TextField(null=True)

    def __unicode__(self):
        return self.name

    def add_item(self):
        self.save()



class DashboardData(models.Model):
    adName = models.CharField(max_length=200)
    channel = models.CharField(max_length=200)
    loginId = models.CharField(max_length=200)
    siteType = models.CharField(max_length=200)
    category1 = models.CharField(max_length=200)
    category2 = models.CharField(max_length=200)
    category3 = models.CharField(max_length=200)
    insDate = models.DateTimeField()
    age = models.IntegerField()
    sex = models.CharField(max_length=200)
    buyYN = models.CharField(max_length=200)

    
