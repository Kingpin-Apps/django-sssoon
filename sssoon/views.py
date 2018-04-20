import json

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader

from sssoon.forms import NewsletterForm
from sssoon.models import MailingList


def index(request):
    signupform = NewsletterForm()

    context = {
        'signupform': signupform
    }

    return render(request, 'sssoon/index.html', context)


def video(request):
    signupform = NewsletterForm()

    context = {
        'signupform': signupform
    }

    return render(request, 'sssoon/video.html', context)


def signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        response_data = {}

        # Validate form data
        if form.is_valid():
            email = form.cleaned_data['email']

            new_email, created = MailingList.objects.get_or_create(email=email)

            if created:
                # Email the profile
                template = loader.get_template('sssoon/sign_up_email_template.txt')

                context = {
                    'email': email,
                }

                content = template.render(context)

                message = EmailMessage(
                    "Mailing List",
                    content,
                    settings.SERVER_EMAIL,
                    [email],
                    headers={'Reply-To': email}
                )
                message.send()
                response_data['result'] = 'Success'
                response_data['message'] = 'Your information has been received. Thank you for your interest.'
            else:
                response_data['result'] = 'Failed'
                response_data['message'] = 'This email address is already signed up. Thank you for your enthusiasm!'
            return HttpResponse(json.dumps(response_data), content_type="application/json")
        else:
            # Return an error message.
            response_data['result'] = 'Failed'
            response_data['message'] = 'Please enter a valid email address and reCAPTCHA.'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return redirect('sssoon:index')


def redirect_404(request):
    return redirect('sssoon:index')

