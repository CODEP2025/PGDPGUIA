from django.urls import path
from . import views

app_name = "guia"

urlpatterns = [
    path("", views.home, name="home"),
    path("p/<slug:slug>/", views.procedure_detail, name="procedure_detail"),
]
