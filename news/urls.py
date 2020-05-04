from django.urls import path
from .views import dashboard,createNews
urlpatterns=[
  path('dashboard/',dashboard,name='dashboard'),
    path('create-news/',createNews,name='createnews'),
]