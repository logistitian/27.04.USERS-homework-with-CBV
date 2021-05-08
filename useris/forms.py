from django import forms
from useris.models import Users


class UserAddForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['id', 'name', 'email']