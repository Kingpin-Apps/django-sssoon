from django import forms
from nocaptcha_recaptcha.fields import NoReCaptchaField


class NewsletterForm(forms.Form):
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.TextInput(attrs={
                                 'id': 'newsletter-email',
                                 'type': 'email',
                                 'title': 'Email',
                                 'name': 'email',
                                 'class': 'form-control transparent',
                                 'placeholder': 'jane.doe@example.com'
                             }))

    captcha = NoReCaptchaField()