from django import forms
from django import forms


class ProfileForm(forms.Form):
    user_image = forms.ImageField()
