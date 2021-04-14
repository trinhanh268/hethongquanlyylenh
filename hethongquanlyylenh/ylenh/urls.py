from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('createylenh/', views.create_ylenh, name="create_ylenh"),
]