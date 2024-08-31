from django import forms

class VerificationCodeForm(forms.Form):
    email = forms.EmailField()
    code = forms.CharField(max_length=6)

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()

class PasswordResetConfirmForm(forms.Form):
    email = forms.EmailField()
    code = forms.CharField(max_length=6)
    new_password = forms.CharField(widget=forms.PasswordInput)
