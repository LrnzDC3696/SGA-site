from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="main-index"),
    path('about/', views.about, name="main-about"),
    path('contact/', views.contact, name="main-contact"),
    path('sga_officials/', views.sga_officials, name="main-sga_officials"),
    path('batch_governors/', views.batch_governors, name="main-batch_governors"),
]
