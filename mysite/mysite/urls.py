
from django.contrib import admin
from django.urls import path, include
from.import views as mysite_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('',mysite_views.index, name='index'),
    path('profile/',mysite_views.profile, name='profile'),
]

