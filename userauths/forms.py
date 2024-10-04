from django import forms
from django.contrib.auth.forms import UserCreationForm

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from userauths.models import User

USER_TYPE = (
    ("Vendor", "Vendor"),
    ("Customer", "Customer"),
)

class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder':'Nombre completo'}), required=True)
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control rounded', 'placeholder':'Número de celular'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control rounded' , 'placeholder':'Correo electronico'}), required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control rounded' , 'placeholder':'Contraseña'}), required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'form-control rounded' , 'placeholder':'Confimar contraseña'}), required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
    user_type = forms.ChoiceField(choices=USER_TYPE, widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = User
        fields = ['full_name', 'mobile', 'email', 'password1', 'password2', 'captcha', 'user_type']
       
class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control rounded' , 'name': "email", 'placeholder':'Correo electronico'}), required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control rounded' , 'name': "password", 'placeholder':'Contraseña'}), required=False)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = User
        fields = ['email', 'password', 'captcha']
