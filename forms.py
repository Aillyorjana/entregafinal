from django import forms
from .models import Page
from ckeditor.widgets import CKEditorWidget

class PageForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = ['title','subtitle','slug','content','cover','published_at']
      
#Registrar e editar perfil

from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2","first_name","last_name"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','birth_date','website']
