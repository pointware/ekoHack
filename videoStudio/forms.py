from django import forms

class AdMaterialForm(forms.Form):
     material = forms.FileField(
        label='Select a file'
    )