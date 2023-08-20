from django import forms
from django.contrib.auth.models import Group
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    # group = forms.ModelChoiceField(queryset=Group.objects.all())
