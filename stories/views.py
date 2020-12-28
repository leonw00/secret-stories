from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404
from .models import Story

class StoryListView(ListView):
    model = Story
    context_object_name = 'stories'
    template_name = 'reading.html'

class StoryDetailView(DetailView):
    model = Story
    template_name = 'story/story_detail.html'

class StoryCreateView(CreateView):
    model = Story
    template_name = 'writing.html'
    fields = ('title', 'content')

    
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            return super(StoryCreateView, self).form_valid(form)
        else:
            form.instance.author = None
            return super(StoryCreateView, self).form_valid(form)

class AccountListView(ListView):
    model = Story
    context_object_name = 'stories'
    template_name = 'accountPage.html'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Story.objects.filter(author = self.request.user)