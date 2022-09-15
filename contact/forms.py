from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    """
    Widgets for each reCAPTCHA type:
    
    ReCaptchaV2Checkbox for Google reCAPTCHA V2 – Checkbox
    ReCaptchaV2Invisible for Google reCAPTCHA V2 – Invisible
    ReCaptchaV3 for Google reCAPTCHA V3
    """
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
