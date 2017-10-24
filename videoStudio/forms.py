from django import forms

class AdMaterialForm(forms.Form):
    adMaterialfile = forms.FileField(
        label='Select a file'
    )