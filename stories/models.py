import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Story(models.Model):
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False,
    )
    title = models.CharField(verbose_name = (''), max_length = 140)
    content = models.TextField(verbose_name = (''), )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        blank = True,
        null = True,
    )
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story_detail', args = [str(self.id)])