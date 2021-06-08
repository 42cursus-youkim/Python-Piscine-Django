from django import forms


class ScarfForm(forms.Form):
    content = forms.CharField(required=True)
