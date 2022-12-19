from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    name = forms.CharField(label=False, max_length=100)
    email = forms.EmailField(label=False, max_length=100)
    subject = forms.CharField(label=False, max_length=100)
    message = forms.CharField(label=False, widget=forms.Textarea)

    def get_info(self):
        """Method that returns formatted information
        :return: subject, msg
        """

        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n\n"Subject: {subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
