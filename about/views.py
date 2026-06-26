from seo.mixins import SEOBlockMixin
from about.models import AboutPage
from django.conf import settings
from about.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import FormView
from about.models import SocialIcon


# Create your views here.

class AboutView(SEOBlockMixin, FormView):
    seo_block_slug = "about"
    template_name = "about.html"
    form_class = ContactForm
    success_url = 'success/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        sender_email = form.cleaned_data['sender_email']
        from_email = settings.CONTACT_EMAIL
        sender_name = form.cleaned_data['sender_name']
        sender_subject = form.cleaned_data['sender_subject']
        message = form.cleaned_data['message']
        full_message = "You have the following contact form submission from Maria Dong.com:\n\n"""
        full_message += f"\n\tFrom Sender: {sender_name}."
        full_message += f"\n\tSender's email: {sender_email}."
        full_message += f"\n\tSubject: {sender_subject}."
        full_message += f"\n\tMessage:\n\n\t{message}"
        message = full_message

        try:
            # send_mail(subject, message, from_email, [from_email], fail_silently=False)
            email = EmailMessage(
                subject=sender_subject,
                body=message,
                from_email=from_email,
                to=[from_email],
                reply_to=[sender_email]
            )
            email.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["object"] = AboutPage.objects.all().first()
        return context

class SuccessView(TemplateView):
    template_name = "success.html"
