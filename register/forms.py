from django import forms
from .models import User

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('mail', 'pwd', 'pwd_repeat',)