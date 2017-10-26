from django import forms

class AdMaterialForm(forms.Form):
     material = forms.FileField(
        label='Select a file'
    )

class videoEditStep1Form(forms.Form):
    text1 = forms.CharField(max_length=200)
    text2 = forms.CharField(max_length=200)
    text3 = forms.CharField(max_length=200)
    text4 = forms.CharField(max_length=200)
    text5 = forms.CharField(max_length=200)
    text6 = forms.CharField(max_length=200)
    text7 = forms.CharField(max_length=200)
    text8 = forms.CharField(max_length=200)
    text9 = forms.CharField(max_length=200)
    text10 = forms.CharField(max_length=200)
    text11 = forms.CharField(max_length=200)
    text12 = forms.CharField(max_length=200)
    text13 = forms.CharField(max_length=200)
    text14 = forms.CharField(max_length=200)
    text15 = forms.CharField(max_length=200)

class videoEditStep2Form(forms.Form):
    text = forms.CharField(max_length=200)
    video = forms.FileField(
        label='Select a video'
    )

class videoEditStep3Form(forms.Form):
    text = forms.CharField(max_length=200)
    image = forms.FileField(
        label = 'Select a image'
    )

class videoEditStep4Form(forms.Form):
    text = forms.CharField(max_length=200)
    video = forms.FileField(
        label='Select a video'
    )

class videoEditStep5Form(forms.Form):
    
    text1 = forms.CharField(max_length=200)
    text2 = forms.CharField(max_length=200)
    text3 = forms.CharField(max_length=200)

    image1 = forms.FileField(
        label = 'Select a image'
    )
    image2 = forms.FileField(
        label = 'Select a image'
    )
    image3 = forms.FileField(
        label = 'Select a image'
    )

seolhyun = ['media/videoMaterial/logo.mp4', 'media/videoMaterial/logo2.mp4', 'media/videoMaterial/logo3.mp4']

class finalMovieSelectForm(forms.Form):

    choice = forms.ChoiceField(choices= seolhyun, widget=forms.RadioSelect())