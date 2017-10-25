# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import AdMaterialFile, Item, DashboardData
from .forms import AdMaterialForm, videoEditStep1Form, videoEditStep2Form, videoEditStep3Form, videoEditStep4Form, videoEditStep5Form

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

    # form = AdMaterialForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         newmat = AdMaterialFile(material=request.FILES['material'])
    #         newmat.save()

    #         # Redirect to the document list after POST
    #         return HttpResponseRedirect(reverse('videoEdit')) 

        video1 = AdMaterialFile.objects.all().filename

    else:
        form = AdMaterialForm()  # A empty, unbound form
        form_step1 = videoEditStep1Form()
        form_step2 = videoEditStep2Form()
        form_step3 = videoEditStep3Form()
        form_step4 = videoEditStep4Form()
        form_step5 = videoEditStep5Form()

    # Load documents for the list page
    materials = AdMaterialFile.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'videoStudio/videoEdit.html',
        { 'materials': materials, 'form': form, 'form_step1': form_step1, 'form_step2': form_step2, 'form_step3': form_step3, 'form_step4': form_step4, 'form_step5': form_step5 }
    )

def videoEditStep1(request):

    if request.method == "POST":
        form = videoEditStep1Form(request.POST)
        video = AdMaterialFile()
    else:
        form = videoEditStep1Form()

    return render(request, 'videoStudio/videoEditStep1.html', {'form':form, 'video1':video})

def videoEditStep2(request):

    if request.method == "POST":
        form = videoEditStep2Form(request.POST, request.FILES)

    else:
        form = videoEditStep2Form()

    return render(request, 'videoStudio/videoEditStep2.html', {})

def videoEditStep3(request):

    if request.method == "POST":
        form = videoEditStep3Form(request.POST, request.FILES)

    else:
        form = videoEditStep3Form()

    return render(request, 'videoStudio/videoEditStep3.html', {})

def videoEditStep4(request):

    if request.method == "POST":
        form = videoEditStep4Form(request.POST, request.FILES)

    else:
        form = videoEditStep4Form()

    return render(request, 'videoStudio/videoEditStep4.html', {})

def videoEditStep5(request):

    if request.method == "POST":
        form = videoEditStep5Form(request.POST, request.FILES)

    else:
        form = videoEditStep5Form()

    return render(request, 'videoStudio/videoEditStep5.html', {})