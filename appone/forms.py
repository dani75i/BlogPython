import ckeditor
from ckeditor.widgets import CKEditorWidget
from django import forms


FAVORITE_LANGUAGES_CHOICES = [
    ('Java', 'Java'),
    ('Python', 'Python'),
    ('JavaScript', 'JavaScript'),
    ('Go', 'Go'),
    ('Ruby', 'Ruby'),
]

CHOICES = (
    ('Languages', (
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('Go', 'Go'),
        ('Ruby', 'Ruby'),
    )),
    ('Devops', (
        ('Docker', 'Docker'),
        ('Kubernetes', 'Kubernetes'),
        ('Jenkins', 'Jenkins'),
    )),
    ('AI', (
        ('Machine Learning', 'Machine Learning'),
        ('Deep learning', 'Deep learning'),
    )),
)

class TestForm(forms.Form):
    title = forms.CharField(label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Enter a title'}),
                            max_length=150)

    tags = forms.ChoiceField(label="Select a tag",
        choices = CHOICES, required=True)

    text = forms.CharField(label="Insert a text",widget=CKEditorWidget())


class LeaveComment(forms.Form):

    content = forms.CharField(widget=CKEditorWidget())
