from django import forms


class TestForm(forms.Form):
    title = forms.CharField(label="Enter a title", max_length=50)
    text = forms.CharField(label="Enter your text", max_length=255)