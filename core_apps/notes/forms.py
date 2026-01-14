from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth import get_user_model

from .models import Note

User = get_user_model()

class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))
    class Meta:
        model = Note
        fields = ["title", "content"]
        # labels = {
        #     "title": "Title",
        #     "content": "Content",
        #     "completed": "Completed",
        # }
        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "form-control"}),
        #     "content": forms.Textarea(attrs={"class": "form-control"}),
        #     "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        # }
