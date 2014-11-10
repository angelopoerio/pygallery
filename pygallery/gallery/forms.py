from django import forms

class UploadPictureForm(forms.Form):
	image = forms.ImageField(required=True)
	notes = forms.CharField(required=False)
