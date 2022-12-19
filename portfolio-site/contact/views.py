from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import ContactForm

class ContactFormView(FormView):
    template_name = 'contact/base_contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # This method is called when valid form data has ben POSTed.
        # It should return an HttpResponse.
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'contact/base_contact_success.html'
