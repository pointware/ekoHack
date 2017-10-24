# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AdMaterialForm
from .models import AdMaterialFile

def index(request):
    return render(request, 'videoStudio/index.html', {})

def items(request):
    return render(request, 'videoStudio/items.html', {})

#def videoEdit(request):
#    return render(request, 'videoStudio/videoEdit.html', {})

# Handle file upload
def videoEdit(request):
    if request.method == 'POST':
        form = AdMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            newmat = AdMaterialFile(adMaterialfile=request.FILES['adMaterialfile'])
            newmat.save()

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
