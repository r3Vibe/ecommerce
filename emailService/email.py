# email activation
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from tokenService.token import VerificationToken


class EmailSender:
    def __init__(self, domain, subject, user) -> None:
        self.domain = domain
        self.subject = subject
        self.user = user

    def account_activation_mail(self):
        message = render_to_string('email/activation.html', {
            'user': self.user,
            'domain': self.domain,
            'uid': VerificationToken(self.user).encode_pk(),
            'token': VerificationToken(self.user).generate_token()
        })
        to_email = self.user.email
        send_mail = EmailMessage(
            self.subject, message, from_email='arnabgupta84@gmail.com', to=[to_email])
        send_mail.send()

    def account_reset_password_mail(self):
        message = render_to_string('email/reset.html', {
            'user': self.user,
            'domain': self.domain,
            'uid': VerificationToken(self.user).encode_pk(),
            'token': VerificationToken(self.user).generate_token()
        })
        to_email = self.user.email
        send_mail = EmailMessage(
            self.subject, message, from_email='arnabgupta84@gmail.com', to=[to_email])
        send_mail.send()
