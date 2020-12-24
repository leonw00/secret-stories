from django.urls import path
from .views import LandingPageView, ReadingPageView, WritingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name = 'landing'),
    path('reading/', ReadingPageView.as_view(), name = 'reading'),
    path('writing/', WritingPageView.as_view(), name = 'writing'),
]   