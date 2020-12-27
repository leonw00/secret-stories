from django.urls import path
from .views import LandingPageView, AccountPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name = 'landing'),
    path('accounts/', AccountPageView.as_view(), name = 'accounts'),
]   