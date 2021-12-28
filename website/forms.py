from django import forms 




class RegisterForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = password = forms.CharField(widget=forms.PasswordInput())
    