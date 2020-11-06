from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('create/',views.create),
    path('details/<str:pk>',views.details),
    path('update/<str:pk>',views.update),
    path('delete/<str:pk>',views.delete),
]