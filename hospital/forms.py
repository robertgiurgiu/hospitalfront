from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  



class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Username', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 

        self.fields['first_name'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'first_name', 
            'id':'first_name', 
            'type':'text', 
            'placeholder':'First Name', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 
        self.fields['last_name'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'last_name', 
            'id':'last_name', 
            'type':'text', 
            'placeholder':'Last Name', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'Your mail', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'Password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'Repeat password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
 
 
    username = forms.CharField(max_length=20, label=False) 
    email = forms.EmailField(max_length=100) 
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    """def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  

    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  """
    
    class Meta:
        model= User 
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2', ]



class DoctorSignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['username'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'username', 
            'id':'username', 
            'type':'text', 
            'placeholder':'Username', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 
        self.fields['first_name'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'first_name', 
            'id':'first_name', 
            'type':'text', 
            'placeholder':'First Name', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 
        self.fields['last_name'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'last_name', 
            'id':'last_name', 
            'type':'text', 
            'placeholder':'Last Name', 
            'maxlength': '16', 
            'minlength': '3', 
            }) 
        self.fields['email'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'email', 
            'id':'email', 
            'type':'email', 
            'placeholder':'Your mail', 
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password1', 
            'id':'password1', 
            'type':'password', 
            'placeholder':'Password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'class': 'form-input', 
            'required':'', 
            'name':'password2', 
            'id':'password2', 
            'type':'password', 
            'placeholder':'Repeat password', 
            'maxlength':'22',  
            'minlength':'8' 
            }) 
 
    username = forms.CharField(max_length=20, label=False) 
    email = forms.EmailField(max_length=100) 
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    
    class Meta:
        model= User 
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2', ]
