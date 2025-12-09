from django import forms
from .models import AdmissionInquiry


class AdmissionInquiryForm(forms.ModelForm):
    class Meta:
        model = AdmissionInquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name*',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address*',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 7,
                'placeholder': 'Questions or Comments'
            }),
        }

    # Optional: Add custom validation if needed
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and "@" not in email:
            raise forms.ValidationError("Enter a valid email address.")
        return email
