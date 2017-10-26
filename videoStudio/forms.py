from django import forms

class AdMaterialForm(forms.Form):
     material = forms.FileField(
        label='Select a file'
    )

class videoEditStep1Form(forms.Form):
    text1 = forms.CharField(max_length=200, initial='EVC로 만든', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text2 = forms.CharField(max_length=200, initial='광고영상을 공개합니다', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text3 = forms.CharField(max_length=200, initial='여기에 text를 입력하면', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text4 = forms.CharField(max_length=200, initial='이렇게 된답니다', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text5 = forms.CharField(max_length=200, initial='이 영상을 만드는데', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text6 = forms.CharField(max_length=200, initial='걸린 시간 ?', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text7 = forms.CharField(max_length=200, initial='5분!', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text8 = forms.CharField(max_length=200, initial='이제부터', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text9 = forms.CharField(max_length=200, initial='제가 팔고 싶은', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text10 = forms.CharField(max_length=200, initial='목 견인기 광고가', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text11 = forms.CharField(max_length=200, initial='광고가', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text12 = forms.CharField(max_length=200, initial='시작 됩니다', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text13 = forms.CharField(max_length=200, initial='3', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text14 = forms.CharField(max_length=200, initial='2', widget=forms.TextInput(attrs={'class': 'form-control'}))
    text15 = forms.CharField(max_length=200, initial='1', widget=forms.TextInput(attrs={'class': 'form-control'}))

class videoEditStep2Form(forms.Form):
    text = forms.CharField(max_length=200, initial='회사원 류현준씨 거북목 되겠네요',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    video = forms.FileField(
        label='Select a video'
    )

class videoEditStep3Form(forms.Form):
    text = forms.CharField(max_length=200, initial='거북이(?)',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.FileField(
        label = 'Select a image'
    )

class videoEditStep4Form(forms.Form):
    text = forms.CharField(max_length=200, initial='슉슉슉슉슉슉슉',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    video = forms.FileField(
        label='Select a video'
    )

class videoEditStep5Form(forms.Form):
    
    text1 = forms.CharField(max_length=200, initial='Shipping팀 이재원님의 후기',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text2 = forms.CharField(max_length=200, initial='ESM팀 최병훈님의 후기',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text3 = forms.CharField(max_length=200, initial='Selling실 김두한님의 후기',
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

seolhyun = ['media/videoMaterial/logo.mp4', 'media/videoMaterial/logo2.mp4', 'media/videoMaterial/logo3.mp4']

class finalMovieSelectForm(forms.Form):

    choice = forms.ChoiceField(choices= seolhyun, widget=forms.RadioSelect())