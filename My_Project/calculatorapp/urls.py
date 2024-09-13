from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.root, name='root'),
    path('submitquery', views.submitquery, name='submitquery')
]