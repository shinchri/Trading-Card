from django.urls import path

from .views import HomeView, ProductDetailView, ProductAddCartView, ShoppingCartView, OrderRemove

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('products/<int:id>/', ProductDetailView.as_view(), name="product-detail"),
    path('products/<int:id>/add-cart/', ProductAddCartView.as_view(), name="product-add-cart"),
    path('shopping-cart/<int:id>/', ShoppingCartView.as_view(), name="shopping-cart"),
    path('remove-order/<int:id>/', OrderRemove.as_view(), name='remove-order')
]