from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Homework

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'subject', 'description', 'due', 'is_finished']
        widgets = {
            'description': CKEditorWidget(attrs={'class': 'ckeditor', 'required': True,}),
            'due': forms.DateInput(attrs={'type': 'date'})
        }
        
        
