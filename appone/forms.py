from django import forms


class TestForm(forms.Form):
    title = forms.CharField(label="Enter a title", max_length=50)
    text = forms.CharField(label="Enter your text",
                           widget=forms.Textarea,
                           max_length=10000)


class LeaveComment(forms.Form):
    content = forms.CharField(label="Leave a comment",
                              widget=forms.Textarea,
                              max_length=1000)