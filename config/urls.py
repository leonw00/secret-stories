from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('adomindo/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', include('pages.urls')),
    path('stories/', include('stories.urls')),
]
