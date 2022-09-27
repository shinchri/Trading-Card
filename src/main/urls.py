from django.urls import path

from .views import HomeView, ProductDetailView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('products/<int:id>/', ProductDetailView.as_view(), name="product-detail"),
]