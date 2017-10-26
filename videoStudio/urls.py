from django.conf.urls import url
from .views import index, items, videoEdit, dashboard, videoEditStep1, videoEditStep2, videoEditStep3, videoEditStep4, videoEditStep5, videoTemplate, go

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^index$', index, name='index'),
    url(r'^items$', items, name='items'),
    url(r'^videoedit$', videoEdit, name='videoEdit'),
    url(r'^videotemplate$', videoTemplate, name='videotemplate'),
    url(r'^videoeditstep1$', videoEditStep1, name='videoEditStep1'),
    url(r'^videoeditstep2$', videoEditStep2, name='videoEditStep2'),
    url(r'^videoeditstep3$', videoEditStep3, name='videoEditStep3'),
    url(r'^videoeditstep4$', videoEditStep4, name='videoEditStep4'),
    url(r'^videoeditstep5$', videoEditStep5, name='videoEditStep5'),
    url(r'^dashboard$', dashboard, name='dashboard'),
    url(r'^go/$', go, name='go'),
]