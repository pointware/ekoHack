# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import AdMaterialFile, Item, DashboardData, RedirectGo
from .forms import AdMaterialForm, videoEditStep1Form, videoEditStep2Form, videoEditStep3Form, videoEditStep4Form, videoEditStep5Form, finalMovieSelectForm
from VideoEdit import * 

import hashlib
import time

def index(request):
    return render(request, 'videoStudio/index.html', {})

def items(request):

    items = Item.objects.all()
    
    return render(request, 'videoStudio/items.html', {'items':items})

# dashboard mapping
def dashboard(request):
    
    # graph1 = DashboardData.objects.filter()

    return render(request, 'videoStudio/dashboard.html', {})

def go(request):
    
    h = request.GET['q']
    vipUrl = RedirectGo.objects.get(hashValue=h)

    return redirect(vipUrl) 

# Handle file upload
def videoEdit(request):
    if request.method == 'POST':

    # form = AdMaterialForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         newmat = AdMaterialFile(material=request.FILES['material'])
    #         newmat.save()

    #         # Redirect to the document list after POST
    #         return HttpResponseRedirect(reverse('videoEdit')) 

        template = VideoTemplate()

        video1 = AdMaterialFile(material='videoMaterial/step1_video.mp4')
        video2 = AdMaterialFile(material='videoMaterial/step2_video.mp4')
        video3 = AdMaterialFile(material='videoMaterial/step3_video.mp4')
        video4 = AdMaterialFile(material='videoMaterial/step4_video.mp4')
        video5 = AdMaterialFile(material='videoMaterial/step5_video.mp4')

        param = ['videoStudio' + video1.material.url, 'videoStudio' + video2.material.url, 'videoStudio' + video3.material.url, 'videoStudio' + video4.material.url, 'videoStudio' + video5.material.url]
        timestr = time.strftime('%H%M%S.mp4')
        template.make(param, 'videoStudio/media/result'+timestr)
        result = AdMaterialFile(material='result'+timestr)

        hash = makeUrl('http://item.gmarket.co.kr/Item?goodscode=642480089')

        URL = 'http://hkta31-u1.koreacentral.cloudapp.azure.com/?q=' + str(hash)

        return render(
        request,
        'videoStudio/videoEdit.html',
        {'result':result, 'URL':URL }
    )
    else:
        form_step1 = videoEditStep1Form()
        form_step2 = videoEditStep2Form()
        form_step3 = videoEditStep3Form()
        form_step4 = videoEditStep4Form()
        form_step5 = videoEditStep5Form()
    # Render list page with the documents and the form
    return render(
        request,
        'videoStudio/videoEdit.html',
        {'div': 1, 'form_step1': form_step1, 'form_step2': form_step2, 'form_step3': form_step3, 'form_step4': form_step4, 'form_step5': form_step5}
    )

def videoTemplate(request):
    return render(request, 'videoStudio/videoTemplate.html', {})

def videoEditStep1(request):

    if request.method == "POST":
        template = VideoTemplate()
        form_step1 = videoEditStep1Form(request.POST)

        param = []
        param.append(form_step1['text1'].value())
        param.append(form_step1['text2'].value())
        param.append(form_step1['text3'].value())
        param.append(form_step1['text4'].value())
        param.append(form_step1['text5'].value())
        param.append(form_step1['text6'].value())
        param.append(form_step1['text7'].value())
        param.append(form_step1['text8'].value())
        param.append(form_step1['text9'].value())
        param.append(form_step1['text10'].value())
        param.append(form_step1['text11'].value())
        param.append(form_step1['text12'].value())
        param.append(form_step1['text13'].value())
        param.append(form_step1['text14'].value())
        param.append(form_step1['text15'].value())

        template.step1(param, 'videoStudio/media/videoMaterial/step1_video.mp4')
        video = AdMaterialFile(material='videoMaterial/step1_video.mp4')
        
        form_step2 = videoEditStep2Form()
        form_step3 = videoEditStep3Form()
        form_step4 = videoEditStep4Form()
        form_step5 = videoEditStep5Form()

    else:
        form = videoEditStep1Form()

    return render(request, 'videoStudio/videoEdit.html', {'div':1, 'form_step1': form_step1, 'form_step2': form_step2, 'form_step3': form_step3, 'form_step4': form_step4, 'form_step5': form_step5, 'video1':video})

def videoEditStep2(request):

    if request.method == "POST":

        template = VideoTemplate()
        form_step2 = videoEditStep2Form(request.POST, request.FILES)

        form_step1 = videoEditStep1Form()
        form_step3 = videoEditStep3Form()
        form_step4 = videoEditStep4Form()
        form_step5 = videoEditStep5Form()

        if form_step2.is_valid():
            param_text = form_step2['text'].value()
            param_video_name = AdMaterialFile(material=request.FILES['video'])
            param_video_name.save()

            template.step2(form_step2['text'].value(), 'videoStudio' + param_video_name.material.url, 'videoStudio/media/videoMaterial/step2_video.mp4')
            video2 = AdMaterialFile(material='videoMaterial/step2_video.mp4')
            video1 = AdMaterialFile(material='videoMaterial/step1_video.mp4')

            return render(request, 'videoStudio/videoEdit.html', {'div':2, 'form_step1': form_step1, 'form_step2': form_step2, 'form_step3': form_step3, 'form_step4': form_step4, 'form_step5': form_step5, 'video1':video1, 'video2':video2})

    else:
        form = videoEditStep2Form()

    return render(request, 'videoStudio/videoEdit.html', {'form':form})

def videoEditStep3(request):

    if request.method == "POST":

        template = VideoTemplate()
        form_step3 = videoEditStep3Form(request.POST, request.FILES)

        form_step1 = videoEditStep1Form()
        form_step2 = videoEditStep2Form()
        form_step4 = videoEditStep4Form()
        form_step5 = videoEditStep5Form()

        if form_step3.is_valid():
            param_text = form_step3['text'].value()
            param_image_name = AdMaterialFile(material=request.FILES['image'])
            param_image_name.save()

            print param_text
            print param_image_name

            template.step3(param_text, 'videoStudio' + param_image_name.material.url, 'videoStudio/media/videoMaterial/step3_video.mp4')
            video3 = AdMaterialFile(material='videoMaterial/step3_video.mp4')
            video2 = AdMaterialFile(material='videoMaterial/step2_video.mp4')
            video1 = AdMaterialFile(material='videoMaterial/step1_video.mp4')

            return render(request, 'videoStudio/videoEdit.html', {'div':3, 'form_step1': form_step1, 'form_step2': form_step2, 'form_step3': form_step3, 'form_step4': form_step4, 'form_step5': form_step5, 'video1':video1, 'video2':video2, 'video3':video3})

    else:
        form = videoEditStep3Form()

    return render(request, 'videoStudio/videoEdit.html', {'form':form})

def videoEditStep4(request):

    if request.method == "POST":

        template = VideoTemplate()
        form_step4 = videoEditStep4Form(request.POST, request.FILES)

        form_step1 = videoEditStep1Form()
        form_step2 = videoEditStep2Form()
        form_step3 = videoEditStep3Form()
        form_step5 = videoEditStep5Form()

        if form_step4.is_valid():
            param_text = form_step4['text'].value()
            param_video_name = AdMaterialFile(material=request.FILES['video'])
            param_video_name.save()

            print param_video_name.material.url
            print param_text

            template.step4(param_text, 'videoStudio' + param_video_name.material.url, 'videoStudio/media/videoMaterial/step4_video.mp4')
            video4 = AdMaterialFile(material='videoMaterial/step4_video.mp4')
            video3 = AdMaterialFile(material='videoMaterial/step3_video.mp4')
            video2 = AdMaterialFile(material='videoMaterial/step2_video.mp4')
            video1 = AdMaterialFile(material='videoMaterial/step1_video.mp4')

            return render(request, 'videoStudio/videoEdit.html', {'div':4,'form_step1': form_step1, 'form_step2': form_step2, 'form_step3': form_step3, 'form_step4': form_step4, 'form_step5': form_step5, 'video1':video1, 'video2':video2, 'video3':video3, 'video4':video4})

    else:
        form = videoEditStep4Form()

    return render(request, 'videoStudio/videoEdit.html', {})

def videoEditStep5(request):

    if request.method == "POST":
        template = VideoTemplate()
        form_step5 = videoEditStep5Form(request.POST, request.FILES)

        form_step1 = videoEditStep1Form()
        form_step2 = videoEditStep2Form()
        form_step3 = videoEditStep3Form()
        form_step4 = videoEditStep4Form()

        if form_step5.is_valid():
            param_text1 = form_step5['text1'].value()
            param_text2 = form_step5['text2'].value()
            param_text3 = form_step5['text3'].value()

            param_image_name1 = AdMaterialFile(material=request.FILES['image1'])
            param_image_name2 = AdMaterialFile(material=request.FILES['image2'])
            param_image_name3 = AdMaterialFile(material=request.FILES['image3'])

            param_image_name1.save()
            param_image_name2.save()
            param_image_name3.save()

            param_image_name = ['videoStudio' + param_image_name1.material.url, 'videoStudio' + param_image_name2.material.url, 'videoStudio' + param_image_name3.material.url]
            param_text = [param_text1, param_text2, param_text3]

            print param_image_name
            print param_text

            template.step5(param_text, param_image_name, 'videoStudio/media/videoMaterial/step5_video.mp4')
            video5 = AdMaterialFile(material='videoMaterial/step5_video.mp4')
            video4 = AdMaterialFile(material='videoMaterial/step4_video.mp4')
            video3 = AdMaterialFile(material='videoMaterial/step3_video.mp4')
            video2 = AdMaterialFile(material='videoMaterial/step2_video.mp4')
            video1 = AdMaterialFile(material='videoMaterial/step1_video.mp4')

            return render(request, 'videoStudio/videoEdit.html', {'div':5,'form_step1': form_step1, 'form_step2': form_step2, 'form_step3': form_step3, 'form_step4': form_step4, 'form_step5': form_step5, 'video1':video1, 'video2':video2, 'video3':video3, 'video4':video4, 'video5':video5})

    else:
        form = videoEditStep5Form()

    return render(request, 'videoStudio/videoEdit.html', {})

def videoEditStep6(request):
    return render(request, 'videoStudio/videoEdit.html', {})

def makeUrl(gmarketVipUrl):
    masterId = 'ekoHack'
    h = hashlib.new('ripemd160')
    strtime = time.strftime('%Y%m%d%H%M%S')
    h.update(strtime + masterId)
    print h.hexdigest()

    r = RedirectGo.objects.create(vipUrl=gmarketVipUrl, hashValue=h.hexdigest())

    return h.hexdigest()
