from django import forms
from django.core.exceptions import ValidationError

def validate_dong(captcha_phrase, captcha_answer):
    if captcha_answer.lower() != captcha_phrase.lower():
        raise ValidationError(message="Please type the captcha word into the box.",
            params={'value': value},
        )

class ContactForm(forms.Form):
    sender_email = forms.EmailField(label='Your Email', required=True)
    sender_name = forms.CharField(label='Your Name', required=True)
    sender_subject = forms.CharField(label='Your Subject', required=True)
    message = forms.CharField(label='What would you like to say?', widget=forms.Textarea, required=True)
    dong_field = forms.CharField(label="In the box, type Maria's last name.", required=True, validators=[validate_dong])