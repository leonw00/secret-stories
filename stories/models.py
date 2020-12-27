import uuid
from django.db import models
from django.urls import reverse

class Story(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    title = models.CharField(verbose_name = (''), max_length = 140)
    content = models.TextField(verbose_name = (''), )
    author = models.ForeginKey()
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story_detail', args = [str(self.id)])