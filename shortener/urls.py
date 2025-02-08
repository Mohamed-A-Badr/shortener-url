from django.urls import path
from . import views

urlpatterns = [
    path("shortener/", views.short_url, name="short_url"),
    path("<str:short_code>/", views.redirect_to_website, name="redirect_to_website"),
]
