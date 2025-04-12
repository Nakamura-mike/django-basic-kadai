from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top"),
    path('crud/product_list', views.ProductListView.as_view(), name="list"),
    path('crud/product_detail/<int:pk>/', views.ProductDetailView.as_view(), name="detail"),
]
