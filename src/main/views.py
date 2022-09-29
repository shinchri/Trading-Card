import json
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
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
    Order.objects.create(product=product, cart=cart, price=product.price)

    messages.success(request, f'{product.name} was added to the Shopping Cart.')

    return redirect('main:product-detail', id=product_id)

class ShoppingCartView(generic.TemplateView):
  template_name = 'shopping-cart.html'

  def get_context_data(self, **kwargs):
    context = super(ShoppingCartView, self).get_context_data(**kwargs)

    cart_id = kwargs.get('id')
    
    cart = Cart.objects.get(id=cart_id)

    context['cart'] = cart

    return context

class OrderRemove(View):
  def post(self, request, *args, **kwargs):

    user = request.user
    cart = Cart.objects.get(user=user)

    order_id = kwargs.get('id')

    instance = Order.objects.get(id=order_id)
    product_name = instance.product.name
    instance.delete()
    

    messages.success(request, f'{product_name} was removed from Shopping Cart.')

    return redirect('main:shopping-cart', id=cart.id)