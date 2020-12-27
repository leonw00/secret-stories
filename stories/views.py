from django.views.generic import ListView, DetailView
from .models import Story

class StoryListView(ListView):
    model = Story
    context_object_name = 'stories'
    template_name = 'reading.html'

class StoryDetailView(DetailView):
    model = Story
    template_name = 'story/story_detail.html'