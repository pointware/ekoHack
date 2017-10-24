from django.conf.urls import url
from .views import UploadMaterial, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
]