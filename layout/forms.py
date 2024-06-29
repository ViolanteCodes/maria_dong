from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

def validate_dong(value):
    if value.lower() != "dong":
        raise ValidationError(message="Please type Maria's last name in the box.",
            params={'value': value},
        )

class ContactForm(forms.Form):
    sender_email = forms.EmailField(label='Your Email', required=True)
    sender_name = forms.CharField(label='Your Name', required=True)
    sender_subject = forms.CharField(label='Your Subject', required=True)
    message = forms.CharField(label='What would you like to say?', widget=forms.Textarea, required=True)
    dong_field = forms.CharField(label="In the box, type Maria's last name.", required=True, validators=[validate_dong])

class CampaignForm(forms.Form):

    MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB in bytes   
    sender_email = forms.EmailField(label='Your Email', required=True)
    sender_name = forms.CharField(label='Your Name', required=True)
    campaign_name = forms.CharField(label="Campaign Name")
    image_field = forms.ImageField(
        label="Upload your image here", 
        required=True, 
        validators=[
                FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'webp']),
            ]
        )
    dong_field = forms.CharField(label="In the box, type Maria's last name.", required=True, validators=[validate_dong])

    def clean_image_field(self):
        image = self.cleaned_data.get('image_field')
        if image:
            if image.size > self.MAX_FILE_SIZE:
                raise forms.ValidationError(f'File size must be less than {self.MAX_FILE_SIZE/(1024*1024)} MB.')
        return image
