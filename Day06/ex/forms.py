from django import forms

# from django.contrib.auth.forms import UserCreationForm


class SignIn(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


# class SignUp(forms.ModelForm):
#     class Meta:
#         model = UserCreationForm
#         fields = ["username", "password"]
