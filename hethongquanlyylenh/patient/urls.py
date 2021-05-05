from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('create_patient', views.create_patient, name="patient_create"),
    path('delete_patient/<int:id>/', views.delete_patient, name="patient_delete"),
    path('modify_patient/<int:id>/', views.modify_patient, name="patient_modify")
]