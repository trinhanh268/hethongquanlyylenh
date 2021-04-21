from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name="ylenh_list"),
    path('createylenh/', views.create_ylenh, name="create_ylenh"),
    path('<int:id>/', views.ylenh_detail),
    path('ylenh_delete/<int:id>', views.ylenh_delete, name="delete_ylenh"),
    # path('ylenh_modify/<int:id>', views.ylenh_modify, name="modify_ylenh")
]