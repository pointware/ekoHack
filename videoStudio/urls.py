from django.conf.urls import url
from .views import index, items, videoEdit, dashboard

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^items$', items, name='items'),
    url(r'^videoedit$', videoEdit, name='videoEdit'),
    url(r'^dashboard$', dashboard, name='dashboard'),
]