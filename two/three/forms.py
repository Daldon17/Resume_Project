from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 6,
            'placeholder': 'Paste job description here...'
        })
    )

    class Meta:
        model = Resume
        fields = ['file']