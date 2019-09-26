from django import forms


class TestForm(forms.Form):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Enter a title'}),
                            max_length=50)

    text = forms.CharField(label="",
                           widget=forms.Textarea(attrs={'placeholder': 'Enter your text'}),
                           max_length=10000)


class LeaveComment(forms.Form):
    content = forms.CharField(label="",
                              widget=forms.Textarea(attrs={'placeholder': 'Leave a comment'}),
                              max_length=1000)