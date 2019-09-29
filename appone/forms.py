import ckeditor
from ckeditor.widgets import CKEditorWidget
from django import forms
from ckeditor.fields import RichTextField


class TestForm(forms.Form):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Enter a title'}),
                            max_length=50)

    # text = forms.CharField(label="",
    #                        widget=forms.Textarea(attrs={'placeholder': 'Enter your text'}),
    #                        max_length=10000)

    text = forms.CharField(widget=CKEditorWidget())


class LeaveComment(forms.Form):
    # content = forms.CharField(label="",
    #                           widget=forms.Textarea(attrs={'placeholder': 'Leave a comment'}),
    #                           max_length=1000)

    # content = RichTextField()
    # toto = RichTextField()
    content = forms.CharField(widget=CKEditorWidget())
    # content = RichTextField(verbose_name="toto")