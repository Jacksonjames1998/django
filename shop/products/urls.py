from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name ='about'),
    path('contact',views.contact,name="contact"),
    path('product',views.product,name="product"),
    path('add',views.add, name = "add")
]