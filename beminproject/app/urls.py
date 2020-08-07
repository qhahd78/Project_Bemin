from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/', views.order, name='order'),
    path('order_list/', views.order_list, name='order_list'),
    path('update/<int:item_id>', views.update, name='update'),
    path('delete/<int:item_id>', views.delete, name='delete'),
    path('store/', views.store, name='store'),
]
