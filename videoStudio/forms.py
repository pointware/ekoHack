from django import forms

class AdMaterialForm(forms.Form):
     material = forms.FileField(
        label='Select a file'
    )

class videoEditStep1Form(forms.Form):
    text1 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}, initial='123'))
    text2 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text3 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text4 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text5 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text6 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text7 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text8 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text9 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text10 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text11 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text12 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text13 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text14 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text15 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

class videoEditStep2Form(forms.Form):
    text = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    video = forms.FileField(
        label='Select a video'
    )

class videoEditStep3Form(forms.Form):
    text = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.FileField(
        label = 'Select a image'
    )

class videoEditStep4Form(forms.Form):
    text = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    video = forms.FileField(
        label='Select a video'
    )

class videoEditStep5Form(forms.Form):
    
    text1 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text2 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text3 = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))

    image1 = forms.FileField(
        label = 'Select a image'
    )
    image2 = forms.FileField(
        label = 'Select a image'
    )
    image3 = forms.FileField(
        label = 'Select a image'
    )