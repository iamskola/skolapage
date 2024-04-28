from django import forms
from .models import Review, Contact_Us


class AddReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['name', 'phone_number', 'email', 'message', 'rating']
        widgets={
            'message':forms.Textarea(attrs={'placeholder':'enter text'}),
            'email':forms.TextInput(attrs={'placeholder':'enter valid email'}),
        }


class AddContactForm(forms.ModelForm):
    class Meta:
        model=Contact_Us
        fields=['your_name', 'phone_number', 'email', 'your_message']
        widgets={
            'your_message':forms.Textarea(attrs={'placeholder':'enter your message'},),
            'email':forms.TextInput(attrs={'placeholder':'enter valid email'}),
            'phone number':forms.TextInput(attrs={'placeholder':'enter valid phone number'}),


        }