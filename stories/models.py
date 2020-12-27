from django.db import models
from django.urls import reverse

class Story(models.Model):
    title = models.CharField(max_length = 140)
    author = models.CharField(max_length = 140)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story_detail', args = [str(self.id)])