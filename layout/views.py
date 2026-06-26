"""Preserved CampaignView for the next time we have a preorder campaign"""

from books.views import BooksListView

class LandingView(BooksListView):
    seo_block_slug = "landing"

# class CampaignViewMixin(ButterMixin):

#     def get_page(self, page_type='*', page_slug=None, params={}):
#         """Fetch campaign page from Butter and add tailwind classes"""
#         page_data = Butter.pages.get(page_type, page_slug, params)['data']['fields']
#         print(page_data)
        
#         if "p" in page_data["campaign_instructions"]:
#             page_data["campaign_instructions"] = page_data["campaign_instructions"].replace("<p>", '<p class="mb-8">')
#         if "ul" in page_data["campaign_instructions"]:
#             page_data["campaign_instructions"] = page_data["campaign_instructions"].replace("<ul>", '<ul class="list-disc">')
#         return page_data


# class CampaignFormView(CampaignViewMixin, FormView):
#     template_name = 'campaign.html'
#     form_class = CampaignForm
#     success_url = reverse_lazy('success')

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         sender_email = form.cleaned_data['sender_email']
#         from_email = settings.CONTACT_EMAIL
#         sender_name = form.cleaned_data['sender_name']
#         campaign_name = form.cleaned_data['campaign_name']
#         image_field = form.cleaned_data['image_field']
#         sender_subject = f"New campaign entry: {campaign_name}"
#         full_message = f"You have the following entry for the campaign: {campaign_name}:\n\n"""
#         full_message += f"\n\tFrom Sender: {sender_name}."
#         full_message += f"\n\tSender's email: {sender_email}."
#         message = full_message


#         try:
#             # send_mail(subject, message, from_email, [from_email], fail_silently=False)
#             email = EmailMessage(
#                 subject=sender_subject,
#                 body=message,
#                 from_email=from_email,
#                 to=[from_email],
#                 reply_to=[sender_email]
#             )
#             email.attach(image_field.name, image_field.read(), image_field.content_type)
#             email.send()
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return super().form_valid(form)
