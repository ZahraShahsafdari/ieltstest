from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']


class SearchForm(forms.Form):
    query = forms.CharField(label='Search for a university', min_length=0.0, max_length=9.0, required=False)
    ielts_score = forms.FloatField(label='IELTS Score', required=False)