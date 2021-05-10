from django import forms
from app.models import Classes

class ClassesForm(forms.ModelForm):
    
    class Meta:
        model = Classes
        fields = "__all__"