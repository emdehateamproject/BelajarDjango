from django import forms

from django.contrib.auth.models import User
from .models import Register

class FormLogin(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control'}),
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'form-control'}),
    )

class FormRegister(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        widgets = {
            'password':forms.PasswordInput(),
            'email':forms.EmailInput(),
        }
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            
        ]
        help_texts = {
            'username': None,
        }
        
    
    def __init__(self, *args, **kwargs):
        super(FormRegister, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-2 py-3 ml-5 mr-5'


'''
    first_name = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control mb-2 py-2 px-4 ml-5 mr-5'}),
    )
    last_name = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control mb-2 py-2 px-4 ml-5 mr-5'}),
    )
    email = forms.CharField(
        widget = forms.EmailInput(attrs={'class':'form-control mb-2 py-2 px-4 ml-5 mr-5'}),
    )
    username = forms.CharField(
        widget = forms.TextInput(attrs={'class':'form-control mb-2 py-2 px-4 ml-5 mr-5','type':'text'}),
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'form-control mb-2 py-2 px-4 ml-5 mr-5'}),
    )
'''