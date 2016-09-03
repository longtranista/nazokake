from django import forms

class PostForm(forms.Form):
    kakeru = forms.CharField(label='kakeru', max_length=256)
    toku = forms.CharField(label='toku', max_length=256)
    kokoro = forms.CharField(label='kokoro', max_length=256)

