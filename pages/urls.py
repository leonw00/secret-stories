from django.urls import path
from .views import LandingPageView, WritingPageView, AccountPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name = 'landing'),
    path('writing/', WritingPageView.as_view(), name = 'writing'),
    path('accounts/', AccountPageView.as_view(), name = 'accounts'),
]   