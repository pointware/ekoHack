# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .forms import AdMaterialForm
from .models import AdMaterialFile

def index(request):
    return render(request, 'videoStudio/index.html', {})

# Handle file upload
def UploadMaterial(request):
    if request.method == 'POST':
        form = AdMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            newpic = AdMaterialFile(picfile=request.FILES['picfile'])
            newpic.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AdMaterialForm()  # A empty, unbound form

    # Load documents for the list page
    materials = AdMaterialFile.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'videoStudio/index.html',
        { 'materials': materials, 'form': form }
    )
