from django.contrib import admin
from django.urls import path
from perfume import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("order_form/", views.order_form, name="order_form"),
    # path("process_order/", views.process_order, name="process_order"),
    # Add more URL patterns as needed
]
