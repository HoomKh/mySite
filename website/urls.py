from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [

    path('', index_view, name='index'),
    path('contact', contact_view, name='contact'),
    path('about', about_view, name='about'),
    path('element', element_view, name='element'),
]
