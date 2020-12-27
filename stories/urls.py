from django.urls import path
from .views import StoryListView, StoryDetailView

urlpatterns = [
    path('reading/', StoryListView.as_view(), name = 'reading'),
    path('reading/<int:pk>/', StoryDetailView.as_view(), name = 'story_detail'),
]