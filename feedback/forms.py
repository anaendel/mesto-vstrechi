from django import forms

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'message')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'ИМЯ'}),
            'email': forms.EmailInput(attrs={'placeholder': 'EMAIL'}),
            'subject': forms.TextInput(attrs={'placeholder': 'ЗАПРОС'}),
            'message': forms.Textarea(attrs={'placeholder': 'СООБЩЕНИЕ'}),
        }