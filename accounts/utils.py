from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

def detectUser(user):
    if user.role == 0:
        url = 'customer-dashboard'

    elif user.role == 1:
        url = 'vendor-dashboard'

    elif user.role is None and user.is_superadmin:
        url = '/admin'

    return url

def send_verification_email(request, user):
    current_site = get_current_site(request)
    from_email = settings.DEFAULT_FROM_EMAIL
    email = user.email
    subject = 'Please click the below link to activate your account'

    message = render_to_string('accounts/emails/account_verification_email.html', {
        'current_site': current_site,
        'email': email,
        'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })

    mail = EmailMessage(subject, message, from_email, to=[email])
    mail.send()