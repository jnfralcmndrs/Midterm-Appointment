from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path(
        'appointments/',
        views.appointment_list,
        name='appointment_list'
    ),

    path(
        'appointments/add/',
        views.appointment_create,
        name='appointment_create'
    ),

    path(
        'appointments/<int:appointment_id>/edit/',
        views.appointment_update,
        name='appointment_update'
    ),

    path(
        'appointments/<int:appointment_id>/delete/',
        views.appointment_delete,
        name='appointment_delete'
    ),
]
