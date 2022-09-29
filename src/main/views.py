from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Product, Cart, Order

# Create your views here.
class HomeView(generic.TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    products = Product.objects.all()

    context["products"] = products

    return context

class ProductDetailView(generic.TemplateView):
  template_name = 'product-detail.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    
    product_id = self.kwargs.get('id')
    product = Product.objects.get(id=product_id)

    context['product'] = product
    
    return context

class ProductAddCartView(View):
  def post(self, request, **kwargs):
    product_id = self.kwargs.get('id')
    
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=request.user)

    # Create order
    order = Order.objects.create(product=product, cart=cart, price=product.price)
    print(f"{product.name} was put into Cart with order id {order.id} for {request.user.email}")

    return JsonResponse({
      'is_added': True
    })

class ShoppingCartView(generic.TemplateView):
  template_name = 'shopping-cart.html'

  def get_context_data(self, **kwargs):
    context = super(ShoppingCartView, self).get_context_data(**kwargs)

    cart_id = kwargs.get('id')
    
    cart = Cart.objects.get(id=cart_id)
    print(cart)
    print(cart.order_set.all())

    context['cart'] = cart

    return context

