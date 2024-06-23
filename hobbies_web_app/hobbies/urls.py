from django.urls import path
from .import views
from .api import hobbies_api, create_hobbies_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.profile, name="profile-page"),
    path('hobbies/', views.hobbies, name="hobbies-page"),
    path("api/hobbies_api", hobbies_api, name = "hobbies API"),
    path("api/create_hobbies_api", create_hobbies_api, name = "create hobbies API"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)