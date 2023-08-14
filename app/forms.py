from django import forms

class LoginForm(forms.Form):
    """Form for logging in """
    login = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
