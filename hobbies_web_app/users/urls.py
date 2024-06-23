from django.urls import path
from .import views
from .api import person_api, persons_api
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/person_api/<slug:slug>", person_api, name = "person API"),
    path("api/persons_api", persons_api, name = "persons API")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)