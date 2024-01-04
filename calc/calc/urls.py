from django.contrib import admin
from django.urls import path, include
from perfume import views
from perfume.views import ProductViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("order_form/", views.order_form, name="order_form"),
    path("api/", include(router.urls)),
    # path("process_order/", views.process_order, name="process_order"),
    # Add more URL patterns as needed
]
