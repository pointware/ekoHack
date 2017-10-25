# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Item, DashboardData

admin.site.register(Item)
admin.site.register(DashboardData)
# Register your models here.
