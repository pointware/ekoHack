# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AdMaterialForm
from .models import AdMaterialFile, Item, DashboardData

def index(request):
    return render(request, 'videoStudio/index.html', {})

def items(request):

    items = Item.objects.all()
    
    return render(request, 'videoStudio/items.html', {'items':items})

# dashboard mapping
def dashboard(request):
    
    # graph1 = DashboardData.objects.filter()

    return render(request, 'videoStudio/dashboard.html', {})

# Handle file upload
def videoEdit(request):
    if request.method == 'POST':
        form = AdMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            newmat = AdMaterialFile(material=request.FILES['material'])
            newmat.save()
            print '******* saved *******'

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('videoEdit'))
    else:
        form = AdMaterialForm()  # A empty, unbound form

    # Load documents for the list page
    materials = AdMaterialFile.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'videoStudio/videoEdit.html',
        { 'materials': materials, 'form': form }
    )