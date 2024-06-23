from django.urls import path
from .import views
from .api import hobbies_api, create_hobbies_api

urlpatterns = [
    path('', views.profile, name="profile-page"),
    path('hobbies/', views.hobbies, name="hobbies-page"),
    path("api/hobbies_api", hobbies_api, name = "hobbies API"),
    path("api/create_hobbies_api", create_hobbies_api, name = "create hobbies API"),
]
