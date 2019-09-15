from django import forms


class TestForm(forms.Form):
    title = forms.CharField(label="Enter a title", max_length=50)
    text = forms.CharField(label="Enter your text", max_length=255)


class LeaveComment(forms.Form):
    content = forms.CharField(label="Leave a comment", max_length=255)