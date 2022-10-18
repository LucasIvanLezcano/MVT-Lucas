from django.urls import path

from family import views

app_name = "family"
urlpatterns = [
    path("family", views.familier, name="family-list"),
]