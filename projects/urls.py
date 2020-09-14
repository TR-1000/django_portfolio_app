from django.urls import path
from .import views

urlpatterns = [
    path("", views.projects, name="projects"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
]
