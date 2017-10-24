# -*- coding: utf-8 -*-
from django.db import models

class AdMaterialFile(models.Model):
    material = models.FileField(upload_to='videoMaterial')
    step = models.IntegerField()
    upload_id = models.CharField(max_length=200)
    upload_time = models.DateTimeField(auto_now=False, auto_now_add=False)