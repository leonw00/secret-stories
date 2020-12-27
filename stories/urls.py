from django.urls import path
from .views import StoryListView, StoryDetailView, StoryCreateView

urlpatterns = [
    path('reading/', StoryListView.as_view(), name = 'reading'),
    path('reading/<uuid:pk>/', StoryDetailView.as_view(), name = 'story_detail'),
    path('writing/', StoryCreateView.as_view(), name = 'writing'),
]