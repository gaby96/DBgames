"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dbgames import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='base'),
    path('list_item/', views.list_item, name='list_item'),
    path('add_items/', views.add_items, name='add_items'),
    path('update_items/<str:pk>/', views.update_items, name="update_items"),
    path('delete_items/<str:pk>/', views.delete_items, name="delete_items"),
    path('stock_detail/<str:pk>/', views.stock_detail, name="stock_detail"),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('list_customer/', views.list_customer, name='list_customer'),
    path('update_customer/<str:pk>/', views.update_customer, name="update_customer"),
    path('customer_detail/<str:pk>/', views.customer_detail, name="customer_detail"),
    path('delete_customer/<str:pk>/', views.delete_customer, name="delete_customer"),
    path('add_order/', views.add_order, name="add_order"),
    path('list_order/', views.list_order, name="list_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
    path('order_detail/<str:pk>/', views.order_detail, name="order_detail"),
    path('add_orderitems/', views.add_orderitems, name='add_orderitems'),
    path('list_orderitems/', views.list_orderitems, name='list_orderitems'),
    path('update_orderitems/<str:pk>', views.update_orderitems, name="update_orderitems"),
    path('delete_orderitems/<str:pk>/', views.delete_orderitems, name="delete_orderitems"),
    path('orderitems_detail/<str:pk>/', views.orderitems_detail, name="orderitems_detail")
]
