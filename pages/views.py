from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = 'landing.html'

class AccountPageView(TemplateView):
    template_name = 'accountPage.html'
