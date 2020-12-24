from django.views.generic import TemplateView

class LandingPageView(TemplateView):
    template_name = 'landing.html'

class ReadingPageView(TemplateView):
    template_name = 'reading.html'

class WritingPageView(TemplateView):
    template_name = 'writing.html'

class AccountPageView(TemplateView):
    template_name = 'accountPage.html'
