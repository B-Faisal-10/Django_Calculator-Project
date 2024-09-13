from django.urls import path, include
from . import views

urlpatterns = [
   path('myfirstpage',views.myfirstpage, name='myfirstpage'),
   path('mysecondpage',views.mysecondpage, name='mysecondpage'),
   path('mythirdpage',views.mythirdpage, name='mythirdpage'),
   path('myimagepage',views.myimagepage, name='myimagepage'),
   path('myimagepage2',views.myimagepage2, name='myimagepage2'),
   path('myform',views.myform, name='myform'),
   path('submitmyform',views.submitmyform, name="submitmyform"),
   path('myform2',views.myform2, name="myform2"),
]
