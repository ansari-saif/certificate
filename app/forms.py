from django import forms
from django.core.validators import validate_email

class EmailForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        required=True,
        error_messages={
            'invalid': 'Invalid email address. Please enter a valid email.',
        }
    )
