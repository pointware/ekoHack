from django.conf.urls import url
from .views import index, items, videoEdit

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^items$', items, name='items'),
    url(r'^videoedit$', videoEdit, name='videoEdit'),
]